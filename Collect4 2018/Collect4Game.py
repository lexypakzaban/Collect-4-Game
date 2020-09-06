import random
#Lexy Pakzaban
# strings you'll use to describe the board....
#                                   12345678901234567890123456789012345678901234567890123456789012345678901234567890
BOARD_STRING =          "           -----A--B---C----D-------A--B---C----D-------A--B---C----D-------A--B---C----D--"
PLAYER_1_STARTER_STRING = "Player 1: "
PLAYER_2_STARTER_STRING = "Player 2: "

def draw_board(p1_pos, p2_pos):
    """
    Draws a picture of the current state of the board
    :param p1_pos: the number of the square where player1 is placed
    :param p2_pos: the number of the square where player2 is placed
    :return: None
    """
    # TODO: you write this! It should be pretty similar to the chutes and ladder, but you will want to also draw the
    #      state of the players' chips above (player1) and below (player2) the board.
    print("{0}{1}{2}{3}".format(player_1_has_A, player_1_has_B, player_1_has_C, player_1_has_D))
    print("{0}{1}{2}".format(PLAYER_1_STARTER_STRING, p1_pos * " ", "*"))
    print(BOARD_STRING)
    print("{0}{1}{2}".format(PLAYER_2_STARTER_STRING, p2_pos * " ", "*"))
    print("{0}{1}{2}{3}".format(player_2_has_A, player_2_has_B, player_2_has_C, player_2_has_D))

def reset():
    """
    Sets the variables to the initial value they should have at the start of the game.
    :return: None
    """
    global game_is_still_playing # this is a boolean (True/False) variable
    global player_1_has_A, player_1_has_B, player_1_has_C, player_1_has_D # These are boolean (True/False) variables
    global player_2_has_A, player_2_has_B, player_2_has_C, player_2_has_D # These are boolean (True/False) variables
    global player_1_position, player_2_position # These are numbers.
    global whose_turn_is_it # a number, 1 or 2.
    # TODO: you write this! Give each of the global variables listed above an initial value.
    game_is_still_playing = True
    player_1_has_A = False
    player_1_has_B = False
    player_1_has_C = False
    player_1_has_D = False
    player_2_has_A = False
    player_2_has_B = False
    player_2_has_C = False
    player_2_has_D = False
    whose_turn_is_it = 1
    player_1_position = 1
    player_2_position = 1

def roll_dice():
    """
    rolls two dice, prints the results to screen, and returns the total of them.
    :return: the total of the two dice.
    """
    # TODO: write this!
    draw_board(player_1_position, player_2_position)
    print("Press <return> to roll the dice.")
    dummy = input()
    move_amount_1 = random.randrange(1, 7)
    move_amount_2 = random.randrange(1, 7)
    move_amount = move_amount_1 + move_amount_2
    print("You rolled a {0}.".format(move_amount))

    return move_amount

def player_1_ply():

    #do what needs to happen when it is player 1's turn
    # Ask player to hit <return>
    # Roll dice and get distance to move
    # Change the position by the amount rolled
    # Wrap to start of field, if needed
    # See whether you pick up a chip
    # See whether game is over
    #:return: None


    global game_is_still_playing # change this variable if player 1 wins.
    global player_1_position
    global player_1_has_A
    global player_1_has_B
    global player_1_has_C
    global player_1_has_D
    # TODO: you write this!

    move = roll_dice()
    player_1_position = move + player_1_position

    if player_1_position > 79:
        player_1_position = 1


    if player_1_position % 20 == 6 :
        print ("Player 1 has A")
        player_1_has_A = True

    if player_1_position % 20 == 9 :
        print ("Player 1 has B")
        player_1_has_B = True

    if player_1_position % 20 == 13  :
        print ("Player 1 has C")
        player_1_has_C = True

    if player_1_position % 20 == 18 :
            print ("Player 1 has D")
            player_1_has_D = True

    if player_1_position == player_2_position:
        player_1_position = player_1_position - 1
        player_1_has_A = False
        player_1_has_B = False
        player_1_has_C = False
        player_1_has_D = False

def player_2_ply():

    #do what needs to happen when it is player 2's turn
    # Ask player to hit <return>
    # Roll dice and get distance to move
    # Change the position by the amount rolled
    # Wrap to start of field, if needed
    # See whether you pick up a chip
    # See whether game is over
    #:return: None

    global game_is_still_playing  # change this variable if player 2 wins.
    global player_2_position
    global player_2_has_A
    global player_2_has_B
    global player_2_has_C
    global player_2_has_D
    # TODO: you write this!

    move = roll_dice()
    player_2_position = move + player_2_position

    if player_2_position > 79:
        player_2_position = 1

    if player_2_position % 20 == 6:
        print("Player 2 has A")
        player_2_has_A = True

    if player_2_position % 20 == 9:
        print("Player 2 has B")
        player_2_has_B = True

    if player_2_position % 20 == 13:
        print("Player 2 has C")
        player_2_has_C = True

    if player_2_position % 20 == 18:
            print("Player 2 has D")
            player_2_has_D = True
    if player_2_position == player_1_position:
        player_2_position = player_2_position - 1
        player_2_has_A = False
        player_2_has_B = False
        player_2_has_C = False
        player_2_has_D = False
def is_game_over():
    """
    determines whether the game has ended.
    :return: True if a player has won, False if neither has.
    """
    # I've written this one for the basic game, but you may need to modify this for some improvements. - HH
    if player_1_has_A and player_1_has_B and player_1_has_C and player_1_has_D:
        return True
    if player_2_has_A and player_2_has_B and player_2_has_C and player_2_has_D:
        return True
    return False

def loop():
    """
    The main function that corresponds to a ply.
    :return: None
    """
    global whose_turn_is_it, game_is_still_playing # since this method may change these long-term variables
    if whose_turn_is_it == 1:
        player_1_ply()
        whose_turn_is_it = 2 #switch player
    else:
        player_2_ply()
        whose_turn_is_it = 1 #switch player
    if is_game_over():
        game_is_still_playing = False

def main():
    reset()
    while game_is_still_playing:
        loop()
    print ("Game Over.")
    print ("Sorry, Player {0}, you lost.".format(whose_turn_is_it))
# --------------------------  GAME STARTS HERE
main()