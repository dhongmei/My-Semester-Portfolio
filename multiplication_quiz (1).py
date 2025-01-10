#Daniel Mei
#1/8/2025
#Multiplication Quiz

#init
import random
score = 0


#function

def multiplication_quiz():
    print("Welcome to the multiplication quiz!")
    number_question = int(input("How many questions would you like? ")) #asks user for question number

    for i in range(number_question):
        first_num = random.randint(1,10)
        second_num = random.randint(1,10)   #creates quesitons using random.randint

        print("What is " + str(first_num) + " x " + str(second_num)) #prints question

        answer = int(input("Your Answer: "))
        solution = first_num*second_num

        if answer == solution:
            print("Correct!")
            global score
            score = score + 1
        else:
            print("Wrong")

    print("Your final score is " + str(score) + "/" + str(number_question)) #tells score

#main
multiplication_quiz()
