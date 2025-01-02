def main():
    expression = input("Expression: ")
    x, operator, y = expression.strip().split(" ")

    num1 = float(x)
    num2 = float(y)

    if operator == "+":
        result = num1 + num2
    if operator == "-":
        result = num1 - num2
    if operator == "/":
        result = num1 / num2
    if operator == "*":
        result = num1 * num2

    print(round(result, 1))

main()