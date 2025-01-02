# Write a program to find the factorial of a given number using a loop.


def main():
    n = int(input("Please enter a number: "))

    factorial = 1

    for i in range(1, n - 1):
        factorial *= i


    print(f"the factorial of the given number is {factorial}")

        

main()