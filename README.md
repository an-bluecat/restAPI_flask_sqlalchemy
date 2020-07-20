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

Base URL: https://restapipostgre.herokuapp.com/

* Get an individule class information:
  GET     #/[classname]
* Get a class's rating average:
  GET     #/[classname]/average
* Post a rating JSON to a class
  POST    #/[classname]
<!-- * PUT     /<classname>/:id -->
* Delete a class rating
  DELETE  #/[classname]/[rating id]

for example, if you want to get ECE110's information:
axios.get(https://restapipostgre.herokuapp.com/ECE110)
if you want to get ECE110's average:
axios.get(https://restapipostgre.herokuapp.com/ECE110/average)


## example JSON
[
  {
    "comment": "bad", 
    "id": 3, 
    "israting": false, 
    "likes": 0, 
    "rate": 0, 
    "time": "2020-07-25-10-3", 
    "user": "unknown"
  }, 
  {
    "comment": "good", 
    "id": 7, 
    "israting": true, 
    "likes": 0, 
    "rate": 2, 
    "time": "not set", 
    "user": "unknown"
  }
]
