#glabal variables
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#game_on = True
move_count = 0
player_dict = {'X':'Player 1', 'O':'Player 2'}

def print_board():
    count = 0
    for i in board:
        print('|'.join(i))
        if count != 2:
            print('-'*6)
            count += 1

def is_over(player, x, y):
    player = player.upper()
    #checking columns
    for i in range(3):
        if board[x][i] != player:
            break
        if i == 2:
            print(player_dict[player]+" won the game")
            return True    
    #checking rows
    for i in range(3):
        if board[i][y] != player:
            break
        if i == 2:
            print(player_dict[player]+" won the game")
            return True
    #checking diagnol
    if x == y:
        for i in range(3):
            if board[i][i] != player:
                break
            if i == 2:
                print(player_dict[player]+" won the game")
                return True
    #checking antidiagnol
    if x+y == 2:
        for i in range(3):
            if board[i][2-i] != player:
                break
            if i == 2:
                print(player_dict[player]+" won the game")
                return True


if __name__ == "__main__":
    print('Player one will use "X" and player two will use "O" ')
    print('Initial board\n')
    print_board()
    while True:
        #player 1 is playing
        player1 = True
        while player1:
            try:
                pos = int(input("Player 1 enter the position:"))
            except ValueError:
                print("Please enter valid position ")
                continue
            if pos == 3:
                row = 0
            elif pos == 6:
                row = 1
            elif pos == 9:
                row = 2
            else:
                row = pos//3
            if pos == 3 or pos == 6 or pos == 9:
                col = 2
            else:
                col = pos%3-1
            if board[row][col] != ' ':
                print("Invalid position ")
                continue
            board[row][col] = 'X'
            print_board()
            move_count += 1
            player1 = False
        if is_over('X', row, col):
            break
        if move_count == 9:
            print_board()
            print('It\'s a draw ')
            break
            
        #player 2 is playing
        player2 = True
        while player2:
            try:
                pos = int(input("Player 2 enter the position:"))
            except ValueError:
                print("Please enter valid position ")
                continue
            if pos == 3:
                row = 0
            elif pos == 6:
                row = 1
            elif pos == 9:
                row = 2
            else:
                row = pos//3
            if pos == 3 or pos == 6 or pos == 9:
                col = 2
            else:
                col = pos%3-1
            if board[row][col] != ' ':
                print("Invalid position ")
                continue
            board[row][col] = 'O'
            print_board()
            move_count += 1
            player2 = False
        if is_over('O', row, col):
            break
        if move_count == 9:
            print_board()
            print('It\'s a draw ')
            break
    print("Thanks for playing the game ")

