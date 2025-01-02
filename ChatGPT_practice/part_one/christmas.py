# Enter the number of rows: 4
# *
# **
# ***
# ****

def main():
    rows = int(input("Enter the number of rows: "))
    christmas(rows)

def christmas(tree):
    for i in range(1, tree + 1):
        print("*" * i)        
        

main()
