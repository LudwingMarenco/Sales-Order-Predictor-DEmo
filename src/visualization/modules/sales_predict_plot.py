import pandas as pd
import numpy as np
import joblib
from matplotlib.figure import Figure

def predict_plot()-> Figure:

    data=pd.read_parquet("data/final/order_training.pqt")
    data_test=pd.read_parquet("data/final/order_test.pqt")

    X_test = (np.arange(len(data_test))+len(data)).reshape((-1,1))
    y_true=data_test.loc[:, data_test.columns != "order_date"].to_numpy()

    regr_3=joblib.load("models/sales_regressor.pkl")
    y_3 = regr_3.predict(X_test)

    fig = Figure()
    ax = fig.subplots() 

    for item in range(5):
        ax.plot(data_test["order_date"], y_true[:,item], marker="*", linestyle="None")
        ax.plot(data_test["order_date"], y_3[:,item], marker=".", color="black", linestyle="None")
        
    fig.autofmt_xdate()
    return fig