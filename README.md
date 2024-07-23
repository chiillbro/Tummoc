# Tummoc Assignment

This repository contains the solutions for the Tummoc assignment, divided into three main sections: Logical problems, FastAPI implementations and SQL queries. Each section is organized in its respective folder.

## Folders and Files

### Logical

This section contains Python scripts for solving logical problems.

- **Credit_Card_Validator**
  - `main.py`: Main Python script for the credit card validator.
- **Voting_And_Result**
  - `main.py`: Python script to vote and get the result.

### FastAPI

This section contains a FastAPI implementation for three different tasks.

- `main.py`: Main FastAPI application file.
- `models.py`: Models for the FastAPI application.
- `requirements.txt`: List of Python dependencies.

## Running the FastAPI Implementations

To run the FastAPI implementations, you need to create a virtual environment and install the required dependencies. You can do this by running the following command:

```bash
python -m venv venv
```

This will create a virtual environment named `venv` in the current directory. Activate the virtual environment by running the following command:

```bash
source venv/bin/activate
```

Once the virtual environment is activated, install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

Once the dependencies are installed, you can run the FastAPI implementations by executing the following command:

```bash
uvicorn main:app --reload
```

After running the command, you can access the FastAPI implementations by visiting `http://127.0.0.1:8000/` in your web browser.

For checking the API's, you can use a tool like [Postman](https://www.postman.com/).

### SQL

This section contains SQL queries for different tasks.

- **station_slot**
  - `query.sql`: SQL query to get the station slot.
- **route_by_stop_id**
  - `query.sql`: SQL query to get the route by stop ID.
- **result_by_station_id_and_slot**
  - `query.sql`: SQL query to get the result by station ID and slot.

## Usage

Each SQL file contains a query for the specific task mentioned. You can execute these queries in your SQL environment to get the desired results.
