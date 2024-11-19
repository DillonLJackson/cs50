# get input from user 
answer = input("What is the answer to the great question of life, the universe, and everything? ")

# see if users input matches desires outcome, if not print no
match answer:
    case "forty-two" | "forty two" | "42":
        print("Yes")
    case _:
        print("No")