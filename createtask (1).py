#3/17/25
#Create Task

#Init
student_names = ["ANDRE", "CATRIN", "DARCY", "SKYLA", "JORDAN", "IMRAN", "DANIELLE",
                  "MEREDITH", "ZAYD", "CONNOR", "Jack", "CHRISTOPHER", "AUSTIN", "JAMIE"]
student_grades = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]


#Function
def add_grade(student): #allows user to input grades for student in parameter
        while True:
            print("What is the grade you wish to add as a percentage? (exclude % and as whole #)")
            grade = input("Grade: ")
            position = student_names.index(student)
            student_grades[position].append(int(grade))
            print("The grade has been successfully inputed for " + student)

            more = input("Add another grade for this student? (Y/N): ").upper() #allows user to input multiple grades for student
            if more == "N":
                print("\n")
                break
            elif more == "Y":
                print("\n")
            else:
                print("ERROR: Invalid Input")
                break

def remove_grade(student): #allows user to remove grades for student in parameter
    while True:
        print("What is the grade you wish to remove as a percentage? (exclude % and as whole #)")
        grade = int(input("Grade: "))
        position = student_names.index(student)
        if grade in student_grades[position]:

            grade = int(grade)
            student_grades[position].remove(grade)
            print("The grade has been successfully removed for " + student)
            print("\n")

            more = input("Remove another grade for this student? (Y/N): ").upper() #allows user to remove multiple grades for student
            if more == "N":
                print("\n")
                break
            elif more == "Y":
                print("\n")
            else:
                print("ERROR: Invalid Input")
                print("\n")
                break

        else:
            print("ERROR: Grade is not in system")
            print("Please Try Again")
            print("\n")
            break



def calculate_average(): #calculates the student's average
    print("\n")
    student = input("Which student?: ").upper() #student name input

    if student in student_names: #locates if student is in student_names list
         position = student_names.index(student) #locates the position of the list for the specific student's grade
         grades = student_grades[position] #all grades within the list inside of the student's list in student_grades list
         number_of_grades = len(grades) #total number of grades for that student
         grade_sum = 0

         if number_of_grades > 0: #locates if there are grades for that student
            grade_sum = sum(grades)
            average_grade = grade_sum / number_of_grades
            print("The average grade for " + student +  " is " + str(average_grade)) #student's average grade
            print("\n")

         else: #prints error if there are no grades for the student
            print("ERROR: no grades for student")
            print("\n")

    else: #prints error if student is not in system
        print("ERROR: Student not in system")
        print("\n")

def view_grades(): #view all of the student's current grades
    print("\n")
    student = input("View Grades for Student: ").upper() #student name input
    if student in student_names: #locates if student is in student_names list
        position = student_names.index(student) #locates the position of the list for the specific student's grade
        if len(student_grades[position]) > 0:  #locates if there are grades for that student
            print(student_grades[position]) #print student's grades
            print("\n")
        else: #prints error if there are no grades for the student
            print("There are no grades for this student")
            print("\n")
    else: #prints error if student is not in system
        print("ERROR: Student not in system")
        print("\n")

def main(): #main function creating the actual grade organizer
    print("---------------------------Welcome to Grade Organizer---------------------------")
    print("This tool allows you to organize your student's grades")
    print("\n")
    print("""You may:
    1) Add Grade
    2) Remove Grade
    3) Show All Grades
    4) Show Average Grade
    5) Quit""")
    print("\n")

    while True:
        print("To begin, please enter a number (1, 2, 3, 4, or 5)")
        number = input("Number: ") #user input for the function that would like to use

        if number == "1": #if input is 1 add grade
            print("\n")
            print("Which student would you like to add a grade for?")
            student = input("Student: ").upper() #name input
            if student in student_names: #locates if student is in student_names list
                add_grade(student)

            else:
                print("ERROR: Student is not in system") #prints error if student is not in system
                print("Please Try Again")
                print("\n")

        elif number == "2": #if input is 2 remove grade
            print("\n")
            print("Which student would you like to remove a grade for?")
            student = input("Student: ").upper() #name input
            if student in student_names: #locates if student is in student_names list
                remove_grade(student) #remove_grade function if student

            else:
                print("ERROR: Student is not in system") #prints error if student is not in system
                print("Please Try Again")

        elif number == "3": #if input is 3 view grades
            view_grades()

        elif number == "4": #if input is 4 calculate average
            calculate_average()

        elif number == "5": #if input is 5 break while True loop
            print("\n")
            print("Thank you for using Grade Organizer")
            break

        else: #locates if there is a wrong input
            print("ERROR: Invalid number")
            print("Please Try Again")
            print("\n")

#Main
main()
