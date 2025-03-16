# SQLAlchemy Demo with FastAPI

A demonstration project showcasing the power of SQLAlchemy with FastAPI, using SQLite as the database.

## Features

- SQLAlchemy ORM implementation
- FastAPI REST endpoints
- HTML templates with Jinja2
- User and Address models with one-to-many relationship
- Web interface for viewing data

## Prerequisites

- Python 3.7+- Virtual environment (recommended)

## Installation

1. Clone the repository:

////////
TODO:

````bashgit clone <your-repository-url>
cd <project-directory>```
2. Create and activate a virtual environment:
```bashpython -m venv sqlalchemy
sqlalchemy\Scripts\activate  # Windowssource sqlalchemy/bin/activate  # Linux/Mac
````

3. Install dependencies:`bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart`

## Project Structure

````
├── main.py           # FastAPI application and routes├── database.py       # SQLAlchemy models and database configuration
├── templates/        # HTML templates│   ├── index.html
│   ├── users.html│   └── addresses.html
└── example.db       # SQLite database file```
## Running the Application
1. Start the server:
```bashuvicorn main:app --reload
````

2. Open your browser and navigate to:- Home page: http://localhost:8000

- Users list: http://localhost:8000/users- Addresses list: http://localhost:8000/addresses

## API Endpoints

### Users

- `GET /users/` - List all users- `GET /users/{user_id}` - Get specific user
- `POST /users/` - Create new user

### Addresses- `GET /addresses/` - List all addresses

- `POST /users/{user_id}/addresses/` - Create new address for user

## Data Models

### User- id: Integer (Primary Key)

- name: String- fullname: String
- nickname: String- addresses: Relationship to Address

### Address

- id: Integer (Primary Key)- email_address: String
- user_id: Integer (Foreign Key)- user: Relationship to User

## License

[Your chosen license]

# SQLAlchemy Demo with FastAPI

A demonstration project showcasing the power of SQLAlchemy with FastAPI, using SQLite as the database.

## Features

- SQLAlchemy ORM implementation
- FastAPI REST endpoints
- HTML templates with Jinja2
- User and Address models with one-to-many relationship
- Web interface for viewing data

## Prerequisites

- Python 3.7+
- Virtual environment (recommended)

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:

```bash
python -m venv sqlalchemy
sqlalchemy\Scripts\activate  # Windows
source sqlalchemy/bin/activate  # Linux/Mac
```

3. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

## Project Structure

```
├── main.py           # FastAPI application and routes
├── database.py       # SQLAlchemy models and database configuration
├── templates/        # HTML templates
│   ├── index.html
│   ├── users.html
│   └── addresses.html
└── example.db       # SQLite database file
```

## Running the Application

1. Start the server:

```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to:

- Home page: http://localhost:8000
- Users list: http://localhost:8000/users
- Addresses list: http://localhost:8000/addresses

## API Endpoints

### Users

- `GET /users/` - List all users
- `GET /users/{user_id}` - Get specific user
- `POST /users/` - Create new user

### Addresses

- `GET /addresses/` - List all addresses
- `POST /users/{user_id}/addresses/` - Create new address for user

## Data Models

### User

- id: Integer (Primary Key)
- name: String
- fullname: String
- nickname: String
- addresses: Relationship to Address

### Address

- id: Integer (Primary Key)
- email_address: String
- user_id: Integer (Foreign Key)
- user: Relationship to User

## License

[Your chosen license]
