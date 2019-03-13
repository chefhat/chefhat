# Chefhat
### chefhat.org | @chefhatapp | A recipe app.

## SSH KEY REGISTRATION
#### Preconditions:
1. You have a GitHub account.
2. You have a Heroku account.
#### Steps:
1. Go to your home directory and generate a new key.
```sh
$ cd ~
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
  - Press enter to accept the default location.
  - Then enter a passphrase.
  - Then enter that passphrase again.
2. Add the SSH key to the SSH agent.
```sh
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_rsa
```
3. Adding the SSH key to the SSH agent every session is tedious, so it should be automated. Paste the following code into a file called ```ssh_helper.txt``` and place it in your home directory.
```sh
SSH_ENV="$HOME/.ssh/env"

function start_agent {
    echo "Initialising new SSH agent..."
    /usr/bin/ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
    echo succeeded
    chmod 600 "${SSH_ENV}"
    . "${SSH_ENV}" > /dev/null
    /usr/bin/ssh-add;
}

# Source SSH settings, if applicable

if [ -f "${SSH_ENV}" ]; then
    . "${SSH_ENV}" > /dev/null
    #ps ${SSH_AGENT_PID} doesn't work under cywgin
    ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
        start_agent;
    }
else
    start_agent;
fi
```
4. Add the code above to your global bash process.
```sh
$ echo -e "\n\n" >> .bashrc
$ cat ssh_helper.txt >> .bashrc
$ sudo rm -rf ssh_helper.txt
```
5. Copy the SSH key to your clipboard.
```sh
$ sudo apt-get install xclip
$ xclip -sel clip < ~/.ssh/id_rsa.pub
```
6. To add your SSH key to GitHub, go to Settings > SSH and GPG keys > New SSH key. Enter your copied SSH public key into the key field and enter a useful identifier into the title key.
7. To add your SSH key to Heroku, go to Account settings > SSH keys > Add. Enter your copied SSH public key into the key field.
8. Make a backup of your SSH keys from your home directory.
```sh
$ sudo tar -czvf ssh.tar.gz .ssh
```
9. Now your SHH keys will enable you to easily work with GitHub/Heroku without signing in as frequently. They're backed up too.

## GPG COMMIT SIGNING
#### Preconditions:
1. You have a GitHub account.
#### Steps:
1. Go to your home directory and generate a new key.
```sh
$ gpg --full-generate-key
```
  - Press enter to accept "RSA and RSA".
  - Enter "4096" for the desired key size.
  - Let the key be available for a year.
  - Verify your selections.
  - Enter your full name "firstname lastname".
  - Enter the email you use for GitHub.
  - You can leave the comment empty.
  - Your passphrase must be decently complex.
2. Locate the newly created GPG key.
```sh
$ gpg --list-secret-keys --keyid-format LONG
```
  - Physically copy the key ID which you just created.
    - The key expires a year from now.
  - The key is just a string of letters and numbers.
  - The key is in the format below. You want just the key ID.
    - ```sec   4096R/KEY_ID 2016-03-10 [expires: 2017-03-10]```
3. Ensure git always signs commits on your system.
```sh
$ git config --global commit.gpgsign true
$ git config --global user.signingkey KEY_ID
```
4. Print the GPG key to your terminal.
```sh
$ gpg --armor --export KEY_ID
```
5. Physically copy your GPG public key. Copy, the identifying statements, from:
```sh
-----BEGIN PGP PUBLIC KEY BLOCK-----
```
  - All the way to:
```sh
-----END PGP PUBLIC KEY BLOCK-----
```
  - Again, make sure to include the two statements above in your copy.
6. To add your GPG key to GitHub, go to Settings > SSH and GPG keys > New GPG key. Enter your copied GPG public key into the key field and enter a useful identifier into the title key.
7. Make a backup of your GPG keys from your home directory.
```
$ sudo tar -czvf gnupg.tar.gz .gnupg
```
8. Now all of your commits will be signed, and your GPG keys are backed up.

## INSTALLATION
#### Preconditions:
1. You have a GitHub account.
2. Your GitHub account has an SSH key registered.
3. You've forked the chefhat repository.
4. You've an understanding of basic Bash & Git commands.
#### Steps:
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
3. Ensure global pip package list is empty.
```sh
$ sudo pip freeze > requirements.txt
$ sudo pip uninstall -r requirements.txt
$ sudo rm -rf requirements.txt
```
4. Install global pip packages.
  - If you don't want autocomplete/linting support in vscode you don't have to follow the tagged command. It's just easier to get it out of the way now.
```sh
$ sudo pip install autopep8 pylint //for vscode autocomplete/linting
$ sudo pip install pipenv
```
5. Ensure virtualenvs folder is empty.
```sh
$ sudo rm -r .local/share/virtualenvs/* .local/share/virtualenvs/.*
```
6. Navigate to the directory you want your forked chefhat repository stored, clone your forked repository, then enter the directory.
```sh
$ cd ~/DIRECTORY-WHERE-YOU-WANT-CHEFHAT/
$ git clone git@github.com:YOUR-GITHUB-USERNAME/chefhat.git
$ cd chefhat
```
7. Add git upstream target chefhat/chefhat/stag, so chefhat/chefhat/stag will always outrank YOUR-GITHUB-USERNAME/chefhat/stag. Then pull any changes.
```sh
$ git remote add upstream git://github.com/chefhat/chefhat.git
$ git pull upstream stag
```
8. Ensure no pipenv exists at chefhat repository and create a new pipenv, installing all required pip packages.
  - If you don't want autocomplete/linting support in vscode you don't have to follow the tagged command. 
```sh
$ pipenv --rm
$ pipenv --python 3.7
$ pipenv install
$ pipenv install --dev //for vscode autocomplete/linting
```
9. Enter pipenv.
```sh
$ pipenv shell
```
10. At this point you must fetch ```local_settings.py``` from Discord and put it in the chefhat/chefhat directory such that it resides in the same directory as settings.py.
11. Now you initial the database.
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```
12. Now start the server. If you run into any errors by this point let someone know; if not, you're done setting up!
```sh
$ python manage.py runserver
```
* You can access your server by going to localhost:8000 or 127.0.0.1:8000

13. While inside your server, you can run Python commands by executing the following in terminal. It will start a Python shell inside the VM.
```sh
$ python manage.py shell
```

14. End the server and then leave the pipenv.
```sh
$ ^c
$ exit
```

## MAKING FURTHER CHANGES
### Local Changes
#### Preconditions:
1. You followed the installation process described as above and ran into zero, or resolved all, errors associated with that process.
#### Steps:
1. Go into the chefhat directory.
```sh
$ cd chefhat
```
2. Get latest chefhat/chefhat/stag changes.
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
5. At this point you can be sure you're running the latest build of chefhat/chefhat/stag and can safely work to extend it.

### Devleoping with Heroku CLI
#### Preconditions:
1. You have a Heroku account.
2. You have install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

#### Steps:

1. After installing the Heroku CLI, you can log in by executing
```sh
$ heroku login      //this will open your web browser
$ heroku login -i   //this will allow you to enter credentials through the CLI
```

You can execute commands on the Chefhat app using the Heroku CLI, for example:

```sh
$ heroku run bash -a chefhat-stag
```
This starts a bash terminal that controls the chefhat-stag Heroku server. You must use the ```-a``` flag to specify which app you want to execute the command on.

## COMMITTING CHANGES

#### Preconditions:
1. You have forked the Chefhat repository.
2. You have GPG and SSH key verification set up.
3. You are developing in the ```stag``` repo.

#### Steps:

1. Before you begin developing in staging, ensure your working directory is up to date.
```sh
$ git pull upstream stag
```
* If you have uncommitted changes, run a ```git stash``` to stash them and then do a pull. Once your directory is up to date, unstash your changes and commit them.
2. Once you have made changes, add them to be committed to your forked repo.
 ```sh 
 $ git add [filename]
 ```
3. Once your files areadded, you can commit them with a message.
```sh
$ git commit -m "Your message here."
```
* At this point, if you have GPG signatures set up, you will be notified with a pop-up asking you for your key password. Type it in to proceed.
4. Push your changes to your forked Chefhat repo.
```sh
$ git push
```
5. Navigate to https://github.com/[your_username]/chefhat/ and switch to the ```stag``` branch. Next to the branch dropdown there is a button labeled "New pull request." Clicking on that brings you to a new screen where you merge the head repository (your fork) with the base repository (chefhat staging). Compare your changes, and click the green "Create pull request" button.

6. From here, your pull request will be created, and you can either merge it now or add reviewers so others can examine your work.

7. Once your pull request is merged, Heroku will automatically execute a new build and update the [Chefhat-stag server](https://chefhat-stag.herokuapp.com/admin/)