#       Calculator V1 - Kevin Van Bommel | Oct 15, 2020
programLoop = str
while True:
    print("Welcome to my shit calculator.")
    try:
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
            print ("Press enter to restart")
            programLoop = input("Press any key to continue")
            if programLoop == "":
                break
            else:
                continue

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
        break
