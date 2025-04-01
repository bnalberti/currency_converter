from cli import parse_arguments
from fetcher import get_exchange_rate
from converter import convert
from logger_config import setup_logging

logger = setup_logging()

def main():
    args = parse_arguments()
    logger.info(f"Arguments received: {args}")

    try:
        rate = get_exchange_rate(args.base, args.target, use_mock=args.mock)
        result = convert(args.amount, rate)
        logger.info(f"{args.amount} {args.base} = {result:.2f} {args.target}")
        print(f"{args.amount} {args.base} = {result:.2f} {args.target}")
    except Exception as e:
        logger.error(f"Conversion failed: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
