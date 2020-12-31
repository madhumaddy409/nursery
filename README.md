# nursery

## Setup and Installation

1) pip install requirements.txt

2)python manage.py makemigrations

3)python manage.py migrate

4)python manage.py createsuperuser

## giver username , email and password

5)python manage.py runserver

then check on browser
http://127.0.0.1:8000/

API Endpoints

## user registraion
http://127.0.0.1:8000/api/user/register/

## user login
http://127.0.0.1:8000/api/user/login/

## nursery registraion
http://127.0.0.1:8000/api/nursery/register/

## nursery login
http://127.0.0.1:8000/api/nursery/login/

## nursery user can add plants
http://127.0.0.1:8000/api/nursery/addplant/

## plants which are available to user 
http://127.0.0.1:8000/api/nursery/plants/

## plants details for example plant name called Crassula Green Mini Plant
http://127.0.0.1:8000/api/nursery/plants/Crassula Green Mini Plant/

## user can place the order 
http://127.0.0.1:8000/api/order/addorder/

## nusery can able to retrieve user oredr
http://127.0.0.1:8000/api/order/name_of_the_nursery




