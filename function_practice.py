def display_invoice(username, amount, due_date):
    print(f"Hello, {username}.")
    print(f"Your Amount owed is, ${amount:.2f}. And is due: {due_date}.")

display_invoice("dillonj", 43.6034, "01/01")

def add(x, y):
    z = x + y 
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y 
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name(input(""), input(""))
print(full_name)

