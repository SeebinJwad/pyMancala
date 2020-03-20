# TODO MAKE THE SECOND LOOP FOR CURR POS
def move(board_top, board_btm, score_top, score_btm, piece):
    # <= because input is 1 2 3 4 5 6 inclusive
    double_move = False
    piece = int(piece)
    if piece <= 6:
        total = board_top[piece - 1]
        curr_pos = piece
        for x in range(total):
            curr_pos -= 1
            if curr_pos == 0:
                score_top += 1
                # print(total - x)
            elif curr_pos < 0:
                print(curr_pos)
                board_btm[(curr_pos + 1) * -1] += 1
            else:
                board_top[curr_pos - 1] += 1
            if total - x == 0:
                double_move = True
            # print(curr_pos)
        board_top[piece - 1] = 0
    else:
        total = board_btm[piece - 7]
        curr_pos = piece - 7
        for x in range(total):
            curr_pos += 1
            if curr_pos == 6:
                score_btm += 1
            elif curr_pos > 6:
                board_top[(curr_pos-6) * -1] += 1
            else:
                board_btm[curr_pos] += 1

            if total - x == 0:
                double_move = True
            print(curr_pos)
        board_btm[piece - 7] = 0
    return board_top, board_btm, score_top, score_btm, double_move


def check_winner(board_top, board_btm, score_top, score_btm):
    # check if board_top is empty or board_btm is empty, by adding all values
    total_top = 0
    total_btm = 0

    for x in board_top:
        total_top += x

    for x in board_top:
        total_btm += x

    if total_btm == 0 or total_top == 0:

        if total_btm + score_btm > total_top + score_top:
            print("BOTTOM WON")
        else:
            print("TOP WON")

    repeat = input("play again? y/n")

    if repeat == 'n':
        quit()
    else:
        gameLoop()


def gameLoop():

    gameOver = False

    board_top = [4, 4, 4, 4, 4, 4]
    board_btm = [4, 4, 4, 4, 4, 4]

    score_top = 0
    score_btm = 0

    print(board_top)
    print(board_btm)

    print("Score Top: " + str(score_top))
    print("Score Bottom: " + str(score_btm))

    turn = "top"

    while not gameOver:
        corr_selection = False
        selection = int(input("\nWhich piece would you like to push? "))
        # if selection is less than 6 and move is top, then run everything underneath, result and prints
        corr_selection = (selection < 7 and turn == "top") or (selection >= 7 and turn == "btm")
        if corr_selection:

            result = move(board_top, board_btm, score_top, score_btm, selection)

            board_top = result[0]
            board_btm = result[1]

            score_top = result[2]
            score_btm = result[3]

            double_move = result[4]
            print(double_move)
            print(board_top)
            print(board_btm)

            print("Score Top: " + str(score_top))
            print("Score Bottom: " + str(score_btm))

            if not double_move:
                if turn == "top":
                    turn = "btm"
                else:
                    turn = "top"
                double_move = False


gameLoop()
