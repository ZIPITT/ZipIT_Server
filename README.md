# ZipIT_Server
```bash
.
├── API
│   ├── __init__.py
│   ├── admin.py
│   ├── api
│   │   ├── _init_.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20180428_0730.py
│   │   └── __init__.py
│   ├── models.py
│   └── tests.py
├── README.md
├── db.sqlite3
├── manage.py
└── rest
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
    ```
Here is the structure of Backend part or the server side.

-The api has been created with the dummy data from the backend,which is accessable on http://127.0.0.1:8000/api in the local server.
-Sqlite has been used as the database can change the database from the settings file.
-The schema and other validations has yet to be done.

Steps to run the Django app-
1.clone the repository.
2.install django.
3.go to the directory of the repository and run commands - 
python manage.py migrate.
python manage.py runserver.
