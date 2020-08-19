# Project Title.
 * Awards.

* Awards is a django application that allows users to post their projects for others to rate and review

## Requirements
##### These are the requirements you need to get the project running locally on your machine:
  * Text Editor
  * Install python
  * Install and activate virtual
  * Setup Database
  * Install Django
  
## Installation Process
 * Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
 * Install your preferred version of python
 * ```sudo apt-get install python3.6```
 * ```python --version``` to confirm that python has been installed.
## Open the command-line and run the following command to open a directory:
  * ```cd your preferred directory``` => ```cd instagram```
## Git clone the project on your current directory by:
  * ```git clone https://github.com/tonyguthiga/reviews.git```.
## Move to your project directory:
 * ```cd reviews```.
## Open the project on your terminal:
  * ```atom . or code .``` , according to the type of your text editor.
## Install virtual environment using python:
  * ```python3.6 -m venv virtual```, check your project to confirm you have a folder called virtual,
  * then activate it by running ```source virtual/bin/activate```
## To install the packages in the ```requirements.txt file```,
  * ```pip install -r requirements.txt```  That will install all packages including Django.
## To open python shell:
  * ```python3.6``` ,
  * ```import django```
  * And lastly ```django.get_version()``` to see and confirm the version of django installed.
  * You can then ```ctrl z``` to get out of the shell,
## After ensuring you have all the above
  * ```python3 manage.py runserver``` to run the project.
  * Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.


## For more information read the following django and python documentation:
  * [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/intro/install/)
  * [PythonDocumentation](https://www.python.org/doc/)

## User Stories
* As a user, I would like to view posted projects and their details.
* As a user, I would like to post a project to be rated/reviewed.
* As a user, I would like to rate/review other users' projects.
* As a user, I would like to search for projects.
* As a user, I would like to view projects overall score.
* As a user, I would like to view my profile page.


## Behavior Driven Development
* Given that a user sign-up with the correct details, and use those details to login successfully, then they should be able to access the application and it's features.
* Given that the user has uploaded a photo, then the application should display the photo uploaded.
* Given that a user has logged in, created a profile and posted a picture, then they  should be able 
  to view their profile and all the photos they've posted.
* Given that a user has an account, then they should be able to rate and review other users projects.



## Technologies Used
* Python
* Django
* PostgreSQL
* HTML5
* Font Awesome
* Bootstrap 4


## License
MIT Copyright (c) 2020 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author:

Antony Guthiga

## Contact Detail:

tonyguthiga93@gmail.com