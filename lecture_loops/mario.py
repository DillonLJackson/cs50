def main():
    print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

#----------------------------------------

def print_column(height):
    print("#\n" * height, end="")

#---------------------------------------- 

    print_row(4)


def print_row(width):
    print("?" * width)

#----------------------------------------

    print_sqaure(3)

def print_sqaure(size):
    for i in range(3):
        print("#" * size)



main()

