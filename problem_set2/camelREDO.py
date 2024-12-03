# creat an index for user input
# create a loop that checks len for capital letter
# if loop returns true convert capital to lower case and add _
def main():
    words = (input("camelCase: "))
    snake_case = camel_to_snake(words)
    print(f"snake_case: {snake_case}")

def camel_to_snake(case):
    result = []
    for i, char in enumerate(case):
        if char.isupper():
            if i != 0:
                result.append("_")
                result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
    

main()

