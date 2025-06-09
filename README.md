# Mobapps Project - Fixit Forward

## Overview
Fixit Forward is a web application designed to connect users who need items repaired with skilled repairers, fostering a culture of repair and waste reduction. This project is built using Django for the backend and standard HTML, CSS, and JavaScript for the frontend components, integrated via Django templates.

## Prerequisites
Before you begin, ensure you have the following installed:
* Python 3.8 or higher
* Pip (Python package installer)
* PostgreSQL (Database server)
* Git (for version control)
* Recommended Operating System to run: Linux 

## Getting Started

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

### 5. PostgreSQL Setup
- Start the postgres service
```bash
sudo systemctl start postgresql
```
or if that does not work, try
```bash
sudo service start postgresql
```

- Check if it is running
```bash
sudo systemctl status postgresql
```
- Set up database and user (Mandatory)
```bash
sudo -u postgres psql -c "CREATE DATABASE fixit;"
sudo -u postgres psql -c "CREATE USER vidky WITH PASSWORD 'vickyganteng&&';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE fixit TO vidky;"
```

### 6. Run Database Migrations
```bash
python3 manage.py makemigrations fixit_frw
python3 manage.py migrate
```

### 7. Create a Superuser (Admin account)
```bash
python3 manage.py createsuperuser
```

### 8. Run the server
```bash
python3 manage.py runserver  
```

### 9. Access the server
Access this in your local browser
```bash
localhost:8000
```

## Authors
- [Teuku Achmad Ra'di Syah](https://github.com/yarin-sys) (23/511627/PA/21833)
- [I Putu Herjuna Manasye Suarthana](https://github.com/HermanCS-07) (23/511460/PA/21801)
- [Ivan Adito Arba Putra](https://github.com/ivanadito-ap) (23/511562/PA/21821)
- [Muhammad Rafif Akio Sarwadi](https://github.com/) (23/511466/PA/21802)



