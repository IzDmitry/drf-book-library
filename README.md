# drf-book-library
Книжная библиотека, созданная с помощью Django Rest Framework.

## Особенности реализации

- Есть небольшой фронтенд на vue


## В API доступны следующие эндпоинты
- GET `/book/` - Возвращает список книг в базе данных в формате JSON
- GET `/book/{{id}}/` - Возвращает единственное представление указанного идентификатора книги в формате JSON
- POST `/book/` - Создает новую книгу с указанными деталями — ожидает тело JSON.
- PUT `/book/{{id}}/` - Обновляет существующую книгу. Ожидается тело JSON.
- POST `/user/` - Создает нового пользователя и отправляет email

## Развертывание проекта

### Развертывание на локальном сервере

1. Выполните команду `docker-compose up`.
