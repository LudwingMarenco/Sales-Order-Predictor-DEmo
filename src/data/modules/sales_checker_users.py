import pandas as pd


def check_users(config: dict) -> list:
    ic()  # type: ignore  # noqa: F821
    august_sales = pd.read_parquet(config["august_sales"])
    august_missing = pd.read_parquet(config["august_missing"])
    august_missing = august_missing.dropna()
    august_missing["users_check"] = (
        august_missing["account_id"].isin(august_sales["account_id"]).astype(int)
    )
    users = august_missing.query("users_check==1")["account_id"].unique().tolist()

    ic("Checking users")  # type: ignore  # noqa: F821
    ic("Quantity of users is " + str(len(users)))  # type: ignore  # noqa: F821

    return users
