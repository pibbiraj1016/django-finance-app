# finance/stocks/tests.py

from django.test import TestCase
from finance.stocks.utils import backtest_strategy
from finance.stocks.models import StockPrice
from django.urls import reverse

class BacktestStrategyTestCase(TestCase):
    def setUp(self):
        # Insert some stock price data to use in tests
        StockPrice.objects.create(symbol="AAPL", date="2023-01-01", open_price=100, close_price=105, high_price=110, low_price=99, volume=1000)
        StockPrice.objects.create(symbol="AAPL", date="2023-01-02", open_price=105, close_price=108, high_price=112, low_price=103, volume=1000)
        StockPrice.objects.create(symbol="AAPL", date="2023-01-03", open_price=108, close_price=103, high_price=109, low_price=101, volume=1000)
        StockPrice.objects.create(symbol="AAPL", date="2023-01-04", open_price=103, close_price=107, high_price=110, low_price=102, volume=1000)

    def test_backtest_strategy(self):
        # Call the backtest strategy with a test symbol and initial investment
        result = backtest_strategy(symbol="AAPL", initial_investment=10000)

        # Assert the result contains a valid total return
        self.assertIsInstance(result['total_return'], float)

        # Assert that at least one trade was made
        self.assertGreaterEqual(len(result['trades']), 1)

        # Assert that max drawdown is calculated
        self.assertIn('max_drawdown', result)

class StockPredictionTest(TestCase):
    def test_valid_predict_stock(self):
        """
        Test valid request with symbol and days.
        """
        # Test valid symbol and valid days parameter
        response = self.client.get(reverse('predict_stock'), {'symbol': 'AAPL', 'days': 30})
        self.assertEqual(response.status_code, 200)  # Status should be 200 OK
        response_json = response.json()
        self.assertIn('predictions', response_json)  # Ensure predictions are present
        self.assertIsInstance(response_json['predictions'], list)  # Predictions should be a list
        self.assertGreaterEqual(len(response_json['predictions']), 1)  # Should contain predictions

    def test_missing_days_with_default(self):
        """
        Test missing days parameter should default to 30 days.
        """
        response = self.client.get(reverse('predict_stock'), {'symbol': 'AAPL'})
        self.assertEqual(response.status_code, 200)  # Status should be 200 OK
        response_json = response.json()
        self.assertIn('predictions', response_json)  # Ensure predictions are present
        self.assertGreaterEqual(len(response_json['predictions']), 1)  # Should contain predictions
        # Optional: Check if a warning is included if you use the warning pattern
        # self.assertIn('warning', response_json)

    def test_invalid_symbol(self):
        """
        Test invalid stock symbol should return error.
        """
        response = self.client.get(reverse('predict_stock'), {'symbol': 'INVALID', 'days': 30})
        self.assertEqual(response.status_code, 400)  # Status should be 400 Bad Request
        response_json = response.json()
        self.assertIn('error', response_json)
        self.assertEqual(response_json['message'], "No data found for symbol INVALID")  # Adjust based on your error message

    def test_invalid_days_value(self):
        """
        Test invalid days parameter (negative or non-integer) should return error.
        """
        # Negative days value
        response = self.client.get(reverse('predict_stock'), {'symbol': 'AAPL', 'days': -10})
        self.assertEqual(response.status_code, 400)  # Status should be 400 Bad Request
        response_json = response.json()
        self.assertIn('error', response_json)
        self.assertEqual(response_json['message'], "Invalid value for days")  # Adjust based on your error message

        # Non-integer days value
        response = self.client.get(reverse('predict_stock'), {'symbol': 'AAPL', 'days': 'abc'})
        self.assertEqual(response.status_code, 400)  # Status should be 400 Bad Request
        response_json = response.json()
        self.assertIn('error', response_json)
        self.assertEqual(response_json['message'], "Invalid value for days")  # Adjust based on your error message

    def test_missing_symbol(self):
        """
        Test missing stock symbol should default to a known valid symbol or return error.
        """
        response = self.client.get(reverse('predict_stock'), {'days': 30})
        self.assertEqual(response.status_code, 200)  # Status should be 200 OK (if default symbol is used)
        response_json = response.json()
        self.assertIn('predictions', response_json)  # Should contain predictions for the default symbol (if applicable)

        # If you want to enforce that a symbol must always be provided, modify this to expect a 400 error:
        # self.assertEqual(response.status_code, 400)  # Status should be 400 if symbol is required
        # self.assertIn('error', response.json())
        # self.assertEqual(response.json()['message'], "Symbol parameter is missing")

    def test_no_parameters(self):
        """
        Test when no parameters are provided (use defaults if applicable).
        """
        response = self.client.get(reverse('predict_stock'))
        self.assertEqual(response.status_code, 200)  # Status should be 200 OK (if defaults are used)
        response_json = response.json()
        self.assertIn('predictions', response_json)  # Ensure predictions are present
        self.assertGreaterEqual(len(response_json['predictions']), 1)  # Should contain predictions