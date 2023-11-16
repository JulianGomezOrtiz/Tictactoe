# Define las constantes para las puntuaciones
WIN_SCORE = 10
NEUTRAL_SCORE = 0
LOSE_SCORE = -10

# Define la clase para representar el nodo del árbol


class Node:
    def __init__(self, board, player):
        self.board = board
        self.player = player

# Función para evaluar el estado del tablero


def evaluate_board(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return player
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return player
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return player

    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Draw'

    return None

# Función para evaluar los movimientos


def evaluate_move(board, move, player):
    new_board = [row[:] for row in board]
    new_board[move[0]][move[1]] = player
    result = evaluate_board(new_board, player)

    if result == player:
        return WIN_SCORE
    elif result == 'Draw':
        return NEUTRAL_SCORE
    else:
        return 0  # Cambiado a 0, ya que no queremos asignar puntuación negativa por perder inmediatamente


# Función para obtener todos los posibles movimientos con sus puntuaciones


def get_all_moves_with_scores(node, player):
    valid_moves = get_valid_moves(node.board)
    moves_with_scores = []

    for move in valid_moves:
        score = evaluate_move(node.board, move, player)
        new_board = [row[:] for row in node.board]
        new_board[move[0]][move[1]] = player
        moves_with_scores.append((new_board, move, score))

    return moves_with_scores

# Función para obtener todos los movimientos válidos


def get_valid_moves(board):
    valid_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                valid_moves.append((row, col))
    return valid_moves

# Muestra el estado del tictactoe


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Ejemplo de cómo utilizar las funciones anteriores
if __name__ == "__main__":
    initial_board = [['X', ' ', ' '], [' ', 'X', ''], [' ', 'O', 'O']]
    current_player = 'X'

    print("¡Bienvenido al juego de Tic-Tac-Toe!")

    print("Tablero Inicial:")
    print_board(initial_board)

    root_node = Node(initial_board, current_player)

    all_moves_with_scores = get_all_moves_with_scores(
        root_node, current_player)

    print("Posibles movimientos con puntuaciones:")
    for move_with_score in all_moves_with_scores:
        board = move_with_score[0]
        move = move_with_score[1]
        score = move_with_score[2]
        print_board(board)
        print(f"Jugada: {move}, Puntuación: {score}")
        print("-" * 30)
