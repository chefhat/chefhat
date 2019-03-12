# chefhat
### Chefhat.org | @Chefhat_app | A recipe app.

## Installation

Chefhat uses [Django](https://docs.djangoproject.com/en/2.1/intro/install/_) and requires [Python 3.7.2](https://www.python.org/downloads/release/python-372/)

1. Fork and clone the repository.
2. Ensure you have a .env file satisfying all the requirements.
3. Execute commands in chefhat root directory:
```sh
$ pipenv install.
$ pipenv run python3 manage.py migrate.
```
4. Activate your project's virtual environment: 
```sh
$ pipenv shell.
```
5. Inside your virtual environment, execute the following command and follow the steps to create a superuser,  For local installations, username and password do not need to be complex.:
```sh
$ python manage.py createsuperuser
```


6. Run the server: 
```sh
$ pipenv run python3 manage.py runserver
```
7. Naviagte to [localhost:8000/admin](localhost:8000/admin) and sign in with your superuser.
8. You can go to [localhost:8000/recipes](localhost:8000/recipes) to view the recipes you create.