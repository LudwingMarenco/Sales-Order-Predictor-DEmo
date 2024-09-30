from icecream import install
from modules.sales_regressor import sales_regressor
import dvc.api

if __name__ == "__main__":
    # Get the configuration from the specified config file
    config = dvc.api.params_show(stages="training") 

    install()

    sales_regressor(config=config)