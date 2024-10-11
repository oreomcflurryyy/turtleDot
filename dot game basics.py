import turtle
import math
import datetime


#diagonal lines or double dots ommnitted
#home screen setup

dot_list = []                      #used for storing board dots coordinates
count_list = []                    #used for storing coordinates in drawing
turn = "red"
turn_list = []                     #order of turns
flag = []
d = []                             #list in format of [[x1, y1], [x2, y2]]
k = 0                              #board type value
dict_sq = {}                       #dictionary in format {(x,y): [ur, ul, dr, dl} to check validity

score_A = 0
score_B = 0
id_name1 = ""
id_name2 = ""



def gen_dot(k):
    
    global dict_sq
    
    turtle.penup()
    turtle.speed(0)
    turtle.setpos((-k//2+1)*50,(k//2)*50)
    
    for i in range (1,k+1):
        for j in range (1,k+1):
            dot_list.append(turtle.pos())
            x, y = turtle.pos()
            dict_sq[(round(x), round(y))] = []
            turtle.dot(15, "black")
            if j == k:
                continue
            else:
                turtle.fd(50)
        turtle.seth(270)
        turtle.fd(50)
        if i%2 == 1:
            turtle.seth(180)
        else:
            turtle.seth(0)

    print("list of dots succcessful....")
            
    print(dot_list)
    print("dict ... ", dict_sq)



def players():
    global id_name1
    global id_name2
    
    p = turtle.Screen()

    id_name1 = p.textinput("Player 1", "Enter a name")
    g1 = p.textinput("Gender of player 1", "M/F")
    g1 = g1.upper()

    id_name2 = p.textinput("Player 2", "Enter a name")
    g2 = p.textinput("Gender of player 2", "M/F")
    g2 = g2.upper()
            
    screen_appearance()



def screen_appearance():
    p = turtle.Turtle()
    p.up()
    p.ht()
    p.speed(0)
    p.setpos(0,270)
    
    p.write("DOT GAME", align = 'center', font = ("COPPERPLATE GOTHIC LIGHT", 35, "normal"))



def draw_line(p1, p2, colour):
    turtle.up()
    turtle.ht()
    turtle.color(colour)
    turtle.pensize(3)
    turtle.goto(p1)
    turtle.down()
    turtle.goto(p2)



def gameplay(x,y):
    l = 600
    p = []
    global turn
    global flag

    for i in range(len(dot_list)):
        dist = math.sqrt((dot_list[i][0]-x)**2 + (dot_list[i][1]-y)**2)
        if dist <= l:
            l = dist
            xcord = round(dot_list[i][0])
            ycord = round(dot_list[i][1])
            p = list([xcord, ycord])

    print ("p = ",p)
    
    count_list.append(p)
    flag.append(p)
    n = len(count_list)
   
    if n >= 2 and n%2 == 0:

        d.append(flag)
        length = len(d)-1
        x1, y1 = d[length][0]
        x2, y2 = d[length][1]

        #checking for marking at same coordinate twice
        if d[length][0] == d[length][1]:
            d[length][1] = [x1+50, y1]
            count_list[n-1] = [x1+50, y1]
            print("Error, automated changes made...")

        #checking for marking too far away in x-axis
        if x2 > x1+50 and (y2 == y1 or y2 == y1+50 or y2 == y1-50):
            d[length][1] = [x1+50, y1]
            count_list[n-1] = [x1+50, y1]
            print("Error, automated changes made...")
        if x2 < x1-50 and (y1 == y2 or y2 == y1+50 or y2 == y1-50):
            d[length][1] = [x1-50, y1]
            count_list[n-1] = [x1-50, y1]
            print("Error, automated changes made...")

        #checking for marking too far away in y-axis
        if y2 > y1+50 and (x2 == x1 or x2 == x1+50 or x2 == x1-50):
            d[length][1] = [x1, y1+50]
            count_list[n-1] = [x1, y1+50]
            print("Error, automated changes made...")
        if y2 < y1-50 and (x1 == x2 or x2 == x1+50 or x2 == x1-50):
            d[length][1] = [x1, y1-50]
            count_list[n-1] = [x1, y1-50]
            print("Error, automated changes made...")

        #checking for marking too far away in both axes
        if x2 > x1+50 and (y2 > y1+50 or y2 < y1-50):
            d[length][1] = [x1+50, y1]
            count_list[n-1] = [x1+50, y1]
            print("Error, automated changes made...")
        if x2 < x1-50 and (y2 < y1-50 or y2 > y1+50):
            d[length][1] = [x1-50, y1]
            count_list[n-1] = [x1-50, y1]
            print("Error, automated changes made...")
        
        #checking for marking diagonals
        if (x2 == x1+50 and y2 == y1+50) or (x2 == x1+50 and y2 == y1-50):
            d[length][1] = [x2, y1]
            count_list[n-1] = [x2, y1]
            print("Error, automated changes made...")
        elif (x2 == x1-50 and y2 == y1-50) or (x2 == x1-50 and y2 == y1+50):
            d[length][1] = [x2, y1]
            count_list[n-1] = [x2, y1]
            print("Error, automated changes made...")
        else:
            print("No Error found...")
            
    
        print("list of coordinates moved = ", d)
        
        flag = []

        turn_list.append(turn)
        draw_line(count_list[n-1], count_list[n-2], turn)

        print("last turn = ",p)
        
        play(d, turn_list, p)

        print("A = ", score_A, "B = ", score_B, k)

        #checking when the game is finished
        if (score_A + score_B) == (k-1)**2:
            result()



def result():
    win = ""
    turtle.reset()
    bt = ""
    global id_name1
    global id_name2

    if k == 5:
        bt = "5X5"
    elif k == 7:
        bt = "7X7"
    else:
        bt = "9X9"

    print(id_name1, id_name2)
    
    if score_A > score_B:
        win = "RED"
        
    elif score_A < score_B:
        win = "BLUE"
        
    else:
        win = "NO ONE"
        
    turtle.ht()
    if win != "NO ONE":
        turtle.write("GAME OVER!!! %s WINS!!!"%(win,), align = "center", font = ("Century Gothic", 50, "normal")) 
    else:
        turtle.write("GAME OVER!!! IT IS A DRAW", align = "center", font = ("Century Gothic", 50, "normal"))
        
    
        
def play(c, colour, last_turn):

    print("entered checking successfully...")

    global turn
    global score_A
    global score_B
    
    x, y = last_turn
    shape_type = "none"

    if 1 not in dict_sq[(x,y)] and ([[x,y],[x+50,y]] in c or [[x+50,y],[x,y]] in c) and ([[x+50,y+50],[x+50,y]] in c or [[x+50,y],[x+50,y+50]] in c) and ([[x,y+50],[x+50,y+50]] in c or [[x+50,y+50],[x,y+50]] in c) and ([[x,y+50],[x,y]] in c or [[x,y],[x,y+50]] in c):
        shape_type = "square up-right"
        dict_sq[(x,y)].append(1)
        dict_sq[(x+50,y)].append(2)
        dict_sq[(x,y+50)].append(3)
        dict_sq[(x+50,y+50)].append(4)
        print(1)

    if 2 not in dict_sq[(x,y)] and ([[x,y],[x-50,y]] in c or [[x-50,y],[x,y]] in c) and ([[x-50,y+50],[x-50,y]] in c or [[x-50,y],[x-50,y+50]] in c) and ([[x,y+50],[x-50,y+50]] in c or [[x-50,y+50],[x,y+50]] in c) and ([[x,y+50],[x,y]] in c or [[x,y],[x,y+50]] in c):
        shape_type = "square up-left"
        dict_sq[(x,y)].append(2)
        dict_sq[(x-50,y)].append(1)
        dict_sq[(x,y+50)].append(4)
        dict_sq[(x-50,y+50)].append(3)
        print(2)
    
    if 3 not in dict_sq[(x,y)] and ([[x,y],[x+50,y]] in c or [[x+50,y],[x,y]] in c) and ([[x+50,y-50],[x+50,y]] in c or [[x+50,y],[x+50,y-50]] in c) and ([[x,y-50],[x+50,y-50]] in c or [[x+50,y-50],[x,y-50]] in c) and ([[x,y-50],[x,y]] in c or [[x,y],[x,y-50]] in c):
        shape_type = "square down-right"
        dict_sq[(x,y)].append(3)
        dict_sq[(x+50,y)].append(4)
        dict_sq[(x,y-50)].append(1)
        dict_sq[(x+50,y-50)].append(2)
        print(3)

    if 4 not in dict_sq[(x,y)] and ([[x,y],[x-50,y]] in c or [[x-50,y],[x,y]] in c) and ([[x-50,y-50],[x-50,y]] in c or [[x-50,y],[x-50,y-50]] in c) and ([[x,y-50],[x-50,y-50]] in c or [[x-50,y-50],[x,y-50]] in c) and ([[x,y-50],[x,y]] in c or [[x,y],[x,y-50]] in c):
        shape_type = "square down-left"
        dict_sq[(x,y)].append(4)
        dict_sq[(x-50,y)].append(3)
        dict_sq[(x,y-50)].append(2)
        dict_sq[(x-50,y-50)].append(1)
        print(4)

    print("shape =", shape_type)
    
    if shape_type != "none":
        if turn == "red":
            score_A += 1
        else:
            score_B += 1
        turn = notchange_colour(turn)
        filling_play(shape_type, colour, last_turn)
        print(908654)
    else:
        turn = change_colour(turn)
        print(907777)


        
def notchange_colour(a):
    if a == "blue":
        return "blue"
    else:
        return "red"



def change_colour(a):
    if a == "blue":
        return "red"
    else:
        return "blue"



def filling_play(p, colour, lturn):

    print("hello filling here....")
    
    t = turtle.Turtle()
    t.up()
    t.ht()
    t.goto(lturn)

    col = colour[len(colour)-1]
    if col == "red":
        st = "#fcc7c7"
    else:
        st = "#c7d6fc"

    
    t.begin_fill()
    
    t.color("black", st)
    if p == "square up-right":
        t.seth(0)
        t.fd(50)
        t.seth(90)
        t.fd(50)
        t.seth(180)
        t.fd(50)
        t.seth(270)
        t.fd(50)
        
    if p == "square up-left":
        t.seth(180)
        t.fd(50)
        t.seth(90)
        t.fd(50)
        t.seth(0)
        t.fd(50)
        t.seth(270)
        t.fd(50)
        
    if p == "square down-right":
        t.seth(0)
        t.fd(50)
        t.seth(270)
        t.fd(50)
        t.seth(180)
        t.fd(50)
        t.seth(90)
        t.fd(50)
        
    if p == "square down-left":
        t.seth(180)
        t.fd(50)
        t.seth(270)
        t.fd(50)
        t.seth(0)
        t.fd(50)
        t.seth(90)
        t.fd(50)
        
    t.end_fill() 



def new_game():
    global k
    
    while True:
        num = int(input("Give your choice of board :  1) 5X5  2) 7X7  3) 9X9\nInput : "))
        if num == 1 or num == 5:
            k = 5
            break
        elif num == 2 or num == 7:
            k = 7
            break
        elif num == 3 or num == 9:
            k = 9
            break
        else:
            print("Invalid input...")
    gen_dot(k)
    players()
    


new_game()    
sc = turtle.Screen()

sc.listen()
sc.onkey(turtle.undo, "k")
sc.onkey(turtle.bye, "space")
sc.onclick(gameplay)

turtle.mainloop()

    
        
             

