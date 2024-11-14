# asking user for input
print("type something: ")
x = input("")

# added sep function to input ... between each word
print(*x.split(), sep='...')