# implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents in change the user is owed. 
# Assume that the user will only input integers, ignore any integer that isn't an accepted denomination.
# integers = 25, 10, and 5 cents

def main():

    amount_due = 50

    while amount_due > 0:

        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Insert Coin: "))

        if insert_coin in [5, 10,25]:
            amount_due -= insert_coin
            
        if amount_due < 0:
            print(f"Change Owed: {abs(amount_due)}")



main()