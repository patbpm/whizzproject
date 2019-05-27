# FOOD TECH WEBSITE 

The goal is to allow food science and food technology discussion

#Running the Project Locally

First, clone the repository to your local machine:

    git clone https://github.com/patbpm/whizzproject.git

create and start a a virtual environment
    python -m venv myvenv

Install the project dependencies:

    pip install -r requirements.txt

Setup the local configurations:

cp .env.example .env

Set up the database:
 Download XAMP



Create Migration
python manage.py migrate

Create a new superuser for the admin
    python manage.py createsuperuser

Finally, run the development server:

    python manage.py runserver

The project will be available at 127.0.0.1:8000.

Optional
 1. How to use git in VSC
 Open the command palette using Ctrl + Shift + P.
 Type - Select Default Shell
 Select Git Bash from the options
 Click on the + icon in the terminal window

 2. How to install XAMPP
  look at https://pureinfotech.com/install-xampp-windows-10/
  and at https://www.apachefriends.org/download.html
