python m - venv test_env
.\test_env\Scripts\activate

pip install Django==4.2

django-admin startproject project_pertama
cd project_pertama

REM python -m pip install kalau venv tidak muncul
REM py -m pip install kalau tidak bisa python
REM py -m pip list 

python manage.py makemigrations
python manage.py startapp pengguna

REM run the app
.\test_env\Scripts\activate
cd web-django/test_env/Scripts/project_pertama
python manage.py runserver

python manage.py createsuperuser REM untuk buat admin (username, email, password)
python manage.py migrate REM untuk apply migrations

python manage.py makemigrations REM untuk create models
python manage.py migrate REM setiap create models harus selalu dimigrate