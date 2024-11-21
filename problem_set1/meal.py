def main():
    # get user input
    what_time = convert(input("what time is it? "))

    # if convert function returns value inbetween desired times, return meal time
    if what_time >= "7" and what_time <= "8":
        print("Breakfast")
    if what_time >= "12" and what_time <= "13":
        print("Lunch")
    if what_time >= "18" and what_time <= "19":
        print("Dinner")

# function that takes input ("7:30") strips the : and converts 7 and 30 to variables which you can manipulate
def convert(time):
    hour, minutes = time.strip().split(":")
    num1 = float(hour)
    num2 = float(minutes)
    result = num1 + num2 / 60
    return time


if __name__ == "__main__":
    main()