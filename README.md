# REST API With Flask & SQL Alchemy

> ratings API using Python Flask, SQL Alchemy and Marshmallow

## Quick Start Using Pipenv

``` bash
# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
```

## Endpoints

* GET     /<classname>
* GET     /<classname>/:id
* POST    /<classname>
* PUT     /<classname>/:id
* DELETE  /<classname>/:id