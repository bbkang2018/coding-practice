try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Devided by Zero")
except ValueError:
    print("Invalid Input")

