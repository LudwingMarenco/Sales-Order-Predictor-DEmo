from icecream import install
from modules.sales_training_data import training_data
from modules.sales_training_data import test_data
import dvc.api


if __name__ == "__main__":
    # Get the configuration from the specified config file
    config = dvc.api.params_show(stages="process_data") 

    install()
    
    training_data(config=config)
    test_data(config=config)

