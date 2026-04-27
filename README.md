# FastAPI Demo

A learning project to study the FastAPI web stack.

## Technologies
- Python 3.9
  - FastAPI
  - pydantic
  - SQLAlchemy
  - uvicorn
- PostgreSQL

# Setting up and running

### Environment
Create a `.env` file and add the following variables with your database credentials:
```
POSTGRES_USER=<your database username>
POSTGRES_PASSWORD=<your database password>
POSTGRES_DB=<your database name>
```

### Database
We will use a PostgreSQL database as a docker container. It will pick up the environment variables from the `.env` file.
```shell
docker-compose up -d
```

### Application
If you have not activated your venv, then execute the following:
```shell
source .venv/bin/activate
```

Next, run the following command to install the dependencies:
```shell
pip install -r requirements.txt
```

Application uses uvicorn as a web-server. To run the application, execute the following command:
```shell
uvicorn main:app --reload
```

You could now access the application at `http://localhost:8000/`. You can use Postman to test the API or any other tool of your choice. As an alternative, you can use openapi-ui to test the API as it is built-in: `http://127.0.0.1:8000/docs#/`