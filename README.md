## 📋 **About the project**

A basic API developed in the Python using Django REST Framework during the course offered by Alura Cursos Online.


## 🛸 **Technologies**
The application was developed with the following technologies:

* 🐍 [Python](https://www.python.org)
* ⚙️ [Django](https://docs.djangoproject.com/en/4.0/)
* ⚙️ [Django REST Framework](https://www.django-rest-framework.org)
* 🐳 [Docker](https://www.docker.com)
 
## 📥 **How to install?**

To install and testing this API, make sure you have a Docker and Docker-Compose installed. Then:


```bash
# Clone the repository
$ git clone git@bitbucket.org:aeduaardo/school-rest-api.git

# Enter the folder
$ cd school-rest-api

# Start project
$ docker-compose up --build -d

# Push migrations to the database
$ docker exec -it api /bin/bash
$ python manage.py migrate

# Create your super user
$ python manage.py createsuperuser
```
<br>
Now you can use the API through your [Local Server](http:127.0.0.1:8000).

<br><br>
Contact me:

* 📧 E-mail: aeduardo.dev@gmail.com
* 🌐 Linkedin: www.linkedin.com/in/aeduaardo  

