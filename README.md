# Binance Futures Testnet Trading Bot

A simplified and structured Python trading bot built for the Binance USDT-M Futures Testnet.

This application allows users to place MARKET and LIMIT orders directly from the command line while maintaining clean architecture, validation, logging, and exception handling.

The project was developed as part of a Python Developer Internship assignment.

---

# Features

## Core Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL order sides
- Binance Futures Testnet integration
- Command Line Interface (CLI)
- Structured reusable codebase
- Logging of:
  - API requests
  - API responses
  - Errors and exceptions
- Input validation
- Exception handling

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core Programming Language |
| python-binance | Binance API SDK |
| Typer | Command Line Interface |
| python-dotenv | Environment Variable Management |
| Colorama | Colored Terminal Output |
| Logging Module | Log Management |

---

# Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── cli.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repository-url>
cd trading_bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

## Step 1: Open Binance Futures Testnet

Visit:

https://testnet.binancefuture.com

---

## Step 2: Generate API Keys

- Login to Binance Futures Testnet
- Open API Management
- Create a new API Key and Secret

---

## Step 3: Configure Environment Variables

Create a `.env` file in the project root directory.

Example:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

---

# Running the Application

The application uses a CLI interface.

---

# MARKET Order Example

```bash
python -m bot.cli BTCUSDT BUY MARKET 0.001
```

---

# LIMIT Order Example

```bash
python -m bot.cli BTCUSDT SELL LIMIT 0.001 --price 78000
```

---

# Command Parameters

| Parameter | Description | Example |
|---|---|---|
| symbol | Trading pair | BTCUSDT |
| side | BUY or SELL | BUY |
| order_type | MARKET or LIMIT | MARKET |
| quantity | Order quantity | 0.001 |
| --price | Required for LIMIT orders | 78000 |

---

# Example Successful Output

```bash
========== ORDER REQUEST ==========
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

========== ORDER SUCCESS ==========
Order ID       : 123456789
Status         : FILLED
Executed Qty   : 0.001
Avg Price      : 76900
```

---

# Logging

All API requests, responses, and errors are stored in:

```bash
logs/trading_bot.log
```

Example log output:

```bash
2026-05-18 15:22:54,494 - INFO - Placing order: BTCUSDT SELL LIMIT Qty=0.001 Price=78000
2026-05-18 15:22:55,459 - INFO - Order response: {...}
```

---

# Validation and Error Handling

The application includes validation for:

- Invalid order side
- Invalid order type
- Invalid quantity
- Missing price for LIMIT orders
- Binance API exceptions
- Network or unexpected runtime errors

Example:

```bash
ERROR: APIError(code=-4024): Limit price can't be lower than allowed price.
```

---

# Code Architecture

## `client.py`
Handles Binance API client initialization and Testnet configuration.

---

## `orders.py`
Contains reusable order placement logic.

---

## `validators.py`
Validates all user inputs before order execution.

---

## `logging_config.py`
Configures file and console logging.

---

## `cli.py`
Main command-line entry point of the application.

---

# Security Notes

- API keys are stored using environment variables
- `.env` is excluded from Git tracking
- Sensitive credentials are never hardcoded

---

# .gitignore

```gitignore
venv/
__pycache__/
.env
logs/
```

---

# Requirements

```txt
python-binance
typer
python-dotenv
colorama
```

---

# Future Improvements

Potential enhancements:

- Stop-Limit Orders
- OCO Orders
- Web Dashboard
- Real-time Price Streaming
- Docker Support
- Database Integration
- Trading Strategy Automation

---

# Assumptions

- User has an active Binance Futures Testnet account
- Valid API credentials are configured
- Testnet wallet contains sufficient virtual balance

---

# Assignment Requirements Covered

| Requirement | Status |
|---|---|
| MARKET Orders | Completed |
| LIMIT Orders | Completed |
| BUY / SELL Support | Completed |
| CLI Input | Completed |
| Validation | Completed |
| Logging | Completed |
| Error Handling | Completed |
| Structured Code | Completed |
| README Documentation | Completed |

---

# Author

## Rahul Jangir

Python Developer Internship Assignment Submission

```