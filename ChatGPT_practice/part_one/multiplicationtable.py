# Generate a multiplication table for a number provided by the user.

def main():
    print("Are you having trouble with your multiplication skills?")
    n = int(input("Enter a number and I'll help you out: "))


    for i in range(0, 13):
        print(f"{n} x {i} = {n * i}")


main()