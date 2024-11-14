# this function takes sen function to convert user input into emoji
def main():
   sen = input("")
   sen = convert(sen)
   print(sen)

# this function uses .replace to change emoticon to emoji
def convert(sen):
   sen = sen.replace(":)", "🙂")
   sen = sen.replace(":(", "🙁")
   return sen

main()

