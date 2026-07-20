# Taika Seafood Recruitment System

## Project Overview

Taika Seafood Recruitment System is a web-based recruitment management application developed using Django. The system allows candidates to browse available jobs, submit applications, upload CVs, and track interview schedules. HR staff can manage job postings, review applications, update application status, and schedule interviews.

This project was developed as part of an internship and demonstrates a complete recruitment workflow.



## Technology Stack

* Backend: Django (Python)
* Database: SQLite3
* Frontend:

  * HTML
  * CSS
  * Bootstrap 5
  * JavaScript
* Template Engine: Django Templates



## Main Features

### Candidate

* Register and Login
* View available jobs
* Search jobs by keyword and location
* Apply for jobs
* Upload and update CV
* View application status
* View interview schedule
* Manage personal profile

### HR

* Login
* HR Dashboard
* Create, edit, close, reopen, and delete jobs
* View applicants for each job
* Review submitted CVs
* Update application status
* Schedule interviews
* Manage recruitment process



## Project Structure

JobRecruitmentSystem/
│
├── recruitment_system/
├── users/
├── jobs/
├── applications/
├── interviews/
├── templates/
├── static/
├── media/
└── manage.py



## User Roles

### Candidate

* Browse jobs
* Submit applications
* Update CV
* Track interview status

### HR

* Manage job postings
* Review applications
* Schedule interviews
* Monitor recruitment dashboard


## Current Status

Completed:

* User Authentication
* Job Management
* Application Management
* Interview Scheduling
* Profile Management
* Responsive UI Integration
* Shared Base Template
* Static Assets Organization

Currently Working On:

* Deployment (Render)
* Production Configuration



## How to Run

Create a virtual environment:

bash
python -m venv venv


Activate the virtual environment:

bash
venv\Scripts\activate


Install dependencies:

bash
pip install -r requirements.txt


Run database migrations:

bash
python manage.py migrate


Start the development server:

bash
python manage.py runserver


Open:


http://127.0.0.1:8000



## Author

Nguyễn Trần Hoàng Minh

Ho Chi Minh City University of Technology (HCMUT)

Computer Science Student

Internship Project – Taika Seafood Recruitment System

# Development Notes

# Django Admin Accounts
********
admin
admin@gmail.com
admin123
********


hr1 / 12345678   (role = hr)
cand1 / 12345678 (role = candidate)
# Commands

python manage.py runserver

python manage.py createsuperuser