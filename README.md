# Django Finance App

This project is a Django-based backend system that fetches financial data, stores it in a PostgreSQL database, performs basic backtesting on historical stock data, generates predictions using a pre-trained model, and outputs reports in both JSON and PDF formats. The application is deployed on Heroku and integrates with Alpha Vantage API for financial data.

### Deploy URL: [Heroku Deployment](https://finance-django-93f5ce60f767.herokuapp.com/)

### Key Endpoints:
- **Fetch stock**: [Fetch AAPL stock](https://finance-django-93f5ce60f767.herokuapp.com/stocks/fetch-stocks/?symbol=AAPL)
- **Backtest**: [Backtest AAPL](https://finance-django-93f5ce60f767.herokuapp.com/stocks/backtest/?symbol=AAPL&initial_investment=10000)
- **Predict**: [Predict AAPL for 30 days](https://finance-django-93f5ce60f767.herokuapp.com/stocks/predict-stock/?symbol=AAPL&days=30)
- **Backtest Report (JSON)**: [JSON Backtest Report](https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=backtest&symbol=AAPL&initial_investment=10000&format=json)
- **Backtest Report (PDF)**: [PDF Backtest Report](https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=backtest&symbol=AAPL&initial_investment=10000&format=pdf)
- **Prediction Report (JSON)**: [JSON Prediction Report](https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=prediction&symbol=AAPL&days=30&format=json)
- **Prediction Report (PDF)**: [PDF Prediction Report](https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=prediction&symbol=AAPL&days=30&format=pdf)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [API Keys](#api-keys)
- [Setup and Installation](#setup-and-installation)
- [Running Migrations](#running-migrations)
- [Fetching Stock Data](#fetching-stock-data)
- [Running the Backtest](#running-the-backtest)
- [Generating Predictions](#generating-predictions)
- [Report Generation](#report-generation)
- [Deploying to Heroku](#deploying-to-heroku)
- [CI/CD Pipeline](#ci/cd-pipeline)
- [AWS Deployment](#aws-deployment-initial-setup)

## Features

- Fetches historical stock prices using Alpha Vantage API.
- Stores the data in a PostgreSQL database.
- Implements a basic moving average crossover strategy for backtesting.
- Predicts future stock prices using a pre-trained machine learning model.
- Generates performance reports in JSON and PDF formats.

## Requirements

- Python 3.9+
- PostgreSQL
- Django 4.2+
- Alpha Vantage API key
- Heroku CLI (if deploying to Heroku)

## API Keys

You will need to create an Alpha Vantage account and obtain an API key to fetch stock data.

- Sign up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
- Add your API key to the `.env` file under `ALPHA_VANTAGE_API_KEY`.

### Example `.env` file:

```bash
ALPHA_VANTAGE_API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
DEBUG=True
SECRET_KEY=your_secret_key_here

```
 ### Setup and Installation

Clone the repository

```bash

git clone https://github.com/pibbiraj1016/django-finance-app.git
cd django-finance-app
```
Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install dependencies

``` bash
pip install -r requirements.txt
```

### Configure environment variables

Copy the .env.example file to .env and fill in your details:

```bash

cp .env.example .env
``` 
Update the .env file with your API keys, database URL, and other environment variables.

### Running Migrations

After setting up your environment, you need to run database migrations:

```bash
python manage.py migrate
```
This will apply all the necessary migrations to create the database schema.

### Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```
You should be able to access the application at http://127.0.0.1:8000/.

### Fetching Stock Data
To fetch stock data for a specific symbol (e.g., AAPL), use the following URL:

```bash
GET /stocks/fetch-stocks/?symbol=AAPL
```
### Response Example:

```bash
{
  "status": "success",
  "message": "Data for AAPL fetched and saved."
}
```
### Running the Backtest
You can backtest a stock based on a moving average strategy with this API:

```bash
=
GET /stocks/backtest/?symbol=AAPL&initial_investment=10000
```
### Response Example:

```bash
{
  "status": "success",
  "result": {
    "initial_investment": 10000,
    "final_portfolio_value": 12000,
    "total_return": 20.0,
    "max_drawdown": 5.0,
    "trades": [
      { "date": "2023-01-10", "type": "buy", "price": 105.0, "shares": 50 },
      { "date": "2023-05-15", "type": "sell", "price": 120.0, "shares": 50 }
    ]
  }
}
```
### Generating Predictions

Predict stock prices for the next 30 days:

```bash

GET /stocks/predict-stock/?symbol=AAPL&days=30
```
### Response Example:

```bash

{
  "status": "success",
  "predictions": [
    { "date": "2024-01-01", "predicted_price": 150.23 },
    { "date": "2024-01-02", "predicted_price": 151.56 }
  ]
}
```
### Report Generation
You can generate reports in both JSON and PDF formats.

### Backtest Report (PDF):
```bash

GET /stocks/report/?type=backtest&symbol=AAPL&initial_investment=10000&format=pdf
```
### Prediction Report (PDF):
```bash
GET /stocks/report/?type=prediction&symbol=AAPL&days=30&format=pdf
```
### Testing

The project contains several test cases to validate the functionality of backtesting and prediction features.

### To run the tests:

```bash

python3 manage.py test finance.stocks.tests
```
### Deploying to Heroku

Set up Heroku CLI:

Install Heroku CLI.

### Log in to Heroku:

```bash
Copy code
heroku login
```
### Create a Heroku App:
```bash

heroku create finance-django
```
### Set up environment variables:
```bash

heroku config:set DATABASE_URL=your_database_url
heroku config:set SECRET_KEY=your_secret_key
heroku config:set ALPHA_VANTAGE_API_KEY=your_api_key
```
### Push the code to Heroku:
```bash
git push heroku main
```
### CI/CD with GitHub Actions

We automated the deployment process of this Django application to Heroku using GitHub Actions.

### Setup GitHub Actions:
Create a `.github/workflows/deploy.yml` file.

This workflow automatically runs when code is pushed to the main branch.

### CI/CD Pipeline:
The pipeline checks out the latest code.
It sets up Python, installs dependencies, and runs tests.
Finally, the code is deployed to Heroku using the Heroku API key (stored in GitHub Secrets).

## AWS Deployment (Initial Setup)

Initially, I set up the project for deployment on AWS using EC2, Elastic Beanstalk, and RDS (PostgreSQL). Here are the practical steps:

### Setting up AWS RDS for PostgreSQL Database:

### Create the RDS instance:

Navigate to RDS in the AWS Management Console and launch a new PostgreSQL database instance.
Configure public access, storage, and security groups.

### Configure Security Group for RDS:

Allow inbound traffic on port 5432 (PostgreSQL) from EC2 and Elastic Beanstalk instances via a custom TCP rule.

### Set up Environment Variables:

Add RDS credentials as environment variables in the Elastic Beanstalk console.

### Setting up AWS Elastic Beanstalk for Deployment:

### Create Elastic Beanstalk Application:

Created a Docker application environment for deploying the Django app.

### Configure Environment Variables:

Added Alpha Vantage API key, database credentials, and Django secret key.

### Security Groups:

Allowed inbound traffic on port 8000 for testing purposes during the initial setup.

### Setting up EC2 Instances:
EC2 instances were auto-provisioned by Elastic Beanstalk.
Configured IAM roles for secure access to RDS and other AWS services.

### Switching to Heroku:
After facing billing issues with AWS services, I switched to Heroku for deployment.
