
![Build Status ](https://github.com/Yurasblv/socialweb/actions/workflows/django.yml/badge.svg?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge)

    https://socialappgreet.herokuapp.com/



To recreate app from hub first of all clone this repository on your pc:

    git clone: https://github.com/Yurasblv/socialweb.git

Then u need to create .env.dev file and use there your personal settings:
    
    DEBUG= ...
    ALLOWED_HOSTS= ...
    SECRET_KEY= ...

To launch an app use command:
    
    docker-compose up 

While app is working create admin role by command:

    1. docker exec -it container_id bash
    2. python manage.py createsuperuser

