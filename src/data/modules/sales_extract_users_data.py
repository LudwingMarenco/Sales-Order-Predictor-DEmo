import pandas as pd


def extract_users_data(config: dict, users: list) -> list:
    ic()  # type: ignore  # noqa: F821
    ic("Extracting historical data")  # type: ignore  # noqa: F821
    historical_sales = pd.read_parquet(config["historical_sales"])
    historical_sales["order_date"] = pd.to_datetime(historical_sales["order_date"])
    ic(len(historical_sales))  # type: ignore # noqa: F821
    extracted_data = historical_sales[historical_sales["account_id"].isin(users)]
    ic(len(extracted_data["account_id"].unique()))  # type: ignore # noqa: F821
    ic(len(extracted_data))  # type: ignore # noqa: F821
    orders_sales_data = (
        extracted_data.groupby(
            [extracted_data["account_id"], extracted_data["order_date"]]
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
    ic(orders_sales_data.to_parquet(config["order_file"]))  # type: ignore  # noqa: F821
    ic("Returning active users")  # type: ignore # noqa: F821

    return extracted_data["account_id"].unique().tolist()
