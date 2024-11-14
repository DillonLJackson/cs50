# get dollars and percent from user to calculate tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# convert user str to float and return to main
def dollars_to_float(d):
   x = float(d.strip('$'))
   return x
  
# convert int to percent float and return to main
def percent_to_float(p):
   y = float(p.rstrip('%')) / 100
   return y


main()
