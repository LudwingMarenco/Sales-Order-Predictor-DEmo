import argparse
from utils.sales_utils import get_config
from modules.sales_checker_users import check_users
from modules.sales_extract_users_data import extract_users_data
from modules.sales_test_data import get_test_data
from icecream import install


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

    users = check_users(config=config)

    active_users=extract_users_data(config=config, users=users)

    get_test_data(config=config, active_users=active_users)


