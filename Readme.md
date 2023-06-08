# Meta Back-End Developer Capstone

![Coursera](https://img.shields.io/badge/Coursera-0747a6?style=flat&logo=coursera&logoColor=white)
![Meta](https://img.shields.io/badge/Meta-0668E1?style=flat&logo=meta&logoColor=white)
![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)

Building RESTful APIs using [Django Rest Framework](https://www.django-rest-framework.org/) connected to a [MySQL](https://dev.mysql.com/downloads/) as part of the [Meta Back-End Developer Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer) teached by [Meta](https://www.facebook.com/business/learn/back-end-back-end-developer-certificate-coursera).

<p align="center">
    <a href="https://www.credly.com/org/facebook-blueprint/badge/meta-back-end-developer-certificate">
        <img src="images/meta-backend-cert.png" width="30%" height="30%" />
    </a>
</p>

## Steps to run the app

### 1. Install `pipenv`

```bash
pip install pipenv
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Make migrations

```bash
py manage.py makemigrations
```

### 4. Migrate

```bash
py manage.py migrate
```

### 5. Run the app

```bash
py manage.py runserver
```
