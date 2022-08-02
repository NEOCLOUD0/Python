userInput = ""
started = False
while userInput.lower() != "quit":
    userInput = input("Type: ")
    if userInput.lower() == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif userInput.lower() == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car has stopped")
    elif userInput.lower() == "quit":
        print("You have quit the program")
    elif userInput.lower() == "help":
        print("start - To start the car")
        print("stop - To stop the car")
        print("quit - to exit")
    else:
        print("Sorry I do not understand that")

