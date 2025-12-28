// Store current board state
let board = [" ", " ", " ", " ", " ", " ", " ", " ", " "];

// ----------------------------
// HANDLE HUMAN MOVE
// ----------------------------
function playMove(index) {

    let gameOver = false;

    if (gameOver) return;


    // Prevent clicking already filled cell
    if (board[index] !== " ") {
        return;
    }

    // Send move to backend
    fetch("/move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ move: index })
    })

    .then(response => response.json())
    .then(data => {

        // Update board from server response
        board = data.board;
        updateBoardUI();

        // Show result if game ended
        if (data.result !== "Continue") {
            document.getElementById("status").innerText = data.result;
            gameOver = true;
        }

    });
}

// ----------------------------
// UPDATE UI
// ----------------------------
function updateBoardUI() {
    const buttons = document.querySelectorAll("#board button");

    buttons.forEach((btn, index) => {
        btn.innerText = board[index];
    });
}

// ----------------------------
// RESET GAME
// ----------------------------
function resetGame() {
    const btn = document.querySelector("button[onclick='resetGame()']");
    btn.disabled = true;

    fetch("/reset", { method: "POST" })
    .then(res => res.json())
    .then(data => {
        board = data.board;
        updateBoardUI();
        document.getElementById("status").innerText = "";
        gameOver = false;
        btn.disabled = false;
    });
}


