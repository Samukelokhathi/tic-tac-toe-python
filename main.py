from tkinter import *
from tkinter import messagebox




currentPlayer="x"

winPositions=[[1,2,3],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7],[4,5,6],[7,8,9]]
buttons = []

def btn_clicked(position,btn):
    global positions , currentPlayer, buttons

    for pos in positions:
        # print(pos)  This line gonna print positions of a variable as dictionary not as a list.
        if pos["position"]==position:
            # print(pos) This line print clicked position
            if pos["player"]!='':
                print('Already clicked idiot') # This if statement prevent changes once button has been clicked.
                return # It return nothing if the button has been clicked.
            pos["player"]=currentPlayer
            # print(pos) #This line print assigned currentPlayer from an empty string player
            buttons.append(btn)
            # print(buttons)
            btn.config(text=currentPlayer) #This line changes button text from '' to current player(x/o)
            # print(btn)
            check_if_won()


    if currentPlayer=="x":
        currentPlayer="o"
        # print(currentPlayer,'assigned') This print a vise versa.
    else:
        currentPlayer="x"
        # print(currentPlayer,'assigned') This print a vise versa.

    label.config(text=f"{currentPlayer}'s turn") # This line show whose turn is it.



def check_if_won():
    global currentPlayer, winPositions, positions,buttons
    xpos=[]
    ypos=[]

    for pos in positions:
        # print(pos) #This line gonna print positions of a variable as dictionary not as a list.
        if pos["player"]=="x" :
            # print(pos) This line print X position appearance
            xpos.append(pos["position"])
            # print(xpos)  # This line print added X position appearance in a list.

        if pos["player"]=="o":
            # print(pos)  #This line print O position appearance.
            ypos.append(pos["position"])
            # print(ypos) # This line print added O position appearance in a list.


    if currentPlayer=="x":
        for win in winPositions:
            # print(win) #This line print every element of a list that represent possible wins.
            if win[0] not in xpos: # Checks if there is first index clicked
                # print(win[0]) # This line prints every first index in every elements.
                continue # If first index is not found jump to the next element.
            if win[1] not in xpos: # Checks if there is second  index is been clicked only if the first one is available.
                continue # If first index is found jump to second index.If this second index is not found than skip to another element
            if win[2] in xpos: # If 1st and 2nd index are found that a win
                print("X has won")

                highlight(win) # This highlight buttons to green if X won

                messagebox.showinfo('tik, tac, toe', 'X has won')

                restart()
                break



    if currentPlayer=="o":
        for win in winPositions:
            if win[0] not in ypos:
                continue
            if win[1] not in ypos:
                continue
            if win[2] in ypos:
                print("O has won")

                highlight(win)
                messagebox.showinfo('tik tac toe','O has won')

                restart()
                break

    if all(pos['player'] != '' for pos in positions):
            print('draw')
            messagebox.showinfo('tik tak toe',"it's a Draw")
            restart()





def highlight(win):
    global positions

    for pos in positions:
        # print(pos) #Print all positions
        if pos['position'] in win:
            # print(pos) #Print win position of current player
            pos['btn'].config(bg='green')
            print(pos,'button changed')



def restart():
    global positions, buttons
    for pos in positions:
        pos["player"] = ''

    for btn in buttons:
        btn.config(text='',bg='grey')


window = Tk()
window.title("Tik Tac Toe")
window.geometry('200x250')




btn1 = Button(window, text=' ', height=3, width=6, bg= 'grey', command=lambda : btn_clicked(1,btn1))
btn1.grid(row=0, column=0)

btn2 = Button(window, text=' ', height=3, width=6, bg= 'grey',command=lambda : btn_clicked(2,btn2))
btn2.grid(row=0, column=1)

btn3 = Button(window, text=' ', height=3, width=6, bg= 'grey',command=lambda : btn_clicked(3,btn3))
btn3.grid(row=0, column=2)


btn4 = Button(window, text=' ', height=3, width=6,bg= 'grey', command=lambda : btn_clicked(4,btn4))
btn4.grid(row=1, column=0)

btn5 = Button(window, text=' ', height=3, width=6, bg= 'grey',command=lambda : btn_clicked(5,btn5))
btn5.grid(row=1, column=1)

btn6 = Button(window, text=' ', height=3, width=6, bg= 'grey',command=lambda : btn_clicked(6,btn6))
btn6.grid(row=1, column=2)

btn7 = Button(window, text=' ', height=3, width=6,bg= 'grey', command=lambda : btn_clicked(7,btn7))
btn7.grid(row=2, column=0)

btn8 = Button(window, text=' ', height=3, width=6,bg= 'grey', command=lambda : btn_clicked(8,btn8))
btn8.grid(row=2, column=1)

btn9 = Button(window, text=' ', height=3, width=6, bg= 'grey',command=lambda : btn_clicked(9,btn9))
btn9.grid(row=2, column=2)

positions=[{"position": 1,"player":"",'btn':btn1},{"position": 2,"player":"",'btn':btn2},{"position": 3,"player":"",'btn':btn3},
           {"position": 4,"player":"",'btn':btn4},{"position": 5,"player":"",'btn':btn5},{"position": 6,"player":"",'btn':btn6},
           {"position": 7,"player":"",'btn':btn7},{"position": 8,"player":"",'btn':btn8},{"position": 9,"player":"",'btn':btn9}]



label = Label(window,text=f"{currentPlayer}'s turn")
label.grid(row=4, column=0)

restart()
Button(window, text='Restart',command=restart).grid(row=4, column=1)




window.mainloop()
