# README
### 2023.08.20

follow the Corey Django youtube tutorial: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p 

## Table of contents
* [General info](#general-info)
* [Main Technologies](#main-technologies)
* [Pre-requisites](#pre-requisites)
* [Setup](#setup)
* [Project Structure](#project-structure)
* [Url Paths](#url-paths)
* [Features](#features)

## General info
This project is simple blog website with user authentication created with Django Web Framework.
	
## Main Technologies
Project is created with:
* Django version 4.2.6

## Pre-requisites
- Install [Python](https://www.python.org) version 3.11.5

## Setup
To run this project, install dependencies and run the project with:
```
$ pip install -r requirements.txt
$ python3 manage.py migrate (apply migrations to set up the database schema)
$ python3 manage.py runserver
```

## Project Structure
The folder structure of this app is explained below:

| Name            | Description                                                                                               |
| ----------------| -------------------------------------------------------------------|
| **django_proj/** | Main Django app folder containing crucial settings and URL configurations for the entire project.        |
| **blog/**        | Django app handling application-specific routes and ensuring modularity for route management.              |
| **users/**       | Django app providing user-related functionalities, managing user authentication, profiles, and settings.  |
| **manage.py**    | Django's command-line utility, facilitating various project management tasks efficiently.                 |


## URL Paths
The application running on `localhost:8000`, url paths as below:

| Route          | Description                                            |
|-----------------|--------------------------------------------------------|
| `/blog/`        | Landing page of the blog, showcasing recent articles.  |
| `/login/`       | Presents a login form for users to access the system.   |
| `/register/`    | Provides a registration form for new user sign-ups.      |
| `/about/`       | Information page about the blog.    |

## Features
- Pagination
- Blog can filter by author
- Register and authentication system
- Profile Page after Login
