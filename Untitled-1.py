def iteneraryMaker():
    pass


def actual():
    pass

def nonactual():
    salary = float(input('Hello! Please enter your per hour salary here...'))
    if salary <= 0:
        print("Error! Values out of scope!")
        main()
    startTime = int(input('Enter your starting time in military time without colons!'))
    endTime = int(input('Enter your ending time in military time without colons!'))
    formula1 = endTime - startTime
    if formula1 <= 0:
        print("Error! Values out of scope!")
        main()
    formula2 = formula1 / 60
    formula3 = formula2 * salary
    rounder = round(formula3, 2)
    print("Your salary is about...")
    print(rounder)
    print("Dollars!")
    iteneraryMaker()
def main():
    choice = int(input("Press 1 for actual date & time, press 2 for non-current date & time."))
    if choice == 1:
        actual()
    else:
        nonactual()
    

main()