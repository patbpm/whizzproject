# FOOD TECH WEBSITE 

The goal is to allow food science and food technology discussion

#Running the Project Locally

First, clone the repository to your local machine:

git clone https://github.com/patbpm/whizzproject.git

Install the requirements:

pip install -r requirements.txt

Setup the local configurations:

cp .env.example .env

Create the database:

python manage.py migrate

Finally, run the development server:

python manage.py runserver

The project will be available at 127.0.0.1:8000.