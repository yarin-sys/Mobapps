# Mobapps Project

# Instructions
## cd to to fixit directory first
```bash
cd fixit
```

## create python environtment
```bash
pyhton3 -m venv env
```

## activate env (mandatory)!!
```bash
source env/bin/activate
```

## install dependency
```bash
pip install -r requirements.py (make sure you at right directory)
```

## database migration (make sure manage.py in the current directory) 
```bash
python3 manage.py makemigrations fixit_frw
python3 manage.py migrate
```

## create super user
```bash
python3 manage.py
```

## run the server
```bash
python3 manage.py
```

