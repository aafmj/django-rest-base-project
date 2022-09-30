# Base Project

## Quick Start :

#### **1. git clone (git address)** (terminal)

#### **2. pip install -r requirements.txt** (terminal, with active virtualenv)

#### **3. python manage.py makemigrations** (terminal)

#### **4. python manage.py migrate** (terminal)

#### **5. create an .env file in your project root directory, copy .env.example file into that and modify its values based on your runtime requirements.**

#### **6. python manage.py runserver (optional: python manage.py runserver 127.0.0.1:8008)** (terminal)


## Done!

-----------------

### if there is other db (mysql or postgres)

    CREATE USER 'sampleuser'@'%' IDENTIFIED BY 'Password_1234';
    
    GRANT ALL PRIVILEGES ON *.* TO 'sampleuser'@'%';
    
    CREATE DATABASE sample_db DEFAULT CHARACTER SET utf8mb4  DEFAULT COLLATE utf8mb4_general_ci;


- **Admin panel**:
    - http://localhost:8000/admin/ 
- **API Documentation**: (pick one)
    - http://localhost:8000/swagger/
    - http://localhost:8000/redoc/
    - http://localhost:8000/swagger.json
    - http://localhost:8000/swagger.yaml
