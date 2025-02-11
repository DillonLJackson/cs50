def main():

    my_list = []
    while True:
            try:
                grocery = input("").title()
                my_list.append(grocery)
                my_list.sort()


            except EOFError:
                print(my_list.count())
                exit()

main()