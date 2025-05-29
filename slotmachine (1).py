#Daniel Mei
#1/28/25
#Slot Machine

#Init
symbols = ["🂡", "🂱", "🃁", "🃑", "🂢", "🂲", "🃂", "🃒", "7"]
credit = 100
import random
import time

#Function
def slot_machine():
    global credit
    print("Slot Machine Symbols: ", symbols)
    print("You have 100 credit. Two of a kind = x2. Three of a kind = x5. Three 7s or Jackpot = x10")
    print("Press 'S' to spin or Press 'Q' to quit") #initation


    while True:

        player_choice = input("Spin the slots? (Q/S):") #user input
        if player_choice.capitalize() == "Q": #quits
            print("Thank you for playing")
            break

        playing_amount = int(input("How much would you like to play:")) #user input for how much they would like to play
        if credit < playing_amount: #if not enough credit will not allow user to play
            print("Not enough credit")
            added_credit = int(input("How much credit would you like to buy: "))
            card = input("Enter card: ") #ask user to pay and add more credit to play
            if card == card:
                credit += added_credit
                print("Thank you for inputing more credit")
            else:
                break


        if player_choice.capitalize() == "S" and credit >= playing_amount: #both user inputs they would like to play and they have enough credit
            credit -= 10
            print("spinning...")
            time.sleep(2)
            slot1 = random.choice(symbols)
            print(slot1)

            print("spinning...")
            time.sleep(2)
            slot2 = random.choice(symbols)
            print(slot2)

            print("spinning...")
            time.sleep(2)
            slot3 = random.choice(symbols)
            print(slot3)

            if slot1 == slot2 == slot3 == "7": #jackpot is all 7 (*10)
                print("Jackpot!!")
                credit += playing_amount*10
                print("Your Credit is: " , credit)

            elif slot1 == slot2 == slot3: #if all slots same three of a kind (*5)
                print("Three of a Kind!")
                credit += playing_amount*5
                print("Your Credit is: " , credit)

            elif slot1 == slot2 or slot2 == slot3 or slot3 == slot1: #if two slots same two of a kind (*2)
                print("Two of a Kind!")
                credit += playing_amount*2
                print("Your Credit is: " , credit)

            else:
                print("You Lose") #lose
                credit - playing_amount
                print("Your Credit is: " , credit)




#main
slot_machine()
