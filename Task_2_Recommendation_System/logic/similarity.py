#similarity.py
#calculates similarity between users

from sklearn.metrics.pairwise import cosine_similarity



def calculate_user_similarity(user_item_matrix):

    """ Takes user-item matrix and returns user_user similarity matrix"""

    #fill missing ratings with 0
    user_item_matrix_filled = user_item_matrix_.fillna(0)

    #calculate cosine similarity
    similarity = cosine_similarity(user_item_matrix_filled)


    return similarity

