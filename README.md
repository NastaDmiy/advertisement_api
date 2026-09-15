# Advertisement API

REST API для сайта объявлений на Flask.

## Стек технологий

- Python 3

- Flask 2.3.3

- Flask-SQLAlchemy 3.0.5

- SQLite



## Установка

```bash

pip install -r requirements.txt

```
## Запуск

```bash

python app.py

```

## API методы

POST /advertisements — создать объявление

Тело запроса (JSON):


```bash

{
  "title": "Продам квартиру",
  "description": "3-комнатная квартира в центре",
  "owner": "Иван Петров"
}

```

Ответ: 201 Created + объект объявления

## GET /advertisements/{id} — получить объявление по ID

Ответ: 200 OK + объект объявления

Пример: GET /advertisements/1

## GET /advertisements — получить все объявления

Ответ: 200 OK + список всех объявлений

## DELETE /advertisements/{id} — удалить объявление

Ответ: 200 OK + сообщение об успешном удалении

Пример: DELETE /advertisements/1
