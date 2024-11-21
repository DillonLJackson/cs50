def main():
    # Get expression from user, assign inputs to var. x,y,z
    expression = input("Expression: ")
    x, operator, z = expression.strip().split(" ")

    # assign index to x,y,z change x,z to floating point values
    num1 = float(x)
    num2 = float(z)

    # use if elif statements to calculate 
    if operator == "+":
        result = num1 + num2 
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        if num2 == 0:
            print("error")
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    else:
        print("error")
        return

    print(round(result, 1))


main() 
