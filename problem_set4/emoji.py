def main():
    import emoji

    try:
        user_input = input("Input: ")
        user_input = emoji.emojize(user_input, language='alias')
        print(user_input)
    except KeyboardInterrupt:
        pass


main()