import random


class WeekOneExercise:

    def abbreviation(self):
        myString = input("input a paragraph : ")
        items = myString.split(' ')
        print(items)
        for item in items:
            print(item[0], end='  ')

    def rockPaperScissors(self):
        myGame = input("Please input One of these Characters ( S , K , G) :").lower()
        list = ['s', 'k', 'g']
        randNum = random.randrange(0, 2)
        # print(f"random number : {randNum} and the char is : {list[randNum]}")
        pcGame = ''
        while True:
            print(f"You Choose {myGame} and PC choose {list[randNum]}")

            if myGame in list:
                pcGame = list[randNum]
                if myGame == pcGame:
                    print(f"{Style.WHITE}The game is draw !!{Style.RESET}")
                    break
                elif myGame == 'k' and pcGame == 'g':
                    print(f"{Style.RED}You Lost!!{Style.RESET}")
                    break
                elif myGame == 'g' and pcGame == 'k':
                    print(f"{Style.GREEN}You Win !!{Style.RESET}")
                    break
                elif myGame == 's' and pcGame == 'k':
                    print(f"{Style.RED}You Lost !!{Style.RESET}")
                    break
                elif myGame == 'k' and pcGame == 's':
                    print(f"{Style.GREEN}You Win !!{Style.RESET}")
                    break
                elif myGame == 's' and pcGame == 'g':
                    print(f"{Style.GREEN}You Win !!{Style.RESET}")
                    break
                elif myGame == 'g' and pcGame == 's':
                    print(f"{Style.RED}You lost !!{Style.RESET}")
                    break
            else:
                myGame = input("Please input One of these Characters ( S , K , G) :").lower()

    def bmiCalculation(self):

        weight = float(input("Please input your weight in kg : "))
        height = float(input("Please input your height in cm : "))
        bmi = 0
        while True:
            try:
                bmi = (weight / (height / 100) ** 2)
                print(f"Your bmi is {bmi}")
                if bmi <= 18.4:
                    print(f"{Style.YELLOW}You are underweight.{Style.RESET}")
                    break
                elif bmi <= 24.9:
                    print(f"{Style.GREEN}You are healthy.{Style.RESET}")
                    break
                elif bmi <= 29.9:
                    print(f"{Style.CYAN}You are over weight.{Style.RESET}")
                    break
                elif bmi <= 34.9:
                    print(f"{Style.CYAN}You are severely over weight.{Style.RESET}")
                    break
                else:
                    print(f"{Style.RED}You are in Critical Condition , immediately visit doctor.{Style.RESET}")
                    break
            except:
                weight = float(input("Please input your weight in kg : "))
                height = float(input("Please input your height in cm : "))


week1 = WeekOneExercise()


class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


print(f"Welcome to Week one exercise , choose one of these programs:")
print(f"{Style.GREEN}1. Abbreviation of paragraph.{Style.RESET}")
print(f"{Style.GREEN}2. Rock Paper Scissor.{Style.RESET}")
print(f"{Style.GREEN}3. BMI calculation.{Style.RESET}")


while True:
    menuSelection = input("Input menu number (1 , 2 , 3):")
    try:
        menuSelection = int(menuSelection)
        if menuSelection == 1:
            week1.abbreviation()
            if input("Do you want to Continue ? (Y / N)") in ['N', 'n']: break;
        elif menuSelection == 2:
            week1.rockPaperScissors()
            if input("Do you want to Continue ? (Y / N)") in ['N', 'n']: break;
        elif menuSelection == 3:
            week1.bmiCalculation()
            if input("Do you want to Continue ? (Y / N)") in ['N', 'n']: break;
        else:
            print(f"{Style.RED}Please input 1 , 2 or 3.{Style.RESET}")
    except:
        print(f"{Style.RED}Please input the integer number.{Style.RESET}")
