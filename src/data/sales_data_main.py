from modules.sales_checker_users import check_users
from modules.sales_extract_users_data import extract_users_data
from modules.sales_test_data import get_test_data
from icecream import install
import dvc.api 


if __name__ == "__main__":
    # Get the configuration from the specified config file
    config = dvc.api.params_show(stages="create_data") 

    install()

    users = check_users(config=config)

    active_users=extract_users_data(config=config, users=users)

    get_test_data(config=config, active_users=active_users)


