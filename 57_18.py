choose = input("Press C to convert from Fahrenheit to Celsisus. \nPress F to convert from Celsius to Fahrenheit.  ")

if choose == "c" or choose == "C":
    print("Your choice: C")
    print()
    F = eval(input("Please enter the temperature in Fahrenheit:  "))
    C = round((F - 32) * 5/9)
print("The temperature in Celsius is", str(C) + ".")    

if choose == "f" or choose == "F":
    print("Your choice: F")
    print()
    C = eval(input("Please enter the temperature in Fahrenheit:  "))
    F = round(C * 9/5) + 32
print("The temperature in Fahrenheit is", str(F) + ".")
