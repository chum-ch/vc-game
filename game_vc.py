import tkinter as tk
import random
# creating tkinter window 
root = tk.Tk() 
root.geometry("650x600")
canvas = tk.Canvas(root)
root.title("Game VC") 
# Creating Menu 
menu_file = tk.Menu(root) 
# Adding File Menu and sub file 
file = tk.Menu(menu_file, tearoff = 0)
menu_file.add_cascade(label ="File", menu = file)
# Adding "New level" inside of the file
file.add_command(label ="New level")
# Adding "Exit" inside of the file
file.add_command(label ="Exit", command = root.destroy) 


# CONSTANTS
SIZE = 40
index_of_one = 0
index_of_two = 0
count_posi_move = 0
player_across_posi = False
player_across_posi_with_box = False
# 0 gird
# 1 is firewall
# 2 person
# 3 the box
# 4 fit the positon
boradgame = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,2,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,1,1,1,1,1,1,0,0,1,1],
    [0,1,0,0,0,1,1,1,1,1,1,0,0,0,1],
    [0,1,0,1,0,1,0,0,0,0,1,0,3,0,1],
    [0,1,1,1,4,1,0,0,0,0,1,0,3,0,1],
    [0,0,0,1,4,1,0,0,0,0,1,0,3,0,1],
    [0,0,0,1,4,1,0,0,0,0,1,0,0,0,1],
    [0,0,0,1,1,1,0,0,0,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

]

# funciton 
def arrayToDrawing():
    global boradgame, index_of_one, index_of_two
    canvas.delete("all")
    for index1 in range (len(boradgame)):
        for index2 in range(len(boradgame[0])):
            x1=SIZE * index2
            y1=SIZE * index1
            x2=SIZE + x1
            y2=SIZE + y1
            if boradgame[index1][index2] == 1:
                canvas.create_image(x2, y2, image = v1_wall)
            elif boradgame[index1][index2] == 2:
                canvas.create_image(x2, y2, image = v1_person)
                index_of_two = index2
                index_of_one = index1
            elif boradgame[index1][index2] == 3:
                canvas.create_image(x2, y2, image = v1_push)
            elif boradgame[index1][index2] == 4:
                canvas.create_image(x2, y2, image = v1_position)
            else:
                canvas.create_image(x2, y2, image = v1_bg)

# player move right
def moveRight(event):
    global boradgame, index_of_one, index_of_two, player_across_posi, player_across_posi_with_box, count_posi_move
    if boradgame[index_of_one][index_of_two+1] == 0:
        index_of_two += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two-1] = 0

        #check player across 1 position
        if player_across_posi:
            boradgame[index_of_one][index_of_two-1] = 4
            player_across_posi = False

    # check player across 1 position and across 1 the box
    elif boradgame[index_of_one][index_of_two+2] == 4:
        index_of_two += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two+1] = 3
        boradgame[index_of_one][index_of_two-1] = 0
        player_across_posi_with_box = True

    # check player cannot move the box if there are 2 boxs and if have the wall
    elif boradgame[index_of_one][index_of_two+1] == 3 and boradgame[index_of_one][index_of_two+2] != 1 and boradgame[index_of_one][index_of_two+2] != 3:
        index_of_two += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two+1] = 3
        boradgame[index_of_one][index_of_two-1] = 0

        # check player across 1 position and across 1 the box
        if player_across_posi_with_box and boradgame[index_of_one][index_of_two+1] == 3:
            count_posi_move += 1
            if count_posi_move == 2:
                boradgame[index_of_one][index_of_two-1] = 4
                player_across_posi_with_box = False
                count_posi_move = 0

    #check player across 1 position
    elif boradgame[index_of_one][index_of_two+1] == 4:
        index_of_two += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two-1] = 0
        player_across_posi = True
    
    arrayToDrawing()

# player move left
def moveLeft(event):
    global boradgame, index_of_one, index_of_two, player_across_posi, player_across_posi_with_box, count_posi_move
    if boradgame[index_of_one][index_of_two-1] == 0:
        index_of_two -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two+1] = 0

        #check player across 1 position
        if player_across_posi:
            boradgame[index_of_one][index_of_two+1] = 4
            player_across_posi = False

    # check player across 1 position and across 1 the box
    elif boradgame[index_of_one][index_of_two-2] == 4:
        index_of_two -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two-1] = 3
        boradgame[index_of_one][index_of_two+1] = 0
        player_across_posi_with_box = True

    # check player cannot move the box if there are 2 boxs and if have the wall
    elif boradgame[index_of_one][index_of_two-1] == 3 and boradgame[index_of_one][index_of_two-2] != 1 and boradgame[index_of_one][index_of_two-2] != 3:
        index_of_two -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two-1] = 3
        boradgame[index_of_one][index_of_two+1] = 0

        # check player across 1 position and across 1 the box
        if player_across_posi_with_box and boradgame[index_of_one][index_of_two-1] == 3:
            count_posi_move += 1
            if count_posi_move == 2:
                boradgame[index_of_one][index_of_two+1] = 4
                player_across_posi_with_box = False
                count_posi_move = 0

    #check player across 1 position
    elif boradgame[index_of_one][index_of_two-1] == 4:
        index_of_two -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one][index_of_two+1] = 0
        player_across_posi = True
    arrayToDrawing()

# player move up
def moveUp(event):
    global boradgame, index_of_one, index_of_two, player_across_posi, player_across_posi_with_box, count_posi_move
    if boradgame[index_of_one-1][index_of_two] == 0:
        index_of_one -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one+1][index_of_two] = 0

        #check player across 1 position
        if player_across_posi:
            boradgame[index_of_one+1][index_of_two] = 4
            player_across_posi = False

    # check player across 1 position and across 1 the box
    elif boradgame[index_of_one-2][index_of_two] == 4:
        index_of_one -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one-1][index_of_two] = 3
        boradgame[index_of_one+1][index_of_two] = 0
        player_across_posi_with_box = True

    # check player cannot move the box if there are 2 boxs and if have the wall
    elif boradgame[index_of_one-1][index_of_two] == 3 and boradgame[index_of_one-2][index_of_two] != 1 and boradgame[index_of_one-2][index_of_two] != 3:
        index_of_one -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one-1][index_of_two] = 3
        boradgame[index_of_one+1][index_of_two] = 0

        # check player across 1 position and across 1 the box
        if player_across_posi_with_box and boradgame[index_of_one-1][index_of_two] == 3:
            count_posi_move += 1
            if count_posi_move == 2:
                boradgame[index_of_one+1][index_of_two] = 4
                player_across_posi_with_box = False
                count_posi_move = 0

    #check player across 1 position
    elif boradgame[index_of_one-1][index_of_two] == 4:
        index_of_one -= 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one+1][index_of_two] = 0
        player_across_posi = True
    arrayToDrawing()

def moveDown(event):
    global boradgame, index_of_one, index_of_two, player_across_posi, player_across_posi_with_box, count_posi_move
    if boradgame[index_of_one+1][index_of_two] == 0:
        index_of_one += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one-1][index_of_two] = 0

        #check player across 1 position
        if player_across_posi:
            boradgame[index_of_one-1][index_of_two] = 4
            player_across_posi = False

    # check player across 1 position and across 1 the box
    elif boradgame[index_of_one+2][index_of_two] == 4:
        index_of_one += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one+1][index_of_two] = 3
        boradgame[index_of_one-1][index_of_two] = 0
        player_across_posi_with_box = True

    # check player cannot move the box if there are 2 boxs and if have the wall
    elif boradgame[index_of_one+1][index_of_two] == 3 and boradgame[index_of_one+2][index_of_two] != 1 and boradgame[index_of_one+2][index_of_two] != 3:
        index_of_one += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one+1][index_of_two] = 3
        boradgame[index_of_one-1][index_of_two] = 0

        # check player across 1 position and across 1 the box
        if player_across_posi_with_box and boradgame[index_of_one+1][index_of_two] == 3:
            count_posi_move += 1
            if count_posi_move == 2:
                boradgame[index_of_one-1][index_of_two] = 4
                player_across_posi_with_box = False
                count_posi_move = 0

    #check player across 1 position
    elif boradgame[index_of_one+1][index_of_two] == 4:
        index_of_one += 1
        boradgame[index_of_one][index_of_two] = 2
        boradgame[index_of_one-1][index_of_two] = 0
        player_across_posi = True

    arrayToDrawing()

 # adding image 
v1_bg = tk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\vc-game\\img\\v1-bg.png")
v1_wall = tk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\vc-game\\img\\v1-wall.png")
v1_person = tk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\vc-game\\img\\v1-person.png")
v1_push = tk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\vc-game\\img\\v1-push.png")
v1_position = tk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\vc-game\\img\\v1-position.png")
arrayToDrawing()

root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
canvas.pack(expand=True, fill='both')
# display Menu 
root.config(menu = menu_file) 
root.mainloop()