# Auth Service with JWT + Permissions

FastAPI-based authentication microservice that issues JWTs with configurable roles and permissions.

## Features

- User registration and authentication
- JWT access and refresh tokens
- Role-based permissions system
- PostgreSQL database
- Configurable permissions per project
- Docker support for easy deployment

## Prerequisites

- Python 3.14+
- Poetry (for dependency management)
- Docker and Docker Compose (for containerized setup)
- PostgreSQL (for local development without Docker)

## Installation

### 1. Clone and Configure Environment (testing only)

```bash
# Clone the repository
git clone <repository-url>
cd auth

# Create environment configuration
cp .env.example .env
```

Edit `.env` and set your values:

```bash
# Generate a secure SECRET_KEY
openssl rand -hex 32

# Update .env with generated key and database credentials
SECRET_KEY=<generated-key>
POSTGRES_USER=authuser
POSTGRES_PASSWORD=<secure-password>
POSTGRES_DB=authdb
```

### 2. Configure Permissions

```bash
# Copy the permissions template
cp permissions.yaml.example permissions.yaml
```

Edit `permissions.yaml` to define your project-specific permissions:

```yaml
default_permissions:
  - admin
  - user
  - moderator
  # Add your custom permissions here

default_user_permissions:
  - user  # Permissions assigned to new users

permission_descriptions:
  admin: "Full system access with all privileges"
  user: "Standard user access"
  moderator: "Moderate content and manage users"
```

### 3. Run migrations

Run migrations with command

`python manage.py migrate`

From dockerized test environment you can run 

`docker compose exec auth python manage.py migrate`

## License

This code is distributed under MIT License.
