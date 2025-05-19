# Domain Driven Design using FastAPI, Kafka and PostgreSQL

This is an example application using Domain Driven Design using FastAPI, Kafka and PostgreSQL

## Dependencies Management

This project uses [Poetry](https://python-poetry.org/) for dependency management.

### Installing Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Installing Dependencies

```bash
poetry install
```

### Adding New Dependencies

```bash
poetry add package-name
```

### Adding Development Dependencies

```bash
poetry add --group dev package-name
```

### Updating the Virtual Environment (.venv)

When you need to update your virtual environment after changes to dependencies:

```bash
# Update all dependencies to their latest versions according to pyproject.toml
````bash
poetry update
````
# Update a specific package
````bash
poetry update package-name
````

# Recreate the virtual environment from scratch
````bash
poetry env remove --all
poetry env use python3.12
````

Make the .venv a local environment
````bash
poetry config virtualenvs.in-project true
poetry install
````

If installing for production:
````bash
poetry install --no-dev
````

# View information about the current environment
````bash
poetry env info
````

# List all Poetry-managed virtual environments
````bash
poetry env list
````

By default, Poetry creates virtual environments in a centralized location. To create the virtual environment in the project directory:

```bash
# Configure Poetry to create .venv in the project directory
poetry config virtualenvs.in-project true

# Then install dependencies
poetry install
```

## Development with Docker

This project includes Docker configuration for development.

### Starting the Development Environment

When debugging locally and in a terminal

```bash
docker compose --profile debug up
```

### Docker Desktop Configuration

In order to get docker desktop's compose to work in Pycharm, you have to go into:

Settings >> Build, Execution, Deployment >> Tools

####
When using docker desktop on Linux or Mac, you have to change the docker context when using the command line
e.g. docker context use <<desktop context>>

On my Fedora machine
```bash
docker context use desktop-linux
```

## API Endpoints

- `POST /messages/`: Create a new message
- `GET /messages/`: Get all messages
- `GET /health/`: Health check endpoint
