### Описание проекта:
Блог про еду, созданный на Django. Сделан по шаблону, находившемуся в открытом 
доступе. Реализованно:

-Создание, редактирование и удаление статьи;  
-Просмотр статей других пользователей;  
-Авторизация и регистрация пользователей;  
-Профиль пользователя, а так же его редактирование;  
-Реализованы базовые права (администратор и пользователь);  
-Реализована панель администратора;  
-Реализованы категории и теги, поиск по ним;  



### Инструменты разработки

**Стек:**
- Python >= 3.9
- Django == 5.0.1
- sqlite3

## Разработка

##### 1) Клонировать репозиторий

    git clone https://github.com/OrKelly/foodei_blog.git

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение
    
Linux

    source venv/bin/activate
    
Windows

    ./venv/Scripts/activate

##### 4) Устанавить зависимости:

    pip install -r requirements.txt

##### 5) Запуск сервера:
    
    python manage.py runserver

##### 6) Ссылки

- Сайт http://127.0.0.1:8000/

- Админ панель http://127.0.0.1:8000/admin
