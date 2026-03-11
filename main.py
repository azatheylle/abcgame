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

app.rand1to3 = 0

def onMousePress(mouseX, mouseY):

    if app.rand1to3 == 1:
        if (box1.hits(mouseX, mouseY) == True):
            RightOrWrong.fill = "Green"
        else:
            RightOrWrong.fill = "Red"
    elif app.rand1to3 == 2:
        if (box2.hits(mouseX, mouseY) == True):
            RightOrWrong.fill = "Green"
        else:
            RightOrWrong.fill = "Red"
    elif app.rand1to3 == 3:
        if (box3.hits(mouseX, mouseY) == True):
            RightOrWrong.fill = "Green"
        else:
            RightOrWrong.fill = "Red"
    else:
        pass

def onMouseRelease(mouseX, mouseY):

    Mainletter = randrange(0, 25)
    Lettershown.value = alphabet[Mainletter]

    letter1.value= alphabet[randrange(0, 25)]
    letter2.value= alphabet[randrange(0, 25)]
    letter3.value= alphabet[randrange(0, 25)]

    app.rand1to3 = randrange(1, 4)
    if app.rand1to3 == 1:
        letter1.value = alphabet[Mainletter-1]
    elif app.rand1to3 == 2:
        letter2.value = alphabet[Mainletter-1]
    elif app.rand1to3 == 3:
        letter3.value = alphabet[Mainletter-1]

cmu_graphics.run()