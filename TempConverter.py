def main():
    input_1 = ""
    while input_1.upper() != "x":
        # print("Would you like to convert to Celcius or Farenheit?")
        input_1 = str(
            input("Convert to (c)elcius or (f)arenheit (x) to exit: "))

        if input_1.upper() == "C":
            farenheit = float(input("Enter temperature in farenheit: "))
            calculateToCelcius(farenheit)
        elif input_1.upper() == "F":
            celcius = float(input("Enter temperature in celcius: "))
            calculateToFah(celcius)
        elif input_1.upper() == "X":
            exit()
        else:
            print("Please choose a valid option!")


def calculateToCelcius(f):
    return print(round((f - 32) * 5 / 9, 1))


def calculateToFah(c):
    return print(round((c * 9 / 5) + 32, 1))


if __name__ == "__main__":
    main()
