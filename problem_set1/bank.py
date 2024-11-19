# takes user input and funcitons below to print total money
def main(): 
   greeting = input("Greeting: ")

   if greeting.startswith("Hello"):
      print("$0")
   elif greeting.startswith("hello"):
      print("$0")
   elif greeting.startswith("H"):
      print("$20")
   elif greeting.startswith("h"):
      print("$20")
   else:
      print("$100")



main()