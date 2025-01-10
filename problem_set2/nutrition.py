def main():

    nutrition = [{"fruit": "Apple", "calories": "130"},
                    {"fruit": "Avacado", "calories": "50"}, 
                    {"fruit": "Banana", "calories": "110"},
                    {"fruit": "cantaloupe", "calories": "50"},
                    {"fruit": "Grapefruit", "calories": "60"},
                    {"fruit": "grapes", "calories": "90"},
                    {"fruit": "Honeydew Melon", "calories": "50"},
                    {"fruit": "kiwifruit", "calories": "90"},
                    {"fruit": "Lemon", "calories": "15"},
                    {"fruit": "Lime", "calories": "20"},
                    {"fruit": "Nectarine", "calories": "60"},
                    {"fruit": "Orange", "calories": "80"},
                    {"fruit": "Peach", "calories": "60"},
                    {"fruit": "Pear", "calories": "100"},
                    {"fruit": "Pineapple", "calories": "50"},
                    {"fruit": "Plums", "calories": "70"},
                    {"fruit": "Strawberries", "calories": "50"},
                    {"fruit": "Sweet Cherries", "calories": "100"},
                    {"fruit": "Tangerine", "calories": "50"},
                    {"fruit": "Watermelon", "calories": "80"}
]

    item = input("Item: ")
    for nut in nutrition:
        formatted_item = item.capitalize()
        if formatted_item == (nut["fruit"]):
            print(f"calories: {(nut["calories"])}")


main()