# FastAPI Kafka PostgreSQL Application

This is a FastAPI application that uses Kafka for message processing and PostgreSQL for data storage.

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

## Development with Docker

This project includes Docker configuration for development.

### Starting the Development Environment

```bash
docker-compose up
```

### Docker Desktop Configuration

In order to get docker desktop's compose to work you have to go into:

Settings >> Build, Execution, Deployment >> Tools

## API Endpoints

- `POST /messages/`: Create a new message
- `GET /messages/`: Get all messages
- `GET /health/`: Health check endpoint
