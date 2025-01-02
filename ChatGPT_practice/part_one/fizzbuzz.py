# Print numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for multiples of both, print "FizzBuzz".
def main():

    n = 1
    m = 101

    for number in range(n, m):
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
       
        else:
            print(number)
        
        



main()