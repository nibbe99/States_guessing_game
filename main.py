import pandas
from turtle import Turtle, Screen

readData = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"
allStates = readData["state"]

correct = 0
correctStates = []

def guess(getInput):

    exist = (readData[allStates == getInput])
    onlyStates = readData["state"].tolist()

    print(onlyStates)
    global correct
    l1 = len(exist)
    if l1 > 0 and not correctStates.__contains__(getInput):
        print("MY CORRECT STATES:", correctStates)
        print(f"{getInput} exists")
        print(exist)
        xcor = exist["x"]
        ycor = exist["y"]
        valueOfx = xcor.max()
        valueOfY = ycor.max()
        t1 = Turtle()
        t1.goto(valueOfx, valueOfY)
        t1.write(getInput)
        correct+=1

    else:
        print(f"{getInput} does not exist")

    correctStates.append(getInput)

s = Screen()

print(readData["x"].max())

s.addshape(image)

t = Turtle()
t.shape(image)

s.title("Usa states games")

gameIsOn = True

while gameIsOn:
    getInput = s.textinput(f"{correct+1} / {len(allStates)}", "What is another states name?")

    print(getInput)
    guess(getInput)






s.listen()
s.mainloop()