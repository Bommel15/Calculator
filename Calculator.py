#       Calculator V1 - Kevin Van Bommel | Oct 15, 2020
while = True:
    try:
        print("Welcome to my shit calculator.")
        print("The program will prompt you to input two integers and an operator")
        while True:
            try:
                Integer1Str = float(input("Please input the first integer: "))
            except ValueError:
                print("Try again, this time with a number")
                continue
            else:
                break

        OpperatorStr = input("Please input the opperator: ")
        while not OpperatorStr in ["+", "-", "*", "/", "^"]:
            print("Try again, this time with one of these symbols: + - * / ^")
            OpperatorStr = input("Please input the opperator: ")

        while True:
            try:
                Integer2Str = float(input("Please input the second integer: "))
            except ValueError:
                print("Try again, this time with a number")
                continue
            else:
                break

        # Calculations


        def addition():
            outputInt = float(Integer1Str) + float(Integer2Str)
            print("Hopefully my math isn't shite:")
            print("Your equation was: ", Integer1Str, OpperatorStr, Integer2Str)
            print(outputInt)


        def subtraction():
            outputInt = float(Integer1Str) - float(Integer2Str)
            print("Hopefully my math isn't shite:")
            print("Your equation was: ", Integer1Str, OpperatorStr, Integer2Str)
            print(outputInt)


        def multiplication():
            outputInt = float(Integer1Str) * float(Integer2Str)
            print("Hopefully my math isn't shite:")
            print("Your equation was: ", Integer1Str, OpperatorStr, Integer2Str)
            print(outputInt)


        def division():
            outputInt = float(Integer1Str) / float(Integer2Str)
            print("Hopefully my math isn't shite:")
            print("Your equation was: ", Integer1Str, OpperatorStr, Integer2Str)
            print(outputInt)


        def exponential():
            outputInt = float(Integer1Str) ^ float(Integer2Str)
            print("Hopefully my math isn't shite:")
            print("Your equation was: ", Integer1Str, OpperatorStr, Integer2Str)
            print(outputInt)


        # Output

        if OpperatorStr == "+":
            addition()
        elif OpperatorStr == "-":
            subtraction()
        elif OpperatorStr == "*":
            multiplication()
        elif OpperatorStr == "/":
            division()
        elif OpperatorStr == "^":
        exponential()
programLoop = input("Press ENTER to do another calculation, otherwise press any key to exit.")) = ""
if programLoop == "":
    continue
else:
    break
# OpperatorStr = input("Press any button")
# while not OpperatorStr in ["+", "-", "*", "/", "^"]:
#    print("Try again, this time with one of these symbols: + - * / ^")
#    OpperatorStr = input("Please input the opperator: ")