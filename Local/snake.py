import curses

field = [[0 for i in range(12)] for j in range(12)]
# start in the middle of the field
snake = [[6,6]]
exit = False
food_on_field = False
while exit is False:
    # draw the field 12x12 chars
    for i in range(12):
        for j in range(12):
            if [i,j] in snake:
                field[i][j] = 1
            else:
                field[i][j] = 0
    # if there is no food on the field, place one
    if food_on_field is False:
        food_on_field = True
        food = [random.randint(0,11),random.randint(0,11)]
        while food in snake:
            food = [random.randint(0,11),random.randint(0,11)]
    # draw the field, snake and food
    # food is a F, snake is a S and empty space is a dot
    for i in range(12):
        for j in range(12):
            if field[i][j] == 1:
                stdscr.addstr(i,j,"S")
            elif food == [i,j]:
                stdscr.addstr(i,j,"F")
            else:
                stdscr.addstr(i,j,".")
    
    