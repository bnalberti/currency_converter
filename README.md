# 💱 Currency Converter CLI Tool

A simple CLI tool to convert currencies using real-time or mock exchange rates. Built to demonstrate production-ready Python code practices.

## 🧰 Features
- Modular code structure
- Logging
- Command-line interface with argparse
- Type hinting
- Unit testing with pytest
- Virtual environment compatibility
- Mock data option for testing offline

## 🚀 Usage
```bash
python main.py --base USD --target EUR --amount 100
python main.py --base GBP --target JPY --amount 200 --mock
```

## 🧪 Run Tests
```bash
pytest tests/
```

## 📁 Project Structure
```
currency_converter/
├── main.py
├── cli.py
├── fetcher.py
├── converter.py
├── logger_config.py
├── data/
│   └── mock_rates.json
├── tests/
│   └── test_converter.py
├── requirements.txt
└── README.md
```
