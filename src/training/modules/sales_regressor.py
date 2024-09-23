from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
import joblib


def sales_regressor(config: dict) -> None:
    ic()  # type: ignore # noqa: F821
    ic("Training regressor")  # type: ignore # noqa: F821
    data = pd.read_parquet(config["training_file"])
    data_test = pd.read_parquet(config["test_file"])
    X1 = np.arange(len(data)).reshape((-1, 1))
    y1 = data.loc[:, data.columns != "order_date"].to_numpy()
    X2 = (np.arange(len(data_test)) + len(data)).reshape((-1, 1))
    y2 = data_test.loc[:, data_test.columns != "order_date"].to_numpy()

    X = np.concatenate((X1, X2), axis=0)
    y = np.concatenate((y1, y2), axis=0)

    regr = DecisionTreeRegressor(max_depth=config["max_depth"])
    regr.fit(X, y)

    with open(config["model_name"], "wb") as f:
        joblib.dump(regr, f)

    ic("Regressor saved")  # type: ignore # noqa: F821

    return None
