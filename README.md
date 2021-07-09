
# Diabetes Intellect


## Run Locally

Clone the project
```bash
git clone https://github.com/aayush-jaiswal/diabetes-intellect-backend.git
```

Go to the project directory
```bash
cd diabetes-intellect-backend
```

Create virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Make migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Start the server
```bash
python3 manage.py runserver
```