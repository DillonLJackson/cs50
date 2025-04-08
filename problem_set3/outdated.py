def main():

    list_month = [{"monthname": "January", "monthday": "01"},
              {"monthname": "February", "monthday": "02"},
              {"monthname": "March", "monthday": "03"},
              {"monthname": "April", "monthday": "04"},
              {"monthname": "May", "monthday": "05"},
              {"monthname": "June", "monthday": "06"},
              {"monthname":"July", "monthday": "07"},
              {"monthname": "August", "monthday": "08"},
              {"monthname": "September", "monthday": "09"},
              {"monthname": "October", "monthday": "10"},
              {"monthname": "November", "monthday": "11"},
              {"monthname": "December", "monthday": "12"}
              ]

    date = input("please input a date in anno Domini format: ")
    while date != "00/00/0000":

        try:
            month, year = date.split(",")
            month, day = month.strip().split(" ")
            year = year.strip()
            for mon in list_month:
                    if month == (mon["monthname"]): 
                        print('{2}-{1}-{0}'.format(day.zfill(2), (mon["monthday"]), year))

        except ValueError:
            try:
                month, day, year = date.strip("").split("/")
                print('{2}-{1}-{0}'.format(day.zfill(2), month.zfill(2), year))
                pass
            except ValueError:
                 pass
        

        date = input("please input a date in anno Domini format: ")
            

            
    
main()