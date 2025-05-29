#Daniel Mei
#1/24/25
#Magic 8 Ball

#Init
import random
import time
magiclist = ["It is certain", "Without a doubt", "Yes definitely", "As I see it, yes", "Most likely", "Yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "No", "My reply is no", "Outlook not so good", "Very doubtful"]

#Function
def magic8ball():
    print("Welcome to the Magic 8 Ball") #welcomes user

    while True:
        user_question = input("Please enter a yes or no question: ") #user inputs yes or no question
        magic_question = user_question.endswith("?")
        print("shake...")
        time.sleep(2)
        print("shake...")
        time.sleep(2)
        print("shake...")
        time.sleep(2)
        if magic_question == True:
            print(random.choice(magiclist)) #prints random outcome
            tryagain = input("Would you like to ask another question: ") #ask user if they would like to ask another question
            if tryagain == "no":
                print("Thank you for using Magic 8 Ball")
                break
        else:
            print("ERROR no question mark")




#Main
magic8ball()
