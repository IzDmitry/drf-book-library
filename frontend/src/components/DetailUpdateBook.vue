<template>
    <div>
        <!-- Single Book -->
        <ul class="books">
            <li class="book card">
                <h4 class="book__name">{{ name_of_book }}</h4>
                <p class="text-muted">{{ isbn }}</p>
            </li>
        </ul>

        <form method="post">
            <h4 class="form__title">Update book</h4>

            <div class="form-group">
                <input type="text" v-model="name_of_book" class="form-control" placeholder="Name of book">
            </div>

            <div class="form-group">
                <input type="text" v-model="isbn" class="form-control" placeholder="ISBN">
            </div>

            <div class="form-group">
                <input type="text" v-model="first_name" class="form-control" placeholder="Firstname of Author">
            </div>

            <div class="form-group">
                <input type="text" v-model="last_name" class="form-control" placeholder="Lastname of Author">
            </div>

            <div class="form-group">
                <input type="text" v-model="date" class="form-control" placeholder="Date">
            </div>

            <div class="form-group">
                <button class="btn btn-primary" type="button" @click="updateSingleBook()">
                    Update
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from "axios";
let baseURL = "http://localhost:1337/api/";

export default {
    name: 'DetailUpdateBook',
    data() {
        return {
            book_id: "",
            name_of_book: "",
            isbn: "",
            first_name: "",
            last_name: "",
            date: "",
        }
    },
    methods: {
        updateBook() {
            console.log(this.$route.params.id);
        },
        async getSingleBook() {
            try {

                let objectID = this.$route.params.id;
                const res = await axios.get(`${baseURL}book/${objectID}/`);

                this.book_id = res.data.id;
                this.name_of_book = res.data.name;
                this.isbn = res.data.isbn;
                this.first_name = res.data.author.split(' ')[0];
                this.last_name = res.data.author.split(' ')[1];
                this.date = res.data.date;
            } catch (e) {
                console.log("Err: ", e);
            }
        },
        updateSingleBook() {

            let objectID = this.$route.params.id;

            axios({
                method: "PUT",
                url: `${baseURL}book/${objectID}/`,
                data: {
                    "name": this.name_of_book,
                    "isbn": this.isbn,
                    "author": {
                        "first_name": this.first_name,
                        "last_name": this.last_name
                    },
                    "date": this.date,
                },
                headers: {
                    "Content-Type": "application/json"
                }
            })
                .then(() => {
                    alert("Update");
                })
                .catch((err) => {
                    console.log("Erorr: ", err);
                });
        }
    },
    mounted() {
        this.getSingleBook();
    },
}
</script>

<style scoped>
ul.books {
    list-style: none;
    display: flex;
    margin-top: 60px;
    max-width: 100%;
    flex-wrap: wrap;
    margin-left: 0px;
    padding-left: 0%;
}

a.book__author {
    color: #575252;
    text-decoration: underline;
}

a.link-text {
    color: #080707;
}

li.book {
    padding: 20px;
    justify-content: center;
    width: 30%;
    margin: auto;
    margin-bottom: 20px;
    background-color: #08070736;
}

form {
    max-width: 50%;
    margin: auto;
    margin-top: 40px;
}

h4.form__title {
    margin-bottom: 20px;
}

form input.form-control {
    margin-bottom: 20px;
    height: 40px;
    border-radius: 4px;
}

form button.btn {
    padding: 12px 40px;
    width: 100%;
    background-color: #525252;
    font-size: 13px;
}

@media screen and (max-width: 489px) {
    form {
        max-width: 100%;
        padding-bottom: 60px;
    }

    li.book {
        width: 100%;
    }
}
</style>