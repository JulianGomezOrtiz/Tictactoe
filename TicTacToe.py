# Define una función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Define una función para verificar si el juego ha terminado
def is_game_over(board):
    for player in ['X', 'O']:
        if (board[0][0] == board[0][1] == board[0][2] == player or
            board[1][0] == board[1][1] == board[1][2] == player or
            board[2][0] == board[2][1] == board[2][2] == player or
            board[0][0] == board[1][0] == board[2][0] == player or
            board[0][1] == board[1][1] == board[2][1] == player or
            board[0][2] == board[1][2] == board[2][2] == player or
            board[0][0] == board[1][1] == board[2][2] == player or
            board[0][2] == board[1][1] == board[2][0] == player):
            return player  # Un jugador ha ganado

    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Empate'  # El juego ha terminado en empate

    return None

# Define una función para realizar el movimiento del jugador
def make_move(board, move, player):
    row, col = move
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False

# Define la función de evaluación basada en el árbol de búsqueda (Minimax)
def evaluate_board(board, player, depth, maximizing_player):
    winner = is_game_over(board)

    if winner == player:
        return 10 - depth
    elif winner is not None:
        return depth - 10

    if maximizing_player:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player
                    eval = evaluate_board(board, player, depth + 1, False)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O' if player == 'X' else 'X'
                    eval = evaluate_board(board, player, depth + 1, True)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Función para seleccionar la mejor jugada usando el algoritmo Minimax
def select_best_move(board, player):
    best_eval = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                eval = evaluate_board(board, player, 0, False)
                board[row][col] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

# Función principal para jugar el juego
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    winner = None

    print("¡Bienvenido al juego de Tic-Tac-Toe!")

    while not winner:
        print_board(board)
        print(f"Turno del jugador {current_player}.")

        if current_player == 'X':
            row = int(input("Ingrese el número de fila (0, 1, o 2): "))
            col = int(input("Ingrese el número de columna (0, 1, o 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                make_move(board, (row, col), current_player)
            else:
                print("Movimiento inválido. Intente de nuevo.")
        else:
            best_move = select_best_move(board, current_player)
            make_move(board, best_move, current_player)

        winner = is_game_over(board)
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    if winner == 'Empate':
        print("¡El juego ha terminado en empate!")
    else:
        print(f"¡El jugador {winner} ha ganado!")

# Inicia el juego
if __name__ == "__main__":
    play_tic_tac_toe()
