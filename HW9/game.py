import random
import math
import time
import random

class TeekoPlayer:
    """ An object representation for an AI game player for the game Teeko.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.

        Args:
            state (list of lists): should be the current state of the game as saved in
                this TeekoPlayer object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.

                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).

        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """

        # t0 = time.time()
        # print("State",state)
        max_val, move = self.max_value(state,depth=2)
        # if(move == None):
        #     # print("IDK")
        #     # print(state)
        # t1 = time.time()
        # print(t1-t0)

        return move

        # TODO: detect drop phase
    def detect_drop_phase(self, state):
        count = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                count += 1 if state[i][j] != ' ' else 0

        return True if count < 8 else False


    # TODO: get all successors
    def succ(self, state, piece):
        drop = self.detect_drop_phase(state)
        successors = []

        if drop:
             # go through every possibility
            for row in range(len(state)):
                for col in range(len(state[row])):
                    if state[row][col] == ' ':
                        successors.append([(row,col)])

        else:
            # print("row:",len(state))
            for row in range(len(state)):
                for col in range(len(state[row])):
                    # print("col:",len(state[row]))
                    if state[row][col] == piece:
                        if (row+1) < len(state) and (col) < len(state[row+1]) and  state[row+1][col] == ' ':
                            #print("Hello")
                            successors.append([(row+1,col),(row,col)])
                        elif (row+1) < len(state) and (col+1) < len(state[row+1]) and  state[row+1][col+1] == ' ':
                            #print("Happy")
                            successors.append([(row+1,col+1),(row,col)])
                        elif (row) < len(state) and (col+1) < len(state[row]) and  state[row][col+1] == ' ':
                            #print("Sad")
                            successors.append([(row,col+1),(row,col)])
                        elif (row -1) >= 0 and (col+1) < len(state[row-1]) and  state[row-1][col+1] == ' ':
                            #print("Here")
                            successors.append([(row - 1,col+1),(row,col)])
                        elif (row -1) >= 0 and (col) < len(state[row-1]) and  state[row-1][col] == ' ':
                            #print("Where")
                            successors.append([(row - 1,col),(row,col)])
                        elif (row -1) >= 0 and (col-1) > 0 and  state[row-1][col-1] == ' ':
                            #print("Hope")
                            successors.append([(row - 1,col-1),(row,col)])
                        elif (row) >= 0 and (col-1) >= 0 and  state[row][col-1] == ' ':
                            #print("Hopeless")
                            successors.append([(row,col-1),(row,col)])
                        elif (row +1) < len(state) and (col-1) > 0 and  state[row+1][col-1] == ' ':
                            #print("Bachlock")
                            successors.append([(row + 1,col-1),(row,col)])
                        

        return successors

        # TODO: return number describing state. 
        # Implement hueristic when not terminal state
    def hueristic_game_value(self, state, piece):
        """
        # Args: state->state of game::piece-> piece to be moved
        # if we detect a terminal state 
        # find the max length of numbers pieces in the right order for a possible win
        # my_score will add one for each piece in the correct place
        # opp_score will subtract one for each piece in the correct place
        # we will divide by 4 to keep the number between 1 and -1
        # if the absolute value of the two scores are equal then whoever goes first has the upper hand
        # if the absolute value of the my_score > opp_score and it is my_piece then return my_score
        # if the absolute value of the my_score < opp_score and it is opp_piece then return abs(opp_score)
        # the same goes true for opponent
        """
        if(self.game_value(state) != 0):
            return self.game_value(state)

        score = 0
        # find all scores of winning rows
        for row in range(5):
            for col in range(2):
                temp_score = 0
                my_score = 0
                opp_score = 0
                my_score += 1 if state[row][col] == self.my_piece else 0
                my_score += 1 if state[row][col+1] == self.my_piece else 0
                my_score += 1 if state[row][col+2] == self.my_piece else 0
                my_score += 1 if state[row][col+3] == self.my_piece else 0
                opp_score += -1 if state[row][col] == self.opp else 0
                opp_score += -1 if state[row][col+1] == self.opp else 0
                opp_score += -1 if state[row][col+2] == self.opp else 0
                opp_score += -1 if state[row][col+3] == self.opp else 0
                temp_score += 0 if state[row][col] == ' ' else 1 if state[row][col] == self.my_piece else -1
                temp_score += 0 if state[row][col+1] == ' ' else 1 if state[row][col+1] == self.my_piece else -1
                temp_score += 0 if state[row][col+2] == ' ' else 1 if state[row][col+2] == self.my_piece else -1
                temp_score += 0 if state[row][col+3] == ' ' else 1 if state[row][col+3] == self.my_piece else -1
                score = score if abs(score) > abs(temp_score) else temp_score
                if((my_score == 1 and opp_score == -3) and self.my_piece == piece): # if true then blocking. 
                    return 0.8
        # find all scores of winning columns
        for col in range(5):
            for row in range(2):
                temp_score = 0
                my_score = 0
                opp_score = 0
                my_score += 1 if state[row][col] == self.my_piece else 0
                my_score += 1 if state[row+1][col] == self.my_piece else 0
                my_score += 1 if state[row+2][col] == self.my_piece else 0
                my_score += 1 if state[row+3][col] == self.my_piece else 0
                opp_score += -1 if state[row][col] == self.opp else 0
                opp_score += -1 if state[row+1][col] == self.opp else 0
                opp_score += -1 if state[row+2][col] == self.opp else 0
                opp_score += -1 if state[row+3][col] == self.opp else 0
                temp_score += 0 if state[row][col] == ' ' else 1 if state[row][col] == self.my_piece else -1
                temp_score += 0 if state[row+1][col] == ' ' else 1 if state[row+1][col] == self.my_piece else -1
                temp_score += 0 if state[row+2][col] == ' ' else 1 if state[row+2][col] == self.my_piece else -1
                temp_score += 0 if state[row+3][col] == ' ' else 1 if state[row+3][col] == self.my_piece else -1
                score = score if abs(score) > abs(temp_score) else temp_score
                if((my_score == 1 and opp_score == -3) and self.my_piece == piece): # if true then blocking
                    return 0.8
        # find all scores of winning diagonals
        for row in range(2):
            for col in range(2):
                temp_score = 0
                my_score = 0
                opp_score = 0
                my_score += 1 if state[row][col] == self.my_piece else 0
                my_score += 1 if state[row+1][col+1] == self.my_piece else 0
                my_score += 1 if state[row+2][col+2] == self.my_piece else 0
                my_score += 1 if state[row+3][col+3] == self.my_piece else 0
                opp_score += -1 if state[row][col] == self.opp else 0
                opp_score += -1 if state[row+1][col+1] == self.opp else 0
                opp_score += -1 if state[row+2][col+2] == self.opp else 0
                opp_score += -1 if state[row+3][col+3] == self.opp else 0
                temp_score += 0 if state[row][col] == ' ' else 1 if state[row][col] == self.my_piece else -1
                temp_score += 0 if state[row+1][col+1] == ' ' else 1 if state[row+1][col+1] == self.my_piece else -1
                temp_score += 0 if state[row+2][col+2] == ' ' else 1 if state[row+2][col+2] == self.my_piece else -1
                temp_score += 0 if state[row+3][col+3] == ' ' else 1 if state[row+3][col+3] == self.my_piece else -1
                score = score if abs(score) > abs(temp_score) else temp_score
                if((my_score == 1 and opp_score == -3) and self.my_piece == piece): # if true then blocking
                    return 0.8
                
                
        for row in range(3,5,1):
            for col in range(2):
                temp_score = 0
                my_score = 0
                opp_score = 0
                my_score += 1 if state[row][col] == self.my_piece else 0
                my_score += 1 if state[row-1][col+1] == self.my_piece else 0
                my_score += 1 if state[row-2][col+2] == self.my_piece else 0
                my_score += 1 if state[row-3][col+3] == self.my_piece else 0
                opp_score += -1 if state[row][col] == self.opp else 0
                opp_score += -1 if state[row-1][col+1] == self.opp else 0
                opp_score += -1 if state[row-2][col+2] == self.opp else 0
                opp_score += -1 if state[row-3][col+3] == self.opp else 0
                temp_score += 0 if state[row][col] == ' ' else 1 if state[row][col] == self.my_piece else -1
                temp_score += 0 if state[row-1][col+1] == ' ' else 1 if state[row-1][col+1] == self.my_piece else -1
                temp_score += 0 if state[row-2][col+2] == ' ' else 1 if state[row-2][col+2] == self.my_piece else -1
                temp_score += 0 if state[row-3][col+3] == ' ' else 1 if state[row-3][col+3] == self.my_piece else -1
                score = score if abs(score) > abs(temp_score) else temp_score
                if((my_score == 1 and opp_score == -3) and self.my_piece == piece): # if true then blocking
                    return 0.8
        # find all scores of winning boxes
        for row in range(4):
            for col in range(4):
                temp_score = 0
                my_score = 0
                opp_score = 0
                my_score += 1 if state[row][col] == self.my_piece else 0
                my_score += 1 if state[row+1][col] == self.my_piece else 0
                my_score += 1 if state[row+1][col+1] == self.my_piece else 0
                my_score += 1 if state[row][col+1] == self.my_piece else 0
                opp_score += -1 if state[row][col] == self.opp else 0
                opp_score += -1 if state[row+1][col] == self.opp else 0
                opp_score += -1 if state[row+1][col+1] == self.opp else 0
                opp_score += -1 if state[row][col+1] == self.opp else 0
                temp_score += 0 if state[row][col] == ' ' else (1 if state[row][col] == self.my_piece else -1)
                temp_score += 0 if state[row+1][col] == ' ' else (1 if state[row+1][col] == self.my_piece else -1)
                temp_score += 0 if state[row+1][col+1] == ' ' else (1 if state[row+1][col+1] == self.my_piece else -1)
                temp_score += 0 if state[row][col+1] == ' ' else (1 if state[row][col+1] == self.my_piece else -1)
                score = score if abs(score) > abs(temp_score) else temp_score
                if((my_score == 1 and opp_score == -3)): # if true then blocking
                    return 0.8
        score = score/4
        return score


        # TODO: max part of minimax
    def max_value(self, state,depth):
        if(self.hueristic_game_value(state,self.my_piece) == 1 or self.hueristic_game_value(state,self.my_piece) == -1 or depth == 0):
            return self.hueristic_game_value(state,self.my_piece),None
        else:
            successors = self.succ(state,self.my_piece)
            rand = random.randint(0,len(successors)-1)
            max_successor = successors[rand]
            alpha = self.hueristic_game_value(self.generate_state(state=state,move=max_successor,piece=self.my_piece),self.my_piece)
            # print("Alpha:",alpha)
            for successor in successors:
                temp_state = self.generate_state(state,successor,self.my_piece)
                alpha_prime,move = self.min_value(temp_state,depth-1)
                move = successor if move == None else move
                if(alpha < alpha_prime or alpha == -math.inf):
                    alpha = alpha_prime
                    max_successor = successor
        return alpha,max_successor

        # TODO: min part of minimax
    def min_value(self, state, depth):
        if(self.hueristic_game_value(state,self.opp) == 1 or self.hueristic_game_value(state,self.opp) == -1 or depth == 0):
            return self.hueristic_game_value(state,self.opp),None
        else:
            successors = self.succ(state,self.opp)
            rand = random.randint(0,len(successors)-1)
            min_successor = successors[rand]
            alpha = self.hueristic_game_value(self.generate_state(state=state,move=min_successor,piece=self.opp),self.opp)
            # print("Alpha:",alpha)
            for successor in successors:
                temp_state = self.generate_state(state,successor,self.opp)
                alpha_prime,move = self.max_value(temp_state,depth-1)
                move = successor if move == None else move
                if(alpha > alpha_prime or alpha == math.inf):
                    alpha = alpha_prime
                    min_successor = successor
        return alpha,min_successor

    def generate_state(self,state,move,piece):
        new_state = []
        for inner in state:
            new_state.append(inner.copy())
        # print(new_state)
        if(len(move) == 1):
            new_state[move[0][0]][move[0][1]] = piece
        else:
            new_state[move[0][0]][move[0][1]] = ' '
            new_state[move[1][0]][move[1][1]] = piece
        return new_state

    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row) + ": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this TeekoPlayer object, or a generated successor state.

        Returns:
            int: 1 if this TeekoPlayer wins, -1 if the opponent wins, 0 if no winner

        TODO: complete checks for diagonal and box wins
        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                    return 1 if row[i] == self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i + 1][col] == state[i + 2][col] == state[i + 3][col]:
                    return 1 if state[i][col] == self.my_piece else -1

        # TODO: check \ diagonal wins
        # Right side
        for row in range(2):
            for col in range(2):
                if state[row][col] != ' ' and state[row][col] == state[row+1][col+1] and state[row+1][col+1] == state[row+2][col+2] and state[row+2][col+2] == state[row+3][col+3]:
                    return 1 if state[row][col] == self.my_piece else -1
                
        for row in range(3,5,1):
            for col in range(2):
                if state[row][col] != ' ' and state[row][col] == state[row-1][col+1] and state[row-1][col+1] == state[row-2][col+2] and state[row-2][col+2] == state[row-3][col+3]:
                    return 1 if state[row][col] == self.my_piece else -1
        # # TODO: check / diagonal wins
        # # Left side
        # for row in range(2):
        #     for col in range(3,5,1):
        #         if state[row][col] != ' ' and state[row][col] == state[row+1][col-1] and state[row+1][col-1] == state[row+2][col-2] and state[row+2][col-2] == state[row+3][col-3]:
        #             return 1 if state[row][col] == self.my_piece else -1
        
        # for row in range(3,5,1):
        #     for col in range(3,5,1):
        #         if state[row][col] != ' ' and state[row][col] == state[row-1][col-1] and state[row-1][col-1] == state[row-2][col-2] and state[row-2][col-2] == state[row-3][col-3]:
        #             return 1 if state[row][col] == self.my_piece else -1
        # TODO: check box wins
        for row in range(4):
            for col in range(4):
                if state[row][col] != ' ' and state[row][col] == state[row+1][col] and state[row+1][col] == state[row+1][col+1] and state[row+1][col+1] == state[row][col+1]:
                    return 1 if state[row][col] == self.my_piece else -1


        return 0  # no winner yet


############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################
def main():
    print('Hello, this is Samaritan')
    ai = TeekoPlayer()
    piece_count = 0
    turn = 0

    # drop phase
    while piece_count < 8 and ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece + " moved at " + chr(move[0][1] + ord("A")) + str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp + "'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0]) - ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece + " moved from " + chr(move[1][1] + ord("A")) + str(move[1][0]))
            print("  to " + chr(move[0][1] + ord("A")) + str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp + "'s turn")
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0]) - ord("A")),
                                      (int(move_from[1]), ord(move_from[0]) - ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        print("AI wins! Game over.")
    else:
        print("You win! Game over.")


if __name__ == "__main__":
    main()
