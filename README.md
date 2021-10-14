=====
shopping
=====
#Online Shop
A simple django ecommerce project

How to Run?
#1- Clone the repository:
```bash
 $ git clone https://github.com/mmdhossien/ShoppingProject/tree/phaze_2
 $ cd Shopping
```

#2- Create a virtualenv and activate it:
```bash
Windows:
py -3 -m venv venv
venv\Scripts\activate
```
```bash
Linux:
$ python3 -m venv venv
$ . venv/bin/activate
```
#3- In settings.py set up the your database:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebi',
        'USER': 'postgres',
        'PASSWORD': 'your password',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

#4- In settings.py set up the your email:
```bash
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```


#5- Install the requirements :
```bash
pip install -r requirements.txt
```
#6- Write the following commands to create your tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

#7- Run the development server:
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000 in your browser.`