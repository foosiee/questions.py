import turtle
import matplotlib.pyplot as plt

lines = []
noAnswer = []
answer = []
totalQ_day = []
days = []

def update():

    global lines
    global noAnswer
    global answer
    global totalQ_day
    global days

    lines = []
    noAnswer = []
    answer = []
    totalQ_day = []
    days = []
    
    f = open("save.txt","r")
    fl = f.readlines()

    for x in fl:
        lines.append(x)
        
    days_count = 0    
    i = 0
    while i < len(lines):
        if lines[i] == "new\n":
            noAnswer.append(int(lines[i+1]))
            answer.append(int(lines[i+2]))
            days_count+=1
            days.append(days_count)
            t = int(lines[i+1]) + int(lines[i+2])
            totalQ_day.append(t)
        i+=3
    f.close()

    
def stop():
    print("Ending program")
    loop = False
    return loop

def helper():
    commands = ["stop","exit","days","totalqs","noanswer","answer","percent",
                "graphno","graphansw","line","pie","avg"]
    print("List of commands: ")
    for x in range(len(commands)):
        print(commands[x])
    print(" ")

def addQs(theList):
    q = 0
    for x in range(len(theList)):
        q+=theList[x]
    return q

def addDays(a,b):
    q = a + b
    return q

def percentage(a,b):
    p = (a / b)*100
    return p

def dayTracker():
     for day in range(len(noAnswer)):
         total_for_day = addDays(noAnswer[day],answer[day])
         percent = percentage(answer[day],total_for_day)
         print("Day", day+1)
         print("Unaswered questions:", noAnswer[day])
         print("Answered questions:", answer[day])
         print("Percentage: ", percent,"%")
         print("")

def responses(theList):
    num_days = len(theList)
    total = 0
    for x in range(num_days):
        t = theList[x]
        total += t
    return total

def totalQ():
    num_days = len(noAnswer)
    total_q = 0
    for x in range(num_days):
        t = addDays(noAnswer[x],answer[x])
        total_q += t
    return total_q

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 

def barSetup(theList):
    border = 10
    maxheight = max(theList)
    numbars = len(theList)

    wn = turtle.Screen()             
    wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           
    tess.color("black")
    tess.fillcolor("white")
    tess.pensize(3)

    for a in theList:
        drawBar(tess, a)

    wn.exitonclick()

def linegraph():
    plt.plot(days,noAnswer,color='r',label="noAnswer")
    plt.plot(days,answer,color='g',label="Answers")
    plt.plot(days,totalQ_day, color ='b', label="# of Questions")
    plt.xlabel('Days')
    plt.ylabel('# of responses')
    plt.axis([0,7,0,max(answer)*1.5])
    plt.title("Answer or No Answer Graph")
    plt.legend(loc='upper left')
    plt.show()

def piechart():
    labels = 'Unanswered', 'Answered'
    sizes = [percentage(addQs(noAnswer),totalQ()),percentage(addQs(answer),totalQ())]
    explode = (0.1,0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

def average():
    num_days = len(noAnswer)
    q1 = addQs(noAnswer)
    q2 = addQs(answer)

    avg1 = q1/num_days
    avg2 = q2/num_days

    print("Average number of unanswered questions:",avg1)
    print("Average number of answered questions:",avg2)
    print("")
    
    

loop = True
while loop == True:
    update()
    print("For list of commands enter: \"help\"")
    user_input = input("Enter a command: ")
    print("")
    user_input = user_input.lower()


    if user_input == "help":
        helper()
    elif user_input == "exit":
        loop = stop()
    elif user_input == "days":
        dayTracker()
    elif user_input == "totalqs":
        print("cole asked",totalQ(),"questions in",len(noAnswer),"days\n")
    elif user_input == "noanswer":
        print("ayana didn't answer",responses(noAnswer),"of coles",totalQ() ,"questions in",len(noAnswer),"days\n")
    elif user_input == "answer":
        print("ayana answered",responses(answer),"of coles",totalQ() ,"questions in",len(noAnswer),"days\n")
    elif user_input == "percent":
        print("ayana answered",percentage(responses(answer),totalQ()),"% of coles questions\n")
    elif user_input == "graphno":
        barSetup(noAnswer)
    elif user_input == "graphansw":
        barSetup(answer)
    elif user_input == "line":
        linegraph()
    elif user_input == "pie":
        piechart()
    elif user_input == "avg":
        average()
    else:
        print(user_input," is not a valid command\n")











        
