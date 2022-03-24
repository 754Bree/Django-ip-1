# My Gallery
## Author
[Briana Odhiambo](https://github.com/bree)

## Live Link
* [here] (**)

## Description
 My Gallery is an application developed using Django to display my photos. Other people can also see the photos when they visit the site, and the user can click on the image to view the details of an image.

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: source virtual/bin/activate
* Install all the requirements found in requirements.txt file.
* On your terminal run python3.6 manage.py runserver
* Access the live site using the local host provided

## Getting started

#### The application requires the following installations to operate 
* python3.8
* virtual environment
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```**```

* Create and activate the virtual environment
    ```python3.8 -m virtualenv virtual```
    ```source virtual/bin/activate```

* Move to the folder and install requirements
    ```pip install -r requirements.txt```

## Setting up environment variables
Create a .env file and paste paste the following filling where appropriate:

* SECRET_KEY='Generate one that suits you'
* DEBUG=True
* DB_NAME='gallery'
* DB_USER='<your database name>'
* DB_PASSWORD='<password to your database>'
* DB_HOST='127.0.0.1'
* MODE='dev'
* ALLOWED_HOSTS='*'
* DISABLE_COLLECTSTATIC=1

## Make and run migrations
* python3.6 manage.py check
* python manage.py makemigrations photos
* python3.6 manage.py sqlmigrate photos 0001
* python3.6 manage.py migrate

## Run the app
* Running the application
    ```python3.8 manage.py runserver```
* Testing the application
    ```python3.8 manage.py test```

## Technologies Used

* python3.8
* Django
* Postgresql
* Bootstrap
* HTML / CSS

## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [brianaodhiambo754@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2022 **Brianna **
