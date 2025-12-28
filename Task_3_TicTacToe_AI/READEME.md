# Tic Tac Toe AI (Human vs Computer)

This project is a **Tic Tac Toe game with an AI opponent**, built using **Python, Flask, and the Minimax algorithm**.  
The human player plays as **X**, and the AI plays as **O**.

The AI always makes the **optimal move**, so it can never lose.

---

## Project Structure

```bash

Task_3_TicTacToe_AI/
│
├── backend/
│ └── app.py # Flask backend
│
├── logic/
│ ├── board.py # Board creation & move handling
│ ├── game_rules.py # Win & draw logic
│ ├── minimax.py # Minimax algorithm
│ └── ai_player.py # AI move selection
│
├── templates/
│ └── index.html # Game UI
│
├── static/
│ ├── style.css # Styling
│ └── script.js # Frontend logic
│
├── requirements.txt
└── README.md

```


---

## Features

- Human vs AI gameplay
- AI uses **Minimax algorithm**
- Game stops automatically after win or draw
- Reset game functionality
- Clean UI using HTML & CSS
- Backend logic handled using Flask

---

## How the AI Works (Minimax)

The AI evaluates **all possible future moves** using the Minimax algorithm and chooses the move that:

- Maximizes its chances of winning
- Minimizes the human player's chances

### Score System:
- **+1** → AI wins
- **-1** → Human wins
- **0** → Draw

Because of this, the AI is **unbeatable**.

---

## Installation & Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
pip install flask
cd backend
python app.py
```

---


## How to Play
Click on any empty box to place X
AI will automatically respond with O
Game stops when:
Human wins
AI wins
Draw occurs
Click Reset Game to play again

---

## Technologies Used

Python
Flask
HTML
CSS
JavaScript
Minimax Algorithm

---

## Task Information

Task Name: Tic Tac Toe AI
Task Number: Task 3
Organization: CodeSoft
Level: Beginner → Intermediate

---

## Author

Gauri

---