from cmu_graphics import *
from alphabet import alphabet

box1 = Rect(50, 300, 100, 100, fill="lightBlue")
box2 = Rect(150, 300, 100, 100, fill="lightGreen")
box3 = Rect(250, 300, 100, 100, fill="lightYellow")
letter1 = Label("G", 100, 350, size=60, font='Arial', bold=True, fill='black', align='center')
letter2 = Label("G", 200, 350, size=60, font='Arial', bold=True, fill='black', align='center')
letter3 = Label("G", 300, 350, size=60, font='Arial', bold=True, fill='black', align='center')
RightOrWrong = Circle(200, 50, 30, fill="gray")


Lettershown = Label("", 200, 200, size=100, font='Arial', bold=True, fill='black', align='center')


app.mouseXold = 0
app.mouseXolder = 0
app.mouseYold = 0
app.mouseYolder = 0
def onMousePress(mouseX, mouseY):

    print("before", mouseX, app.mouseXold, app.mouseXolder)
    if app.mouseXolder == mouseX:
        app.mouseXold = mouseX
    else:
        app.mouseXolder = app.mouseXold
        app.mouseXold = mouseX
    print("after", mouseX, app.mouseXold, app.mouseXolder)
    if app.mouseYolder == mouseY:
            app.mouseYold = mouseY
    else:
        app.mouseYolder = app.mouseYold
        app.mouseYold = mouseY


    Mainletter = randrange(0, 25)
    Lettershown.value = alphabet[Mainletter]

    letter1.value= alphabet[randrange(0, 25)]
    letter2.value= alphabet[randrange(0, 25)]
    letter3.value= alphabet[randrange(0, 25)]

    rand1to3 = randrange(1, 4)
    if rand1to3 == 1:
        letter1.value = alphabet[Mainletter-1].lower()
        if (box1.hits(app.mouseXolder, app.mouseYolder) == True):
            RightOrWrong.fill = "Green"
        else:
            RightOrWrong.fill = "Red"
    elif rand1to3 == 2:
        letter2.value = alphabet[Mainletter-1].lower()
        if (box2.hits(app.mouseXolder, app.mouseYolder) == True):
            RightOrWrong.fill = "Green"
        else:
            RightOrWrong.fill = "Red"
    elif rand1to3 == 3:
        letter3.value = alphabet[Mainletter-1].lower()
        if (box3.hits(app.mouseXolder, app.mouseYolder) == True):
            RightOrWrong.fill = "Green"
        else:
            RightOrWrong.fill = "Red"
    


cmu_graphics.run()