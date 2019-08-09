# python-flask-getting-started
This code base will have getting started with structure for Python Flask application for API development, along with database connections

## Prerequisite
Make sure you have installed python :) 
To check python version,  
> python -V  

Make sure you have installed 
> python-pip 

## lets get started with 'Hello World'!

* Checkout code


       git clone https://github.com/srikanthjeeva/python-flask-getting-started.git    
       cd python-flask-getting-started   

* Install dependencies, (use sudo if required)    

       pip install -r requirements.txt 
           
       or 
          
       pip install Flask Flask-SQLAlchemy Flask-Migrate flask-marshmallow marshmallow-sqlalchemy pymysql

* start server    

       python server.py  

* In browser go to,

       http://localhost:5000 
            
        or 
                    
       http://localhost:5000/hello  

        or for UI 

       http://localhost:5000/ui/hello 

## Docker

```
docker ps
docker images
docker build -t pygs:1.0.0 . 
docker run -d pygs:1.0.0
```
