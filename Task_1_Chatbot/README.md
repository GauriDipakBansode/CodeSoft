# Rule-Based Chatbot   
### CodeSoft Internship – Task 1

---

## Project Description

This project is a **Rule-Based Chatbot** built as part of the **CodeSoft Internship (Task 1)**.  
The chatbot works by matching user input with predefined rules (semantic word mapping) and responding accordingly.

The project demonstrates the integration of:
- Frontend (HTML, CSS, JavaScript)
- Backend (Python with Flask)
- Basic chatbot logic without using any AI/ML libraries

---

## Features

- Rule-based conversational chatbot  
- Simple and clean web interface  
- Flask backend to process user messages  
- JavaScript frontend to send and receive messages  
- Beginner-friendly implementation  

---

## Technologies Used

- **Frontend**:  
  - HTML  
  - CSS  
  - JavaScript  

- **Backend**:  
  - Python  
  - Flask  

- **Data Format**:  
  - JSON (for communication between frontend and backend)

---

## Project Structure
```bash

Task_1_Chatbot/
│
├── app.py # Flask backend
├── chatbot.py # Chatbot logic (rule-based)
│
├── templates/
│ └── index.html # Frontend HTML
│
├── static/
│ ├── style.css # CSS styling
│ └── script.js # JavaScript logic
│
└── README.md # Project documentation

```md


---

## How the Chatbot Works (Flow)

1. User types a message in thebrowser.
2. JavaScript captures the message.
3. JavaScript sends the message to Flask using `fetch()` (POST request).
4. Flask receives the message.
5. Flask sends the message to `chatbot.py`.
6. Chatbot logic detects the concept and selects a response.
7. Flask sends the response back as JSON.
8. JavaScript receives the response and displays it on the webpage.

---

## How to Run the Project

### Step 1: Clone the repository
```bash
- git clone <your-github-repo-link>
cd Task_1_Chatbot
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py
http://127.0.0.1:5000/

```

---

## Future Improvements

Add more rules and better intent detection
Store chat history in a database
Improve UI design
Add NLP or ML-based chatbot logic

---

## Author

Gauri
Third Year Engineering Student
CodeSoft Internship – Task 1

---