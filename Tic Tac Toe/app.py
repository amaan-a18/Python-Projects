from flask import Flask, render_template, request, redirect, session
import copy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for sessions

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def is_draw(board):
    return all(cell != "" for row in board for cell in row)

@app.route("/", methods=["GET", "POST"])
def index():
    if "board" not in session:
        session["board"] = [["" for _ in range(3)] for _ in range(3)]
        session["turn"] = "X"

    board = copy.deepcopy(session["board"])
    turn = session["turn"]
    message = ""

    if request.method == "POST":
        row = int(request.form["row"])
        col = int(request.form["col"])

        if board[row][col] == "":
            board[row][col] = turn
            winner = check_winner(board)

            if winner:
                message = f"Player {winner} wins!"
                session.clear()
            elif is_draw(board):
                message = "It's a draw!"
                session.clear()
            else:
                session["turn"] = "O" if turn == "X" else "X"
                session["board"] = board

    return render_template("index.html", board=board, turn=turn, message=message)

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
