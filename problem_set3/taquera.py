def main():


    menu = [
       {
        "food": "Baja Taco", "price": 4.25,
        "food": "Burrito", "price": 7.50,
        "food": "Bowl", "price": 8.50,
        "food": "Nachos", "price": 11.00,
        "food": "Quesadilla", "price": 8.50,
        "food": "Super Burrito", "price": 8.50,
        "food": "Super Quesadilla", "price": 9.50,
        "food": "Taco", "price": 3.00,
        "food": "Tortilla Salad", "price": 8.00
        }
    ]


    
    while True:
        item = input("Item: ")
        for men in menu:
            if item == (men["food"]):
                print(men["price"])
            
            if item == "control-d":
                break










    import re
    def titlecase(s):
        return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                    lambda mo: mo.group(0).capitalize(),
                    s)
    

main()