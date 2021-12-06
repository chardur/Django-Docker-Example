# Django-Docker-Example
A reusable "Quick Start" for Django Docker Projects. (Base Django project with some common initial settings)

## To get started:
(This assumes you have docker/docker-compose installed on a linux system)


Download the github zip file and extract the contents of the `Django-Docker-Example` folder into your project folder. Then run the following command in the project folder: 

`docker-compose build`


## You can then launch the app using:
 
`docker-compose --env-file .env.dev up`

## warning
(for production make a .env file with production secrets and passwords, then run the app with: `docker-compose up`)


## It may be helpful to run this command to setup a superuser for the django admin pages:

`docker-compose run app sh -c "python manage.py createsuperuser"` (if you have created a .env)

or in the dev environment:

`docker-compose --env-file .env.dev run app sh -c "python manage.py createsuperuser"`

## You can run unit tests by running:
`docker-compose run app sh -c "python manage.py test"`

or with linting:

`docker-compose run app sh -c "python manage.py test && flake8"`

or in the dev environment:

(`docker-compose --env-file .env.dev run app sh -c "python manage.py test"`
