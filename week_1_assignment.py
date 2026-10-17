# GOOD AFTERNOON, EVERYONE!
# THIS IS MY WEEK 1 ASSIGNMENT.
# HOPE I DID WELL.
#######################################################CALCULATOR#######################################################
import sys

count = 0 

def calculator():
    asks_3 = str(
        input(
            "Choose an Operation to perform: Enter a for addition, b for subtraction, c for multiplication, d for division, and e for modulus..."
        )
    )
    if asks_3 == "a":
        def addition():
            print("\nWelcome to the Addition Operation!\n")
            try:
                x = float(input("Enter your first variable: "))
                y = float(input("Enter your second variable: "))
                print(f"{x} + {y} = {x + y}")
            except ValueError:
                print("Please, enter only numbers!")
                addition()

            def checking():
                asking = input("Do you want to perform another calculation?\n")
                if asking.lower() == "yes":
                    calculator()
                elif asking.lower() == "no":
                    exit
                else:
                    print("Please, enter 'yes' or 'no'!")
                    checking()
            checking()
        addition()



    elif asks_3 == "b":
        def subtraction():
            print("\nWelcome to the Subtraction Operation!\n")
            try:
                x = float(input("Enter your first variable: "))
                y = float(input("Enter your second variable: "))
                print(f"{x} - {y} = {x - y}")
            except ValueError:
                print("Please, enter only numbers!")
                subtraction()

            def checking():
                asking = input("Do you want to perform another calculation?\n")
                if asking.lower() == "yes":
                    calculator()
                elif asking.lower() == "no":
                    exit
                else:
                    print("Please, enter 'yes' or 'no'!")
                    checking()
            checking()
        subtraction()



    elif asks_3 == "c":
        def multiplication():
            print("\nWelcome to the Multiplication Operation!\n")
            try:
                x = float(input("Enter your first variable: "))
                y = float(input("Enter your second variable: "))
                print(f"{x} * {y} = {x * y}")
            except ValueError:
                print("Please, enter only numbers!")
                multiplication()

            def checking():
                asking = input("Do you want to perform another calculation?\n")
                if asking.lower() == "yes":
                    calculator()
                elif asking.lower() == "no":
                    exit
                else:
                    print("Please, enter 'yes' or 'no'!")
                    checking()
            checking()
        multiplication()



    elif asks_3 == "d":
        def division():
            print("\nWelcome to the Division Operation!\n")
            try:
                x = float(input("Enter your first variable: "))
                y = float(input("Enter your second variable: "))
                print(f"{x} / {y} = {x / y}")
            except ZeroDivisionError, ValueError:
                print("Please, enter only numbers, and do not enter '0' for the second value!")
                division()

            def checking():
                asking = input("Do you want to perform another calculation?\n")
                if asking.lower() == "yes":
                    calculator()
                elif asking.lower() == "no":
                    exit
                else:
                    print("Please, enter 'yes' or 'no'!")
                    checking()
            checking()
        division()



    elif asks_3 == "e":
        def modulus():
            print("\nWelcome to the Modulus Operation!\n")
            try:
                x = float(input("Enter your first variable: "))
                y = float(input("Enter your second variable: "))
                print(f"{x} mod {y} = {x % y}")
            except ZeroDivisionError, ValueError:
                print("Please, enter only numbers, and do not enter '0' for the second value!")
                modulus()

            def checking():
                asking = input("Do you want to perform another calculation?\n")
                if asking.lower() == "yes":
                    calculator()
                elif asking.lower() == "no":
                    exit
                else:
                    print("Please, enter 'yes' or 'no'!")
                    checking()
            checking()
        modulus()

    else:
        print("Please, enter a valid input 'a, b, c, d, or e'!")
        calculator()
#####################################################################################################################################################################
#######################################################QUIZ#######################################################
def quiz():

    def question_1a():
        question_1 = str(
            input(
                "What is an Atom according to classical physics?\na. A ball\nb. An electron\nc. A divider\nd. A particle\ne. A wave\n\n"
            )
        )
        if (
            question_1.lower() == "a"
            or question_1.lower() == "b"
            or question_1.lower() == "c"
            or question_1.lower() == "e"
        ):
            print("\nWrong!\n")
        elif question_1.lower() == "d":
            print("Correct!")
            global count
            count += 1
        else:
            print("Please, enter a valid input!")
            question_1a()

    question_1a()

    def question_2b():
        question_2 = str(
            input(
                "Which of the following is a Low Level Language?\na. JS\nb. HTML\nc. Python\nd. ASM\ne. CSS\n\n"
            )
        )
        if (
            question_2.lower() == "a"
            or question_2.lower() == "b"
            or question_2.lower() == "c"
            or question_2.lower() == "e"
        ):
            print("\nWrong!\n")
        elif question_2.lower() == "d":
            print("Correct!")
            global count
            count += 1
        else:
            print("Please, enter a valid input!")
            question_2b()

    question_2b()

    def question_3c():
        question_3 = str(
            input(
                "How many points in space were discovered by the French Mathematician 'Joseph Louis Lagrange', where the gravitational effects of two bodies cancel out, allowing a third body to be placed without interference?\na. 4\nb. 5\nc. 7\nd. 2\ne. 7\n\n"
            )
        )
        if (
            question_3.lower() == "a"
            or question_3.lower() == "c"
            or question_3.lower() == "d"
            or question_3.lower() == "e"
        ):
            print("\nWrong!\n")
        elif question_3.lower() == "b":
            print("Correct!")
            global count
            count += 1
        else:
            print("Please, enter a valid input!")
            question_3c()

    question_3c()

    def question_4d():
        question_4 = str(
            input(
                "Who is the British Scientist that invented Calculus?\na. Leonhard Euler\nb. Jacob Bernoulli\nc. Friedrich Gauss\nd. Isaac Newton\ne. Albert Einstein\n\n"
            )
        )
        if (
            question_4.lower() == "a"
            or question_4.lower() == "b"
            or question_4.lower() == "c"
            or question_4.lower() == "e"
        ):
            print("\nWrong!\n")
        elif question_4.lower() == "d":
            print("Correct!")
            global count
            count += 1
        else:
            print("Please, enter a valid input!")
            question_4d()

    question_4d()

    def question_5e():
        question_5 = str(
            input(
                "Which of the following is not a consequence of Quantum Physics/Mechanics?\na. Wave-Particle Duality\nb. Quantum Tunneling\nc. Quantum Assist\nd. Quantum Entanglement\ne. Non-Locality\n\n"
            )
        )
        if (
            question_5.lower() == "a"
            or question_5.lower() == "b"
            or question_5.lower() == "d"
            or question_5.lower() == "e"
        ):
            print("\nWrong!\n")
        elif question_5.lower() == "c":
            print("Correct!")
            global count
            count += 1
        else:
            print("Please, enter a valid input!")
            question_5e()

    question_5e()

    print(f"You got {count} of 5")
    if count == 5:
        print("You got an A!")
    elif count == 4:
        print("You got a B!")
    elif count == 3:
        print("You got a C!")
    elif count == 2:
        print("You got a D!")
    elif count == 1:
        print("You got an E!")
    elif count == 0:
        print("You got an F!")
#####################################################################################################################################################################
#######################################################FREE-WILL1#######################################################
def does1():
    dose = input("Do you want to launch the quiz?\nEnter 'yes' or 'no'!\n")
    if dose.lower() == "yes":
        quiz()
    elif dose.lower() == "no":
        print("Thank You for using CalcuQuizAtor!\nSee you later!")
        sys.exit()
    else:
        print("\nPlease, enter 'yes' or 'no'!\n")
        does1()
#####################################################################################################################################################################
#######################################################FREE-WILL2#######################################################
def does2():
    dose = input("Do you want to launch the calculator?\nEnter 'yes' or 'no'!\n")
    if dose.lower() == "yes":
        calculator()
    elif dose.lower() == "no":
        print("Thank You for using CalcuQuizAtor!\nSee you later!")
        sys.exit()
    else:
        print("\nPlease, enter 'yes' or 'no'!\n")
        does2()
#####################################################################################################################################################################
#######################################################LAUNCH#######################################################
def launch():
    asks_2 = str(input("To launch Calculator...press 1\nFor Quiz...press 2\n"))
    if asks_2 == "1":
        calculator()
        does1()
    elif asks_2 == "2":
        quiz()
        does2()
    else:
        print("\nPlease, enter '1' or '2'!\n")
        launch()



#######################################################ACTUAL-QUIZ-CALCULATOR#######################################################

def start():
    asks = str(input("Do you want to Launch CalcuQuizAtor?\nEnter 'yes' or 'no'!\n"))
    if asks.lower() == "yes":
        print(f"\nYou answered {asks}!\n")
        launch()
    elif asks.lower() == "no":
        print(f"\nYou answered {asks}!\n")
        print("Thank You for using CalcuQuizAtor!\nSee you later!")
        sys.exit()
    else:
        print("\nPlease, enter 'yes' or 'no'!\n")
        start()
start()







































