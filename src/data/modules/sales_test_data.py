import pandas as pd


def get_test_data(config: dict, active_users: list) -> None:
    ic()  # type: ignore # noqa: F821
    ic("Getting test data")  # type: ignore # noqa: F821
    august_missing = pd.read_parquet(config["august_missing"])
    august_missing["order_date"] = pd.to_datetime(august_missing["order_date"])
    august_missing = august_missing.dropna()
    august_missing = august_missing[august_missing["account_id"].isin(active_users)]

    orders_sales_data = (
        august_missing.groupby(
            [august_missing["account_id"], august_missing["order_date"]]
        )
        .size()
        .to_frame(name="intra_daily_count")
        .reset_index()
    )
    orders_sales_data["month"] = pd.DatetimeIndex(orders_sales_data["order_date"]).month
    orders_sales_data["year"] = pd.DatetimeIndex(orders_sales_data["order_date"]).year
    orders_sales_data["monthly_orders"] = orders_sales_data.groupby(
        [
            orders_sales_data["account_id"],
            orders_sales_data["month"],
            orders_sales_data["year"],
        ]
    )["month"].transform("count")
    orders_sales_data["orders"] = orders_sales_data.groupby(
        [
            orders_sales_data["account_id"],
            orders_sales_data["month"],
            orders_sales_data["year"],
        ]
    )["month"].cumcount()
    orders_sales_data["orders"] = (
        orders_sales_data["monthly_orders"] - orders_sales_data["orders"]
    )

    ic(len(orders_sales_data))  # type: ignore # noqa: F821
    ic(orders_sales_data.to_parquet(config["test_file"]))  # type: ignore  # noqa: F821

    return None
