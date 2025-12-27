import numpy as np
import pandas as pd

def recommend_products(user_id, user_item_matrix, similarity_matrix, top_n=5):

    if user_id not in user_item_matrix.index:
        return []

    # Similarity scores of other users
    user_similarities = similarity_matrix.loc[user_id].drop(user_id)

    # Ratings by this user
    user_ratings = user_item_matrix.loc[user_id]

    # Products NOT rated by this user
    unrated_products = user_ratings[user_ratings.isna()].index

    product_scores = {}

    for product in unrated_products:
        weighted_sum = 0
        similarity_sum = 0

        for other_user, similarity in user_similarities.items():
            rating = user_item_matrix.loc[other_user, product]

            if not pd.isna(rating):
                weighted_sum += similarity * rating
                similarity_sum += similarity

        if similarity_sum > 0:
            product_scores[product] = weighted_sum / similarity_sum

    recommendations = sorted(
        product_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:top_n]
