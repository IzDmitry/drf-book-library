import { createWebHistory, createRouter } from "vue-router";
const routes = [
    {
        path: "/books/",
        alias: "/books/",
        name: "books",
        component: () => import("./components/GetBooks")
    },
    {
        path: "/book/:id/",
        alias: "/book/:id/",
        name: "book-details",
        component: () => import("./components/DetailUpdateBook")
    },
    {
        path: "/book/",
        name: "book",
        component: () => import("./components/CreateBook")
    },
    {
        path: "/user/",
        name: "user",
        component: () => import("./components/CreateUser")
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;