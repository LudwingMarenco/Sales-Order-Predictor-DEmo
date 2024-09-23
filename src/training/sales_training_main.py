import argparse
from utils.sales_utils import get_config
from icecream import install
from modules.sales_regressor import sales_regressor

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Add a command-line argument for the config file
    parser.add_argument("--config_file", type=str, dest="config", required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the configuration from the specified config file
    config = get_config(args.config)

    install()

    sales_regressor(config=config)