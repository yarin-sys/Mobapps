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



