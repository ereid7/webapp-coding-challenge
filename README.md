# Web Application Coding Challenge
A simple web application which displays a list of products + their ingredients. The application allows users to create new products, and enter the product ingredients. Built using Python, Flask, PostgreSQL, and Angular.

# Development Setup
### Install Machine Dependencies
- PostgreSQL v14
- Python 3.0
- npm

### Install Python Dependencies with pip
- flask
- flask_restful
- flask-cors
- psycopg2

### Database Setup
- Ensure PostgreSQL is installed
- Navigate to `backend/utilities`
- Update `postgresconfig.py` with the correct `postgres` user password
- Run `python initialize_database.py`

### Serve Backend
- Navigate to `backend/src`
- Run `python api.py`

### Serve Frontend
- Navigate to `frontend`
- Run `npm install` to install dependencies
- Run `ng serve` to serve frontend
- Navigate to `http://localhost:4200/` in a browser

# Unit Tests
### API Unit Tests
- Navigate to `backend/src`
- Run `python api_test.py`

### Frontend Service Unit Tests
- Navigate to `frontend`
- run `ng test` 