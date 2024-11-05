# 📈 Stock Price Stationarity Analysis

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![arch](https://img.shields.io/badge/arch-5.0%2B-orange)

A Python tool for analyzing stock price stationarity using the Phillips-Perron test. This tool helps identify whether a time series exhibits unit root behavior, which is crucial for financial time series analysis and modeling.

## 🚀 Features

- 📊 Downloads historical stock data via `yfinance`
- 📉 Calculates daily returns
- 🔍 Performs Phillips-Perron unit root test
- 📈 Provides detailed test statistics and interpretation
- 📝 Includes comprehensive logging

## 📋 Prerequisites

Before running the script, ensure you have Python 3.7+ installed on your system.

## 🔧 Installation

1. Clone the repository
```bash
git clone https://github.com/YavuzAkbay/phillips-perron-test
cd phillips-perron-test
```

2. Install required packages
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Basic usage with default parameters:
```python
from phillips-perron-test import StationarityAnalyzer

analyzer = StationarityAnalyzer(
    ticker="AAPL",
    start_date="2019-05-10",
    end_date="2024-05-10"
)

results, data = analyzer.analyze()
analyzer.print_results()
```

2. Custom analysis with interpretation:
```python
analyzer = StationarityAnalyzer(ticker="MSFT", start_date="2020-01-01", end_date="2024-05-10")
analyzer.analyze()
interpretation = analyzer.interpret_results(alpha=0.01)  # Custom significance level
print(interpretation)
```

## 📊 Output Example

```
Phillips-Perron Test Results for AAPL:
--------------------------------------------------
Test Statistic: -24.3456
P-value: 0.0001
Critical Values:
1%: -3.4336
5%: -2.8627
10%: -2.5674

Number of observations: 1258
Lags used: 15

The time series is stationary (reject unit root hypothesis)
```

## 🔍 Code Structure

```
phillips-perron-test/
│
├── stock_stationarity.py  # Main script
├── requirements.txt      # Dependencies
├── README.md            # Documentation
└── .gitignore          # Git ignore rules
```

## 📚 Theory

The Phillips-Perron test is a unit root test used in time series analysis to test the null hypothesis that a time series is integrated of order 1 (I(1)). It builds on the Dickey-Fuller test by making non-parametric corrections to address serial correlation.

### Hypotheses:
- H₀: The time series has a unit root (non-stationary)
- H₁: The time series is stationary

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- `yfinance` for stock data access
- `arch` package for Phillips-Perron test implementation
- Financial econometrics literature on unit root testing

## 📧 Contact

Your Name - [akbay.yavuz@gmail.com](mailto:akbay.yavuz@gmail.com)

Project Link: [https://github.com/YavuzAkbay/phillips-perron-test](https://github.com/YavuzAkbay/phillips-perron-test)

---
⭐️ If you found this project helpful, please consider giving it a star!