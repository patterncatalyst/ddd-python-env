# Domain Driven Design using FastAPI, Kafka and PostgreSQL

This is an example application using Domain Driven Design using FastAPI, Kafka and PostgreSQL

## Dependencies Management

This project uses [Poetry](https://python-poetry.org/) for dependency management.

### Installing and using Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or

````bash
pip install -U poetry
````

#### If you did not create the project with poetry and do not have a pyproject.toml file

````bash
poetry init
````

#### Installing Dependencies

```bash
poetry install
```

#### Adding New Dependencies

```bash
poetry add package-name
```

#### Adding Development Dependencies

```bash
poetry add --group dev package-name
```

#### Updating the Virtual Environment (.venv)

When you need to update your virtual environment after changes to dependencies:

#### Update all dependencies to their latest versions according to pyproject.toml
````bash
poetry update
````
#### Update a specific package
````bash
poetry update package-name
````

#### Recreate the virtual environment from scratch
````bash
poetry env remove --all
poetry env use python3.12
````
#### Configure Poetry to create .venv in the project directory
By default, Poetry creates virtual environments in a centralized location. To create the virtual environment in the project directory:

Make the .venv a local environment
````bash
poetry config virtualenvs.in-project true
poetry install
````

If installing for production:
````bash
poetry install --no-dev
````

#### View information about the current environment
````bash
poetry env info
````

#### List all Poetry-managed virtual environments
````bash
poetry env list
````

## Development with Docker

This project includes Docker configuration for development.

### Starting the Development Environment

When debugging locally and in a terminal

```bash
docker compose --profile debug up -d
```
To bring docker compose down

````bash
docker compose --profile debug down
````

If you want to remove the volume(s) so you start clean next time

````bash
docker compose --profile debug down -v
````

### Docker Desktop Configuration

In order to get docker desktop's compose to work in Pycharm, you have to go into:

Settings >> Build, Execution, Deployment >> Tools

####
When using docker desktop on Linux or Mac, you may have to change the docker context when using 
the command line
e.g. docker context use <<desktop context>>

This will change the docker socket.
To list the sockets:

````bash
docker context list
````

Then select the context you wish to use.  On Linux, docker desktop may have a different context.

On my Fedora machine
```bash
docker context use desktop-linux
```

## API Endpoints

- `POST /messages/`: Create a new message
- `GET /messages/`: Get all messages
- `GET /health/`: Health check endpoint
