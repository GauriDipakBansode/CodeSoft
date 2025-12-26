import numpy as np
import pandas as pd


def generate_recommendations(user_id, user_item_matrix, similarity_matrix, top_n=5):

    """
    Generate product recommendations for a given user

    Parameters:
    user_id            -> user for whom recommendations are needed
    user_item_matrix   -> rows: users, columns: products, values: ratings
    similarity_matrix  -> similarity score between users
    top_n              -> number of recommendations to return
    """


    # -------------------------------
    # Step 1: Get similarity scores
    # -------------------------------
    # This gives how similar all users are to the given user
    user_similarities = similarity_matrix.loc[user_id]


    # -------------------------------
    # Step 2: Sort users by similarity
    # -------------------------------
    # Most similar users come first
    user_similarities = user_similarities.sort_values(ascending=False)

    # Remove the user itself (similarity = 1)
    user_similarities = user_similarities.drop(user_id)

    # -------------------------------
    # Step 3: Get products not rated
    # -------------------------------
    user_ratings = user_item_matrix.loc[user_id]

    # Products where rating is NaN → not rated yet
    unrated_products = user_ratings[user_ratings.isna()].index

    # -------------------------------
    # Step 4: Score each unrated product
    # -------------------------------
    product_scores = {}


    for product in unrated_products:

        weighted_sum = 0
        similarity_sum = 0


        # Look at similar users
        for similar_user, similarity in user_similarities.items():

            rating = user_item_matrix.loc[similar_user, product]

            # Consider only users who rated this product
            if not np.isnan(rating):
                weighted_sum += similarity * rating
                similarity_sum += similarity

        # Avoid division by zero
        if similarity_sum > 0:
            product_scores[product] = weighted_sum / similarity_sum

    # -------------------------------
    # Step 5: Sort and return top N
    # -------------------------------
    recommendations = sorted(
        product_scores.items(),
        key = lambda x: x[1], 
        reverse = True
    )


    return recommendations[:top_n]

