# Player Class
class Player:
    def __init__(self, token, name):
        self.token = token
        self.name = name
        self.locations = []

    def get_token(self):
        return self.token

    def get_name(self):
        return self.name

    def add_location(self, v):
        self.locations.append(v)

    def get_locations(self):
        return self.locations


# Functions
def player_setup():
    player1_token = None
    while player1_token != "X" and player1_token != "O":
        player1_token = input("Player 1, would you like to be X or O: ")
        player1_token = player1_token.upper()
    if player1_token == "X":
        player2_token = "O"
    else:
        player2_token = "X"
    return player1_token, player2_token


def draw_board(board):
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-----------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")


def user_input(player):
    in_range = False
    pos = "FLAG"

    while not pos.isdigit() or not in_range:
        pos = input(player.get_name() + ", enter a position (1-9) to add your " + player.get_token() + ": ")
        if not pos.isdigit():
            print("[!] There was an error with your input! Try again.")
        else:
            if int(pos) in range(1, 10):
                in_range = True
            else:
                print("[!] There was an error with your input! Try again.")

    return int(pos)


def check_position(board, pos):
    if board[pos] == " ":
        return True
    else:
        return False


# ----Game Logic----
# Game loop
play_again = True

while play_again:
    # Player setup
    player1_token, player2_token = player_setup()

    # Draw initial board
    board = {9: " ", 8: " ", 7: " ", 6: " ", 5: " ", 4: " ", 3: " ", 2: " ", 1: " "}
    draw_board(board)

    player1 = Player(player1_token, "Player1")
    player2 = Player(player2_token, "Player2")

    players = [player1, player2]

    player_list = [player1, player2]
    player = player1

    # Round Loop
    player_won = False

    while not player_won:
        # User input
        pos = user_input(player)

        # Check position
        if check_position(board, pos):
            board[pos] = player.get_token()
            player.add_location(pos)

        else:
            print("That position is already taken. Try again")
            continue

        draw_board(board)

        # Check Board
        # make sure the board isn't full
        full = True
        for x in range(1, 10):
            if board[x] == " ":
                full = False
                break
        if full:
            print("It is a tie!")
            break

        solution_list = [[7, 8, 9],
                         [4, 5, 6],
                         [1, 2, 3],
                         [1, 4, 7],
                         [2, 5, 8],
                         [3, 6, 9],
                         [1, 5, 9],
                         [7, 5, 3]]
        for solution_set in solution_list:
            for location in player.get_locations():
                if location in solution_set:
                    solution_set.remove(location)
            if len(solution_set) == 0:
                print("Congratulations, " + player.get_name() + "! You won!")
                player_won = True
                break

        player = player_list[abs(player_list.index(player)-1)]

    player_response = None
    answered = False
    while not answered:
        player_response = input("Would you like to play again? [y,n]: ")

        if player_response.lower() == "y":
            play_again = True
            answered = True
        elif player_response.lower() == "n":
            play_again = False
            answered = True
        else:
            print("Invalid entry, try again!")
