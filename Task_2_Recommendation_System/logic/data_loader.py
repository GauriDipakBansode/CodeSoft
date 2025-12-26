import pandas as pd

def load_ratings(file_path):
    """Loads ratings dataset from a CSV file 
       and returns a cleaned DataFrame"""
    
    # Read CSV file
    df = pd.read_csv(file_path)

    # Remove any missing values 
    df = df.dropna()

    # Ensure correct data types
    df["user_id"] = df["user_id"].astype(int)
    df["product_id"] = df["product_id"].astype(int)
    df["rating"] = df["rating"].astype(float)

    return df


def create_user_item_matrix(df):

    """ Converts ratings DataFrame into 
        user-item matrix """
    
    user_item_matrix = df.pivot(
        
    )
    