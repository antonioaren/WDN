# Backend API
version python 3.11
You will use poetry to manage the python dependencies and npm to manage the javascript dependencies.

```bash
cd backend
poetry install
```

Make sure you install the right version of python.

```bash
# Make sure you still inside the backend folder
poetry env info
```

## Environment variables
Have a look to env.example and create a .env file with the right values.

## Database
In this example I will use Posgresql, but you can use any database you want. 
Create a database to be able to manage all website.

You will need to create a database and then copy the url string inside the .env file, like this:

```
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```

Have a look inside [env.example](env.example) to see all the variables you need to set.

```bash
poetry run python manage.py migrate
```


To run this:

```bash
poetry run python manage.py runserver 8000
```