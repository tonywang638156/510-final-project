# 510-final-project
## Step 1: Stock Data Collection Script 

This script collects stock data for a given stock symbol (AAPL) over the last 30 days from Yahoo Finance, and saves it as a CSV file.

## Requirements

Before running the script, make sure to install the required Python packages. You can use `pip` to install them.

### Packages required:
- `yfinance` - A Python library to download Yahoo Finance data
- `datetime` - For date manipulation
- `os` - For file operations

To install the `yfinance` package, run the following command:

```bash
pip install yfinance
```



## Step 2: News Data Collection Script

This script collects news articles related to "Apple Stock" over the last 30 days using the [NewsAPI](https://newsapi.org/). It fetches the top articles each day based on popularity and saves them as a CSV file.

## Requirements

Before running the script, make sure to install the required Python packages. You can use `pip` to install them.

### Packages required:
- `requests` - A simple HTTP library to make requests to the NewsAPI.
- `pandas` - For data manipulation and saving the results to a CSV file.
- `datetime` - For date manipulation

To install the required libraries, run the following command:

```bash
pip install requests pandas
```

## step 3: Sentiment Analysis on News Articles

This script performs sentiment analysis on the titles and descriptions of news articles using the [Hugging Face Transformers](https://huggingface.co/transformers/) library. The script applies a pre-trained sentiment analysis model to the news articles fetched previously and saves the results to a new CSV file.

## Requirements

Before running the script, make sure to install the required Python packages. You can use `pip` to install them.

### Packages required:
- `transformers` - The Hugging Face library to access pre-trained models and pipelines.
- `torch` - Required for running Hugging Face models.
- `numpy<2` - A specific version of NumPy to avoid compatibility issues with other dependencies.

To install the required libraries, run the following command:

```bash
pip install transformers torch numpy<2
```

## Step 4: Merging Stock Data and News Articles with Sentiment Analysis

This script merges stock data with news articles containing sentiment analysis results. It combines historical stock data with the sentiment of related news articles from the past 30 days, aligning the two datasets by date.

## Requirements

Before running the script, make sure to install the required Python packages. You can use `pip` to install them.

### Packages required:
- `pandas` - A library for data manipulation and analysis.

To install the required library, run the following command:

```bash
pip install pandas
```


## Step 5: Stock Data Analysis with SMA, EMA, and RSI

This script performs technical analysis on stock data by calculating the **Simple Moving Average (SMA)**, **Exponential Moving Average (EMA)**, and **Relative Strength Index (RSI)**. It processes a merged dataset containing stock data and news articles, cleans the data, and computes these key indicators.

## Requirements

Before running the script, ensure that the following Python package is installed:

- `pandas` - A library for data manipulation and analysis.

You can install the required package using:

```bash
pip install pandas
```
