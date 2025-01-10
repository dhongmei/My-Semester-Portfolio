#Daniel Mei
#Name Generator
#10/17/24

#init

#functions
def name_generator():
    print("Welcome to Your Alternate Name Generator")
    print("Please Answer the Following Answers to Figure Out Your Name") #welcome user

    answer = input("blue or green:") #asks blue or green

    if answer == "blue":
        answer = input("ocean or desert:") #ask ocean or desert
        if answer == "ocean":
            answer = input("swimming or running:") #ask swimming or running
            if answer == "swimming":
                print("Derek")
            else:
                print("Thomson")
        if answer == "desert":
            answer = input("lifting or tennis:")
            if answer == "lifting":
                print("Gray")
            else:
                print("Austin")

    if answer == "green":
        answer = input("mountain or forest:") #asks mountain or forest
        if answer == "mountain":
            answer = input("biking or diving:") #asks biking or diving
            if answer == "biking":
                print("Thomas")
            else:
                print("Peter")
        if answer == "forest":
            answer = input("volleyball or basketball:") #asks volleyball or basketball
            if answer == "volleyball":
                print("Rose")
            else:
                print("Aiden")

#main

name_generator()
