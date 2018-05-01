# psiholeks-web

Web interface for the psycholinguistic database of the Croatian language.

## Development notes

Code is based on this series of tutorials:

[Build a CRUD Web App With Python and Flask - Part One](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)
[Build a CRUD Web App With Python and Flask - Part Two](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two)
[Build a CRUD Web App With Python and Flask - Part Three](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three)

Create the database table with utf-8 encoding:
```
CREATE DATABASE psiholeks_hr CHARACTER SET utf8 COLLATE utf8_general_ci;
```

When changing the table model, run:
```
flask db migrate
flask db upgrade
```

Running with flask development server:

```
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```

## Deployment notes

The following environment variables must be set on the deployment server:
```
export FLASK_CONFIG=production
export FLASK_APP=run.py
export SQLALCHEMY_DATABASE_URI='mysql://<username>:<password>@<host-address>/<database-name>'

## Licensing

Data ...

Code ...
