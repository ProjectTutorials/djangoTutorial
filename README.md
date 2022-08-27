# djangoTutorial

## 1. To get started
```
pip install django
```

```
pip install pipenv
```

### 2. In the folder - Create skeleton
```
pipenv install django
```

```
django-admin startproject djangoProject .
```

### 3. Run

```
python manage.py runserver
```
It should look like this at [localhost:8000](localhost:8000)
![image](https://user-images.githubusercontent.com/76637730/187042587-0955dd48-d46e-46fd-8844-3fa342340dbb.png)


### 4. Create APP

```
python manage.py startapp playground
```
It will add `playground` in the directory.


### 5. django-debug-toolbar

[Reference](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

On `no such table: django_session` error run :
```
python manage.py makemigrations
python manage.py migrate
```
