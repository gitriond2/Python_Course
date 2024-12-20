# Finance Dashboard

This project is a web application built with Flask that displays a candlestick chart for Google's stock prices using the Bokeh library. The data is fetched from Yahoo Finance.

## Features

- Fetches stock data from Yahoo Finance
- Displays a candlestick chart with high and low segments
- Differentiates between days with increased and decreased closing prices
- Fully responsive and styled with Bokeh

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later
- Flask
- Pandas
- yfinance
- Bokeh
- NumPy

## Installation

1. Clone this repository to your local machine.

```sh
git clone https://github.com/your-username/finance-dashboard.git
cd finance-dashboard

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

echo Flask > requirements.txt
echo pandas >> requirements.txt
echo yfinance >> requirements.txt
echo bokeh >> requirements.txt
echo numpy >> requirements.txt

flask run

Open your web browser and go to http://127.0.0.1:5000/finance/ to view the candlestick chart.

## Project Structure
app.py: The main Flask application.

templates/layout.html: The base HTML template.

templates/home.html: The home page HTML template.

templates/finance.html: The finance page HTML template.

static/: Directory for static files (CSS, JavaScript, images).
