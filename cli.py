"""
Use argparse to accept user inputs via CLI arguments
"""

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Currency converter CLI tool.")
    parser.add_argument("--base", required=True, help="Base currency code (e.g. USD)")
    parser.add_argument("--target", required=True, help="Target currency code (e.g. EUR)")
    parser.add_argument("--amount", required=True, type=float, help="Amount to convert")
    parser.add_argument("--mock", action="store_true", help="Use mock data instead of live API")
    return parser.parse_args()
