# Django Finance App

This project is a Django-based backend system that fetches financial data, stores it in a PostgreSQL database, performs basic backtesting on historical stock data, generates predictions using a pre-trained model, and outputs reports in both JSON and PDF formats. The application is deployed on Heroku and integrates with Alpha Vantage API for financial data.

Deploy URL - https://finance-django-93f5ce60f767.herokuapp.com/

Fetch stock - https://finance-django-93f5ce60f767.herokuapp.com/stocks/predict-stock/?symbol=AAPL&days=30

Backtest - https://finance-django-93f5ce60f767.herokuapp.com/stocks/backtest/?symbol=AAPL&initial_investment=10000

Predict - https://finance-django-93f5ce60f767.herokuapp.com/stocks/predict-stock/?symbol=AAPL&days=30

Backtest Report(Json) - https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=backtest&symbol=AAPL&initial_investment=10000&format=json

Backtest Report (PDF) - https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=backtest&symbol=AAPL&initial_investment=10000&format=pdf

Prediction Report(Json) - https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=prediction&symbol=AAPL&days=30&format=json

Prediction Report(PDF) - https://finance-django-93f5ce60f767.herokuapp.com/stocks/report/?type=prediction&symbol=AAPL&days=30&format=pdf

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [API Keys](#api-keys)
4. [Setup and Installation](#setup-and-installation)
5. [Running Migrations](#running-migrations)
6. [Fetching Stock Data](#fetching-stock-data)
7. [Running the Backtest](#running-the-backtest)
8. [Generating Predictions](#generating-predictions)
9. [Report Generation](#report-generation)
10. [Deploying to Heroku](#deploying-to-heroku)

---

## Features

- Fetches historical stock prices using Alpha Vantage API.
- Stores the data in a PostgreSQL database.
- Implements a basic moving average crossover strategy for backtesting.
- Predicts future stock prices using a pre-trained machine learning model.
- Generates performance reports in JSON and PDF formats.

---

## Requirements

- Python 3.9+
- PostgreSQL
- Django 4.2+
- Alpha Vantage API key
- Heroku CLI (if deploying to Heroku)

---

## API Keys

You will need to create an Alpha Vantage account and obtain an API key to fetch stock data.

1. Sign up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
2. Add your API key to the `.env` file under `ALPHA_VANTAGE_API_KEY`.

Example `.env` file:

ALPHA_VANTAGE_API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
DEBUG=True
SECRET_KEY=your_secret_key_here

Setup and Installation

1. Clone the repository
   - git clone https://github.com/pibbiraj1016/django-finance-app.git
   - cd django-finance-app

2. Set up a virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install dependencies
   - pip install -r requirements.txt
   
4. Configure environment variables
   Copy the .env.example file to .env and fill in your details:
   - cp .env.example .env
   Update the .env file with your API keys, database URL, and other environment variables.

# Django secret key
SECRET_KEY='your-secret-key'

# Debug mode (Turn it off for production)
DEBUG=False

# Database configuration (for local development using docker-compose)
DB_NAME=finance
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

# Alpha Vantage API key
ALPHA_VANTAGE_API_KEY='your-alpha-vantage-api-key'
ALPHA_VANTAGE_URL='https://www.alphavantage.co/query'

Running Migrations
After setting up your environment, you need to run database migrations:

- python manage.py migrate
This will apply all the necessary migrations to create the database schema.

Run the Development Server
Start the Django development server:

- python manage.py runserver
You should be able to access the application at http://127.0.0.1:8000/.

Fetching Stock Data
To fetch stock data for a specific symbol (e.g., AAPL), use the following command or make an API request:
Fetch daily stock prices from the Alpha Vantage API and store them in the database.

URL: /stocks/fetch-stocks/

Method: GET

- http://localhost:8000/stocks/fetch-stocks/?symbol=AAPL
  This will store historical stock data in the PostgreSQL database.

  Response:
{
    "status": "success",
    "message": "Data for GOOG fetched and saved."
}

Running the Backtest
The backtest functionality allows you to input investment amount, and simulate trades based on moving averages:
Perform a backtest on the stock data using simple moving averages (50-day and 200-day).

URL: /stocks/backtest/

Method: GET

- http://localhost:8000/stocks/backtest/?symbol=AAPL&initial_investment=5000
  This returns a performance summary of the backtest.
  
Response:
  {
    "status": "success",
    "result": {
        "initial_investment": 5000,
        "final_portfolio_value": 5450,
        "total_return": 9.0,
        "max_drawdown": 2.5,
        "trades": [
            {
                "date": "2023-01-10",
                "type": "buy",
                "price": 105.0,
                "shares": 50
            },
            {
                "date": "2023-05-15",
                "type": "sell",
                "price": 110.0,
                "shares": 50
            }
        ]
    }
}


Generating Predictions
You can predict stock prices for the next 30 days using the following API:
- http://localhost:8000/stocks/predict-stock/?symbol=AAPL&days=30
  This will store the predictions in the database and return the predicted stock prices.

  Response:
    {
    "status": "success",
    "predictions": [
        {
            "date": "2024-01-01",
            "predicted_price": 110.23
        },
        {
            "date": "2024-01-02",
            "predicted_price": 111.56
        }
    ]
}


Report Generation
Reports can be generated in both JSON and PDF formats:

Backtest Report (PDF):
- http://localhost:8000/stocks/report/?type=backtest&symbol=AAPL&initial_investment=10000

Prediction Report (PDF):
- http://localhost:8000/stocks/report/?type=prediction&symbol=AAPL&days=30

Testing
The project contains several test cases to validate the functionality of backtesting and prediction features.

To run the tests:

- python3 manage.py test finance.stocks.tests
This will run the available test suite. Ensure that your environment variables and database are properly configured for testing.

Deploying to Heroku
This project is set up for deployment on Heroku. Follow these steps:

1. Install Heroku CLI
    Download and install the Heroku CLI.

2. Log in to Heroku
    heroku login

3. Create a Heroku app
    heroku create finance-django
   
4. Set up environment variables
    Set your environment variables on Heroku (including your DATABASE_URL, SECRET_KEY, and ALPHA_VANTAGE_API_KEY):
- heroku config:set DATABASE_URL=your_database_url
- heroku config:set SECRET_KEY=your_secret_key
- heroku config:set ALPHA_VANTAGE_API_KEY=your_api_key
  
5. Push the code to Heroku
- git push heroku main
This will trigger the deployment process.

CI/CD with GitHub Actions
We automated the deployment process of this Django application to Heroku using GitHub Actions.

Setup GitHub Actions:

We created a GitHub Actions workflow in the .github/workflows/deploy.yml file.
This workflow automatically runs when code is pushed to the main branch.

CI/CD Pipeline:

The pipeline checks out the latest code.
It sets up Python, installs dependencies, and runs any necessary checks.
Finally, the code is deployed to Heroku using the Heroku API key, securely stored in GitHub Secrets.

Heroku Deployment:

The project is deployed on Heroku.
The Procfile ensures that the app runs with Gunicorn as the server.







AWS Deployment (Initial Setup)
Initially, I set up the project for deployment on AWS using EC2, Elastic Beanstalk, and RDS (PostgreSQL). Below are the steps I followed for each service:

1. Setting up AWS RDS for PostgreSQL Database:
Create the RDS instance:

I navigated to RDS in the AWS Management Console and launched a new PostgreSQL database instance.
Configured the instance with the required storage and memory.
Selected "Public Access" to ensure the database could be accessed from the EC2 instances and Elastic Beanstalk.

Configure Security Group for RDS:

I created a security group for the RDS instance that allowed inbound traffic on port 5432 (PostgreSQL port) from the EC2 and Elastic Beanstalk instances using Custom TCP Rule.
Allowed connections from 0.0.0.0/0 during setup for testing but restricted it later to only allow access from my application.

Set up Environment Variables for Django:

Added the database credentials as environment variables in the Elastic Beanstalk console to securely configure Django settings without hardcoding.
Set DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, and DB_PORT environment variables in the Django app's settings.py.

2. Setting up AWS Elastic Beanstalk for Deployment:
   
Create Elastic Beanstalk Application:

I created a new Elastic Beanstalk environment for a Docker application, since I was deploying a Dockerized Django app.
Uploaded the Dockerized Django app to Elastic Beanstalk using a zip archive that included the Docker configuration.
Configure Environment Variables:

Added necessary environment variables like the Alpha Vantage API key, database credentials, and Django secret key in the Elastic Beanstalk console under Configuration -> Software.

Security Groups for EC2 Instances:

Set up a security group for the Elastic Beanstalk EC2 instances to allow inbound traffic on port 8000 for the Django app.

Configured Custom TCP Rule for port 80 (HTTP) and port 443 (HTTPS) to allow web traffic access to the EC2 instances via Elastic Beanstalk.

3. Setting up EC2 Instances:
   
Auto-provisioning through Elastic Beanstalk:

Elastic Beanstalk automatically provisioned EC2 instances for the application.
The instances were configured with the required instance type and security group to allow inbound traffic from 0.0.0.0/0 for testing purposes.

IAM Roles for EC2:

I assigned IAM roles to the EC2 instances to allow the application to securely access other AWS services like RDS and S3 (if needed).

Created a custom IAM role and attached it to the EC2 instances from the Elastic Beanstalk console under Configuration -> Instances.

5. Setting up Docker on AWS:

Dockerfile Configuration:

I wrote a Dockerfile to package the Django application with all its dependencies.
The Dockerfile exposed port 8000 for the Django app and used Gunicorn to serve the application.

Upload and Deploy Dockerized Application:

Uploaded the application with the Dockerfile to Elastic Beanstalk, ensuring that all dependencies were installed inside the container.

Testing the Application:

After the application was deployed, I tested the deployment by accessing the Elastic Beanstalk public URL.

7. Switching to Heroku:
After facing billing issues with AWS services, I decided to switch to Heroku for hosting the application. This was a more cost-effective option for a smaller-scale project.
On Heroku, I followed similar steps to set up environment variables for the database and Alpha Vantage API, and redeployed the Dockerized app as outlined in the Heroku section of the README.













