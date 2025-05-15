# get user to input fruits
# make user input case insensitive
# make counter for amount of items inputed
# return items in alphabetical order with amount of times entered 


def main():
        
    shopping_list = []

    while True:
        try:
            shopping_cart = input("")
            shopping_list.append(shopping_cart)
            shopping_list.sort()
        except EOFError:
            break
    print(shopping_list)
                       

main()