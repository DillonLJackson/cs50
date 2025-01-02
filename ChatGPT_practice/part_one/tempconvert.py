# write a program that converts between celsius and fahrenheit

def main():
    # converting from celsius to fahrenheit. 
    c = int(input("Please enter a degree in celsius: "))
    conversion = (c * 1.8) + 32
    
    print(f"{c} degrees in Celcius is equal to {conversion} degrees in fahrenheit. ")
    

    # converting from fahrenheit to celsius
    f = int(input("Please enter a degree in Fahrenheit: "))
    conversionf = (f - 32) * 5/9

    print(f"{f} degrees in Fahrenheit is equal to {conversionf} degrees in Celsius. ")

    



main()