def main():
   sen = input("")
   sen = convert(sen)
   print(sen)

def convert(sen):
   sen = sen.replace(":)", "🙂")
   sen = sen.replace(":(", "🙁")
   return sen

main()

