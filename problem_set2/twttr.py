def main():

    import re

    while True:
        n = str(input("Input: "))

        n = re.sub("[aeiou]", "", n)

        print(f"Output: {n}")

        if n == "quit":
            break

main()