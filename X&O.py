
field = ["_","_","_",
         "_","_","_",
         "_","_","_"]

turns = 0

def x_input():
    global turns
    position = (input("X: Choose the cell: "))
    if position.isdigit() == True:
        position = int(position) - 1
        if position in range(0,9):
            if field[position] in ["x","o"]:
                print("This cell was already taken, try another one")
                x_input()
            else:
                field[position] = 'x'
                turns += 1
        else:
            print("This cell is out of range, try another one")
            x_input()
    else:
        print('Cell should be a number')
        x_input()
    
def o_input():
    global turns
    position = (input("O: Choose the cell: "))
    if position.isdigit() == True:
        position = int(position) - 1
        if position in range(0,9):
            if field[position] in ["x","o"]:
                print("This cell was already taken, try another one")
                x_input()
            else:
                field[position] = 'o'
                turns += 1
        else:
            print("This cell is out of range, try another one")
            o_input()
    else:
        print('Cell should be a number')
        o_input


def up(a,b,c):
    field[a] = field[a].upper()
    field[b] = field[b].upper()
    field[c] = field[c].upper()
    
def check_horizontal(symbol):
    if field[0] == field[1] == field[2] == symbol:
        up(0,1,2)
        return True
    elif field[3] == field[4] == field[5] == symbol:
        up(3,4,5)
        return True
    elif field[6] == field[7] == field[8] == symbol:
        up(6,7,8)
        return True

def check_vertical(symbol):
    if field[0] == field[3] == field[6] == symbol:
        up(0,3,6)
        return True
    elif field[1] == field[4] == field[7] == symbol:
        up(1,4,7)
        return True
    elif field[2] == field[5] == field[8] == symbol:
        up(2,5,8)
        return True
        
def check_askance(symbol):
    if field[0] == field[4] == field[8] == symbol:
        up(0,4,8)
        return True
    elif field[2] == field[4] == field[6] == symbol:
        up(2,4,6)
        return True

def win_check(symbol):
    if check_horizontal(symbol) or check_vertical(symbol) or check_askance(symbol) == True:
        print(f"Congrats, {symbol} wins")
        return True
    else:
        return False

def field_view():
    for a in range(3):
        print()
        for i in range(a*3,a*3+3):
            print(field[i], end=' ')
    print()

while True:
    x_input()
    field_view()
    if win_check("x") == True:
        break
    if turns == 9:
        if win_check("x") == True:
            break
        if win_check("o") == True:
            break
        print("It's a tie")
        break
    o_input()
    field_view()
    if win_check("o") == True:
        break
field_view()