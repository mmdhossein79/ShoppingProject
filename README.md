=====
shopping
=====
#Online Shop
A simple django ecommerce project

How to Run?
#1- Clone the repository:
$ git clone https://github.com/mmdhossien/ShoppingProject/tree/phaze_2
$ cd Shopping

#2- Create a virtualenv and activate it:

Windows:
py -3 -m venv venv
venv\Scripts\activate

Linux:
$ python3 -m venv venv
$ . venv/bin/activate

#3- In settings.py set up the your database:
-  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebi',
        'USER': 'postgres',
        'PASSWORD': 'your password',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}-

#4- In settings.py set up the your email:

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'


#5- Install the requirements :
pip install -r requirements.txt

#6- Write the following commands to create your tables:
python manage.py makemigrations
python manage.py migrate

#7- Run the development server:
python manage.py runserver
Open http://127.0.0.1:8000 in your browser.