# Сервис для управления списком книг

## Описание

Проект описывает работу сервиса для управления списком книг. Сервис разработан в качестве
тестового задания для компании Alteasy. Задание можно найти в файле task.md.

## Проект

## Документация API

<http://localhost/api/doc/v1/download/>

<http://localhost/api/doc/v1/swagger/>

<http://localhost/api/doc/v1/redoc/>

## Технологии

Python 3.11

Django 4.2

Django REST Framework 3.15.1

DRF-Spectacular 0.27.2

PostgreSQL 16

## Запуск проекта

- клонировать репозиторий

```
git clone git@github.com:SunnyInHouse/books_management.git
```

- в директории books_management создать файл .env и наполнить его по примеру .env_sample

```
DEBUG=False
DJANGO_SECRET_KEY=django-secret

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=books_]
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres-books
DB_PORT=5432
```

### Предупреждение

```
Если вы используете Windows, убедитесь, что файл run_app.sh имеет формат конца строки LF
```

- перейти в директорию infra

```
cd infra 
```

- запустить сборку контейнеров:

```
docker-compose up -d
```

- проект доступен по адресу:

```
http://localhost/
```
- документация доступна по адресу:

```
http://localhost/api/doc/swagger/v1/
```

- после запуска проекта в базе данных уже есть пользователь-суперюзер:

```
{
    "username": "admin",
    "password": "admin"
}
```


## Команда проекта

[SunnyInHouse](https://github.com/SunnyInHouse)

