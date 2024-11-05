import yfinance as yf
from arch.unitroot import PhillipsPerron

def fetch_and_analyze_data(ticker, start_date, end_date):
    """
    Fetch data from Yahoo Finance and perform Phillips-Perron test
    
    Parameters:
    ticker (str): Stock ticker symbol
    start_date (str): Start date in 'YYYY-MM-DD' format
    end_date (str): End date in 'YYYY-MM-DD' format
    
    Returns:
    tuple: PP test statistics and results dataframe
    """
    # Fetch data
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    
    # Calculate daily returns
    df['Returns'] = df['Close'].pct_change().dropna()
    
    # Perform Phillips-Perron test
    pp = PhillipsPerron(df['Returns'].dropna())
    pp_result = pp.summary()
    
    # Create results dictionary
    results = {
        'Test Statistic': pp.stat,
        'P-value': pp.pvalue,
        'Critical Values': pp.critical_values,
        'Lags Used': pp.lags,
        'Observations': pp.nobs
    }
    
    return results, df

# Example usage
if __name__ == "__main__":
    # Set parameters
    ticker = "AAPL"  # Apple stock as example
    start_date = "2019-05-10"
    end_date = "2024-05-10"
    
    # Run analysis
    results, data = fetch_and_analyze_data(ticker, start_date, end_date)
    
    # Print results
    print(f"\nPhillips-Perron Test Results for {ticker}:")
    print("-" * 50)
    print(f"Test Statistic: {results['Test Statistic']:.4f}")
    print(f"P-value: {results['P-value']:.4f}")
    print("\nCritical Values:")
    for key, value in results['Critical Values'].items():
        print(f"{key}: {value:.4f}")
    print(f"\nNumber of observations: {results['Observations']}")
    print(f"Lags used: {results['Lags Used']}")
    
    # Interpretation
    alpha = 0.05  # 5% significance level
    if results['P-value'] < alpha:
        print("\nResult: Reject the null hypothesis of a unit root.")
        print("The time series is stationary.")
    else:
        print("\nResult: Fail to reject the null hypothesis of a unit root.")
        print("The time series is non-stationary.")