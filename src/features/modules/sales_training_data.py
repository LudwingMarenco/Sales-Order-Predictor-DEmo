import pandas as pd


def training_data(config: dict) -> None:
    ic()  # type: ignore # noqa: F821
    order_data = pd.read_parquet(config["order_file"])
    

    date = pd.date_range(
        start=order_data["order_date"].min(), end=order_data["order_date"].max()
    )
    ic(len(date))  # type: ignore # noqa: F821
    training_data = pd.DataFrame({"order_date": date})
    ic(len(order_data["account_id"].unique().tolist()))  # type: ignore # noqa: F821
    for account in order_data["account_id"].unique().tolist():
        aux = order_data[order_data["account_id"] == account]["order_date"].tolist()
        aux2 = order_data[order_data["account_id"] == account]["orders"].tolist()
        mapp = dict(zip(aux, aux2))
        aux = training_data["order_date"].apply(lambda x: mapp.get(x, 0)).to_list()
        for i in range(1, len(aux)):
            if aux[i] < aux[i-1] and aux[i] == 0 and aux[i-1] != 1:
                aux[i] = aux[i-1]
        aux_df=pd.DataFrame({account: aux})
        training_data=pd.concat([training_data, aux_df], axis=1)
    ic(training_data.to_parquet(config["training_file"]))  # type: ignore # noqa: F821

    return None

def test_data(config: dict) -> None:
    ic()  # type: ignore # noqa: F821
    test_data=pd.read_parquet(config["order_test_file"])
    ic(len(test_data["account_id"].unique().tolist()))  # type: ignore # noqa: F821
    date = pd.date_range(
        start=test_data["order_date"].min(), end=test_data["order_date"].max()
    )
    ic(len(date))  # type: ignore # noqa: F821
    training_data = pd.DataFrame({"order_date": date})
    # ic(len(test_data["account_id"].unique().tolist()[0:config["accounts"]]))  # type: ignore # noqa: F821

    for account in test_data["account_id"].unique().tolist():
        aux = test_data[test_data["account_id"] == account]["order_date"].tolist()
        aux2 = test_data[test_data["account_id"] == account]["orders"].tolist()
        mapp = dict(zip(aux, aux2))
        aux = training_data["order_date"].apply(lambda x: mapp.get(x, 0)).to_list()
        for i in range(1, len(aux)):
            if aux[i] < aux[i-1] and aux[i] == 0 and aux[i-1] != 1:
                aux[i] = aux[i-1]
        aux_df=pd.DataFrame({account: aux})
        training_data=pd.concat([training_data, aux_df], axis=1)
    ic(training_data.to_parquet(config["test_file"]))  # type: ignore # noqa: F821

    return None
