# Check if a number is prime.
def main():

    n = int(input("Please insert a number: "))


    for i in range(2, (n//2)+1):
        if n % i == 0:
            print("not prime")
            break

    else:
        print("is prime")


main()