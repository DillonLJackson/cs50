def main():
<<<<<<< HEAD
    
=======

    # gather fraction from user
>>>>>>> 46e5249c99c22e827bb78aec189a814aa9584493
    fuel = input("Fraction: ")
    x, y = fuel.strip().split("/")

    # give user input int value
    num1 = int(x)
    num2 = int(y)

    # take the int value from user and convert them into fraction
    amount = (num1 / num2) * 100
    if num1 and num2 == 4:
        amount = "F"
    if num1 or num2 == 0:
        amount = "E"
    else:
        print(f"{amount}")



main()