lifelines = ["50-50", "flip question", "50-50", "flip question"]

def remaininglifelines():
    print("You have Following Lifelines remaining")
    for i in range(len(lifelines)):
        print(i + ") " + lifelines[i])
        options.append(i)


def linelines():
    print("Which Lifeline would you like to use? Press the number to use or press F to cancel")
    remaininglifelines()
    option = []
    for i in range(len(lifelines)):
        options.append(i)
    
    while True: 
        if keyboard.is_pressed('F' or 'f'):
            break
        options = []
        for i in range(len(lifelines)):
            
