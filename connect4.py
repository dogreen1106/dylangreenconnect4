def request_input(grid, player):
    try:
        col = input(f"Player {player}, choose a column (1-7): ")
        col = int(col)
        if col < 1 or col > 7:
            return -1
        col -= 1
        for row in range(5, -1, -1):
            if grid[row][col] == '':
                return (row + 1, col + 1)
        return -2
    except ValueError:
        return -1

def make_move(grid, row, column, player):
    grid[row - 1][column - 1] = player
    return grid

def check_row(grid, player):
    for row in grid:
        count = 0
        for cell in row:
            count = count + 1 if cell == player else 0
            if count == 4:
                return True
    return False

def check_column(grid, player):
    for col in range(7):
        count = 0
        for row in range(6):
            count = count + 1 if grid[row][col] == player else 0
            if count == 4:
                return True
    return False

def check_diag(grid, player):
    for row in range(3):
        for col in range(4):
            if (grid[row][col] == player and
                grid[row+1][col+1] == player and
                grid[row+2][col+2] == player and
                grid[row+3][col+3] == player):
                return True
    for row in range(3, 6):
        for col in range(4):
            if (grid[row][col] == player and
                grid[row-1][col+1] == player and
                grid[row-2][col+2] == player and
                grid[row-3][col+3] == player):
                return True
    return False

def is_draw(grid):
    for row in grid:
        for cell in row:
            if cell == '':
                return False
    return True

def display_grid(grid):
    for row in grid:
        cells = []
        for cell in row:
            if cell == '':
                cells.append('  ') 
            else:
                cells.append(f' {cell} ')  
        line = '|' + '|'.join(cells) + '|'
        print(line)
        print('+-----------------------------+')

def play_game(grid):
    current_player = 'X'
    display_grid(grid)
    while True:
        move = request_input(grid, current_player)
        if move == -1:
            print("Invalid Response")
            continue
        elif move == -2:
            print("Column you selected has no empty slots.")
            continue
        row, col = move
        make_move(grid, row, col, current_player)
        display_grid(grid)
        if (check_row(grid, current_player) or
            check_column(grid, current_player) or
            check_diag(grid, current_player)):
            print(f"Congratulations! Player {current_player} won.")
            return
        if is_draw(grid):
            print("Game is a draw")
            return
        current_player = 'O' if current_player == 'X' else 'X'
        
