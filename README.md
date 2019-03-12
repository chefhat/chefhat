# chefhat
### Chefhat.org | @Chefhat_app | A recipe app.

## INSTALLATION
1. Install necessary packages.
```sh
$ sudo apt-get install git
$ sudo apt-get install build-essential libffi-dev libpq-dev libssl-dev openssl zlibc zlib1g zlib1g-dev
$ sudo apt-get install python3-pip python3-dev
$ sudo apt-get install python3.7
```
2. Make python alias.
```sh
$ sudo echo "alias python=python3.7" >> .bashrc
```
3. Ensure pip list is empty.
```sh
$ sudo pip freeze > requirements.txt
$ sudo pip uninstall -r requirements.txt
$ sudo rm -rf requirements.txt
```
4. Install global pip packages.
```sh
$ sudo pip install autopep8 pylint //if you want vscode linting
$ sudo pip install pipenv
```
5. Ensure virtualenvs folder is empty.
```sh
$ sudo rm -r .local/share/virtualenvs/* .local/share/virtualenvs/.*
```
6. Navigate to the directory you want the chefhat repository stored, clone the repository, then go into it.
```sh
$ cd ~/<SOMEDIRECTORYWHEREYOUWANTCHEFHAT>/
$ git clone git@github.com:<YOURGITHUBUSERNAME>/chefhat.git
$ cd chefhat
```
7. Add upstream target chefhat/chefhat.
```sh
$ git remote add upstream git://github.com/chefhat/chefhat.git
$ git fetch upstream
```
8. Ensure no pipenv exists at chefhat repository and create a new pipenv, installing all required pip packages.
```sh
$ pipenv --rm
$ pipenv --python 3.7
$ pipenv install
$ pipenv install --dev //if you want vscode linting
```
9. Enter pipenv.
```sh
$ pipenv shell
```
10. At this point you must fetch the local_settings.py from Discord and put it in chefhat/chefhat such that it resides in the same folder as settings.py.
11. Initial database.
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```
12. Start the server. You're done setting up!
```sh
$ python manage.py runserver
```
13. Now we end the server and leave the pipenv.
```sh
$ ^c //to end server
$ exit //to leave pipenv
```

# FURTHER CHANGES
1. Go into chefhat.
```sh
$ cd chefhat
```
2. Get latest chefhat/stag changes.
```sh
$ git pull upstream stag
```
3. Enter pipenv.
```sh
$ pipenv shell
```
4. Ensure database is updated.
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
5. You're now good to make your changes.
