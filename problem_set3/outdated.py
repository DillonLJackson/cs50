def main():


    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"
              ]
    
    while True:
        try:
            
            date = input("Please enter a date in MM/DD/YY style: ")
            month, day, year = date.strip().split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            

        except ValueError:
            print("please enter date in the correct format.")
            break
            
        print(date)
        
        


main()