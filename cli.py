"""
This module handles command-line argument parsing for the currency converter CLI tool.
It defines and validates the expected inputs such as base currency, target currency, amount to convert, and whether to use mock data instead of live exchange rates
"""

import argparse

def parse_arguments():

    """
    Parses command-line arguments provided by the user

    Returns:
        An object containing the parsed argument:
        - base (str): Base currency code 
        - target (str): Target currency code 
        - amount (float): Amount to be converted
        - mock (bool): Whether to use mock exchange rate data
    """
    parser = argparse.ArgumentParser(description="Currency converter CLI tool.") 
    parser.add_argument("--base", required=True, help="Base currency code (e.g. USD)") # Required - base currency
    parser.add_argument("--target", required=True, help="Target currency code (e.g. EUR)")# Require - target currency
    parser.add_argument("--amount", required=True, type=float, help="Amount to convert") # Required - amount to convert
    parser.add_argument("--mock", action="store_true", help="Use mock data instead of live API") # Optional use mock data instead of live API
    return parser.parse_args()
