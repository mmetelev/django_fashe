# Fashe Shop

---

### Цель проекта.

Создание магазина с подробным описанием товара и его оплатой.
Python, Django, PostgresSQL

---

### Установка.

1. Клонируйте проект с помощью git clone или скачайте ZIP-архив.
2. Перейдите в папку с проектом и создайте виртуальное окружение.

~~~
    python3 -m venv venv
~~~

3. Установите все необходимые пакеты.

~~~
    pip install -r requirements.txt
~~~

4. Сделайте миграции

~~~
    python manage.py makemigrations
    python manage.py migrate
~~~

5. Запустите проект.

~~~
    python manage.py runserver
~~~

6. Создайте суперпользователя.

~~~
    python manage.py createsuperuser
~~~