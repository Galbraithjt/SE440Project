class ChessBoard(object): #singleton Used to keep one instance of board
    difficulty = 1
    computer_move_linked_list = []

    def generate_board(self):
        print("board ready")

    def __set_difficulty(self):
        print("difficulty set to {}".format(self.difficulty))

    def __player_color_choice(self):
        print("Choose your side")


#every Move will check for checkmate and set to true if it is.
class ChessPiece(object):

    def move(self):
        print("")

class King(ChessPiece):
    #will have methods to conrol movement
    def move(self):
        print("king moved")
        Observer.check_checkmate

class Queen(ChessPiece):
    # will have methods to conrol movement
    def move(self):
        print("queen moved")
        Observer.check_checkmate

class Knight(ChessPiece):
    # will have methods to conrol movement
    def move(self):
        print("knight moved")
        Observer.check_checkmate

class Bishop(ChessPiece):
    # will have methods to conrol movement
    def move(self):
        print("bishop moved")
        Observer.check_checkmate

class Rook(ChessPiece):
    # will have methods to conrol movement
    def move(self):
        print("rook moved")
        Observer.check_checkmate

class Pawn(ChessPiece):
    # will have methods to conrol movement
    def move(self):
        print("pawn moved")
        Observer.check_checkmate

class Observer(object):
    #will check for check mate and control when to go to end game
    checkmate = false
    def check_checkmate(self):
        #will check for check mate here and set to true if it is.
        if(checkmate == true) :
        EndGame.game_over
        else :
        ChangeTurns.computer_move

class EndGame(object):

    def game_over(self):
        print("Game Over")

class ChangeTurns(object):

    def computer_move(self):
        print("computer turn")

        #Computer makes Move

        print("Player Turn")

        # Game allows player to move