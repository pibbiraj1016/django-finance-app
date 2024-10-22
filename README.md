Django Finance App

This project is a Django-based backend system that fetches financial data, stores it in a PostgreSQL database, performs basic backtesting on historical stock data, generates predictions using a pre-trained model, and outputs reports in both JSON and PDF formats. The application is deployed on Heroku and integrates with Alpha Vantage API for financial data.

Deploy URL

Deployed Project on Heroku

Quick Links for Functionality

Fetch Stock Data: Fetch AAPL Stock Data
Backtest Strategy: Backtest for AAPL
Predict Stock Prices: Predict AAPL Stock Prices (30 Days)
Backtest Report (JSON): Backtest Report (JSON)
Backtest Report (PDF): Backtest Report (PDF)
Prediction Report (JSON): Prediction Report (JSON)
Prediction Report (PDF): Prediction Report (PDF)

Table of Contents

Features
Requirements
API Keys
Setup and Installation
Running Migrations
Fetching Stock Data
Running the Backtest
Generating Predictions
Report Generation
Testing
Deploying to Heroku
CI/CD with GitHub Actions
AWS Deployment (Initial Setup)

Features

Fetches historical stock prices using Alpha Vantage API.
Stores the data in a PostgreSQL database.
Implements a basic moving average crossover strategy for backtesting.
Predicts future stock prices using a pre-trained machine learning model.
Generates performance reports in JSON and PDF formats.

Requirements

Python 3.9+
PostgreSQL
Django 4.2+
Alpha Vantage API key
Heroku CLI (if deploying to Heroku)

API Keys

You will need to create an Alpha Vantage account and obtain an API key to fetch stock data.

Sign up at Alpha Vantage.
Add your API key to the .env file under ALPHA_VANTAGE_API_KEY.
Example .env file:

env
Copy code
ALPHA_VANTAGE_API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
DEBUG=True
SECRET_KEY=your_secret_key_here
Setup and Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/django-finance-app.git
cd django-finance-app
Set up a virtual environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Configure environment variables:
Copy the .env.example file to .env and fill in your details:

bash
Copy code
cp .env.example .env
Update the .env file with your API keys, database URL, and other environment variables.

Running Migrations
After setting up your environment, you need to run database migrations:

bash
Copy code
python manage.py migrate
This will apply all the necessary migrations to create the database schema.

Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
You should be able to access the application at http://127.0.0.1:8000/.

Fetching Stock Data
To fetch stock data for a specific symbol (e.g., AAPL), use the following URL:

sql
Copy code
GET /stocks/fetch-stocks/?symbol=AAPL
Response Example:

json
Copy code
{
  "status": "success",
  "message": "Data for AAPL fetched and saved."
}
Running the Backtest
You can backtest a stock based on a moving average strategy with this API:

bash
Copy code
GET /stocks/backtest/?symbol=AAPL&initial_investment=10000
Response Example:

json
Copy code
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
Generating Predictions
Predict stock prices for the next 30 days:

bash
Copy code
GET /stocks/predict-stock/?symbol=AAPL&days=30
Response Example:

json
Copy code
{
  "status": "success",
  "predictions": [
    { "date": "2024-01-01", "predicted_price": 150.23 },
    { "date": "2024-01-02", "predicted_price": 151.56 }
  ]
}
Report Generation
You can generate reports in both JSON and PDF formats.

Backtest Report (PDF):
bash
Copy code
GET /stocks/report/?type=backtest&symbol=AAPL&initial_investment=10000&format=pdf
Prediction Report (PDF):
bash
Copy code
GET /stocks/report/?type=prediction&symbol=AAPL&days=30&format=pdf
Testing
The project contains several test cases to validate the functionality of backtesting and prediction features.

To run the tests:

bash
Copy code
python3 manage.py test finance.stocks.tests
Deploying to Heroku
Set up Heroku CLI:
Install Heroku CLI from here.

Log in to Heroku:

bash
Copy code
heroku login
Create a Heroku App:
bash
Copy code
heroku create finance-django
Set up environment variables:
bash
Copy code
heroku config:set DATABASE_URL=your_database_url
heroku config:set SECRET_KEY=your_secret_key
heroku config:set ALPHA_VANTAGE_API_KEY=your_api_key
Push the code to Heroku:
bash
Copy code
git push heroku main
CI/CD with GitHub Actions
We automated the deployment process of this Django application to Heroku using GitHub Actions.

Setup GitHub Actions:
Create a .github/workflows/deploy.yml file.
This workflow automatically runs when code is pushed to the main branch.
CI/CD Pipeline:
The pipeline checks out the latest code.
It sets up Python, installs dependencies, and runs tests.
Finally, the code is deployed to Heroku using the Heroku API key (stored in GitHub Secrets).
