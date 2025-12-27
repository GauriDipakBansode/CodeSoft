from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def compute_similarity(user_item_matrix):
    """
    Compute cosine similarity between users
    """
    matrix_filled = user_item_matrix.fillna(0)

    similarity = cosine_similarity(matrix_filled.values)

    similarity_df = pd.DataFrame(
        similarity,
        index=matrix_filled.index,
        columns=matrix_filled.index
    )

    return similarity_df
