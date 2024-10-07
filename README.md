 # SIM Card Activation Service

This project implements a simple API for activating, deactivating, and retrieving details of SIM cards for a telecom company. It uses **Flask** for the API and **SQLite** for the database.

## Features

- Activate a SIM card.
- Deactivate a SIM card.
- Retrieve details of a SIM card.

## Project Structure

sim_card_activation/ │ ├── app.py # Main Flask application ├── init_db.py # Script to initialize the database ├── sim_db.sqlite # SQLite database (generated after running init_db.py) ├── requirements.txt # Python dependencies └── README.md # This file

markdown
Copy code

## Requirements

- Python 3.x
- Flask

## Setup Instructions

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
Initialize the database:

Run the init_db.py script to create the SQLite database with sample SIM card data.

bash
Copy code
python init_db.py
Run the Flask application:

bash
Copy code
python app.py
API Endpoints:

Activate SIM Card:

POST /activate
Body: { "sim_number": "123456789" }
Deactivate SIM Card:

POST /deactivate
Body: { "sim_number": "123456789" }
Get SIM Details:

GET /sim-details/{sim_number}`x`
