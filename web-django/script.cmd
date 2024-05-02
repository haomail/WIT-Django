python m - venv test_venv
.\test_venv\Scripts\activate

pip install Django==4.2

django-admin startproject project_pertama
cd project_pertama

REM python -m pip install kalau venv tidak muncul
REM py -m pip install kalau tidak bisa python
REM py -m pip list 

python manage.py makemigrations
python manage.py startapp pengguna
