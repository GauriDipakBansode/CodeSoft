import pandas as pd

def load_data(file_path):
    """
    Load ratings CSV and return DataFrame
    """
    df = pd.read_csv(file_path)
    df = df.dropna()

    df["user_id"] = df["user_id"].astype(str)
    df["product_id"] = df["product_id"].astype(str)
    df["rating"] = df["rating"].astype(float)

    return df


def create_user_item_matrix(df):
    """
    Convert DataFrame into user-item matrix
    """
    user_item_matrix = df.pivot_table(
        index="user_id",
        columns="product_id",
        values="rating"
    )

    return user_item_matrix
