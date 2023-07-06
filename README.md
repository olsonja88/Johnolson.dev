# Johnolson.dev
My personal portfolio website.
https://www.johnolson.dev

## How to run Locally
1. You'll need Python 3.11.3 (that's the version this project was made on).
2. Clone this repository into an empty directory.
3. Open a command prompt and cd into the directory.
4. Run "python -m venv venv" to create a virtual environment.
5. cd into venv/scripts and run "activate".
6. Refer to requirements.txt to see all current dependencies.  Pip install these inside of scripts.
7. cd back out (../..) to the base dir.
8. Go into settings.py and set "Debug=True".
9. At this point you'll need either setup your own local pg or sqlite db and add it to DATABASES in settings.py
10. From the command line run "python manage.py runserver" to run locally.
11. Access the local app at "localhost:8000".

## About this project
* Created using the Django web framework, and hosted on Vercel (both deployment and PostgreSQL db).
* This project used Python, HTML, CSS, and JS languages.

## Current State 7/6/23
Working on moving from the entire project being Django, to only having only a Django backend with React frontend.
