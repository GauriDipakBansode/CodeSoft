# Task 2 – Product Recommendation System  
**CodeSoft Internship**

---

## Project Overview

This project is a **Product Recommendation System** developed as **Task 2** of the **CodeSoft Internship**.  
The system recommends products to users based on their preferences using **Collaborative Filtering**.

It analyzes user–product rating data, finds users with similar interests, and suggests products that a user has not rated yet but similar users have liked.

---

## Objective

- To build a real-world recommendation system
- To understand collaborative filtering concepts
- To integrate machine learning logic with a web application
- To display recommendations through a browser interface

---

## Recommendation Technique Used

**User-Based Collaborative Filtering**

- Users are compared based on rating patterns
- Cosine Similarity is used to measure similarity between users
- Products are recommended based on weighted ratings from similar users

---

## Technologies Used

- **Python**
- **Flask** (Backend Web Framework)
- **Pandas & NumPy** (Data Processing)
- **Scikit-learn** (Cosine Similarity)
- **HTML, CSS, JavaScript** (Frontend)

---

## Project Structure

```bash

Task_2_Recommendation_System/
│
├── backend/                         # Backend (Flask Web App)
│   │
│   ├── app.py                       # Main Flask application (routes + API)
│   │
│   ├── templates/                   # HTML templates
│   │   └── index.html               # Frontend UI
│   │
│   └── static/                      # Static frontend files
│       ├── script.js                # JS: handles user input & API calls
│       └── style.css                # CSS: UI styling
│
├── data/                            # Dataset layer
│   └── ratings.csv                  # User–Product ratings data
│
├── logic/                           # Recommendation & ML logic
│   │
│   ├── data_loader.py               # Loads & preprocesses CSV data
│   ├── similarity.py                # Computes user similarity (cosine)
│   ├── recommender.py               # Generates product recommendations
│   └── __pycache__/                 # Python cache files
│
├── venv/                            # Virtual environment (dependencies)
│
├── .gitignore                       # Git ignored files
│
└── README.md                        # Project documentation



```

---


## Dataset Description

The dataset (`ratings.csv`) contains:

| Column Name | Description |
|------------|-------------|
| user_id | Unique user identifier |
| product_id | Unique product identifier |
| rating | Rating given by the user (1–5) |

**Important:**  
Not all users rate all products. Missing ratings are essential for generating recommendations.

---

## How the System Works

1. Load user–product ratings from CSV
2. Create a user-item matrix using pivot table
3. Handle missing values (`NaN`)
4. Compute similarity between users using cosine similarity
5. Identify products not rated by the target user
6. Calculate weighted scores using similar users’ ratings
7. Recommend top-N products

---

## Web Application Flow

1. User enters `user_id` in the browser
2. JavaScript sends the user ID to Flask backend
3. Flask processes the request using recommendation logic
4. Recommended products are returned as JSON
5. Results are displayed on the webpage

---

## How to Run the Project

```bash
pip install flask pandas numpy scikit-learn
cd backend
python app.py
http://127.0.0.1:5000

```

---

## Key Learnings

- Understanding collaborative filtering
- Handling missing data in recommendation systems
- Working with pivot tables and similarity matrices
- Backend–frontend communication using APIs
- Debugging real-world issues in ML projects


---

## Conclusion

This project successfully demonstrates a real-world product recommendation system using collaborative filtering.
It highlights how data preprocessing, similarity computation, and backend–frontend integration work together to deliver personalized recommendations.

---

## Developed By

Gauri
CodeSofr Internship - Task 2

