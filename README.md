# Mobapps Project - Fixit Forward

## Overview
Fixit Forward is a web application designed to connect users who need items repaired with skilled repairers, fostering a culture of repair and waste reduction. This project is built using Django for the backend and standard HTML, CSS, and JavaScript for the frontend components, integrated via Django templates.

## Prerequisites
Before you begin, ensure you have the following installed:
* Python 3.8 or higher
* Pip (Python package installer)
* PostgreSQL (Database server)
* Git (for version control)

## Setup Instructions

Follow these steps to get the Fixit Forward application running locally:

### 1. Clone the Repository
Get the project code onto your local machine using the provided Git repository link:
```bash
git clone (https://github.com/yarin-sys/Mobapps.git)
cd Mobapps
```

### 2. Navigate to the Django Project Directory
```bash
cd fixit
```

### 3. Create and Activate a Python Virtual Environment
```bash
python3 -m venv env
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Run Database Migrations
```bash
python3 manage.py makemigrations fixit_frw
python3 manage.py migrate
```

### 6. Create a Superuser (Admin account)
```bash
python3 manage.py createsuperuser
```

### 7. Run the server
```bash
python3 manage.py createsuperuser
```

## Project Structure and Frontend Integration
The main Django application logic is in the fixit_frw app directory within fixit/.
Templates: HTML files are primarily located in fixit/fixit_frw/templates/. Pages like the landing page, maps page, and confirmation page have been structured to be served as Django templates.

    Example: fixit/fixit_frw/templates/landing/index.html

Static Files: CSS, JavaScript, and images are located in fixit/fixit_frw/static/. Django's development server will automatically serve these when DEBUG = True.

    App-specific CSS/JS: fixit/fixit_frw/static/css/, fixit/fixit_frw/static/js/, and subfolders like fixit/fixit_frw/static/landing/ for landing page specific CSS/JS.
    Shared image assets: fixit/fixit_frw/static/assets/img/
    Other images (e.g., for menupage.html): fixit/fixit_frw/static/Images/

Static File Usage in Templates: Always use {% load static %} at the top of your templates and then the {% static %} template tag to refer to static files. Example: <link rel="stylesheet" href="{% static 'css/main.css' %}"> or <img src="{% static 'assets/img/logo.png' %}">.
URL Usage in Templates: Always use the {% url 'view_name' %} template tag for internal links, where 'view_name' is the name parameter given to a path() in your urls.py.



