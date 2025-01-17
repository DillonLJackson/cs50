def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(s):

    #check that user input is within 2-6 characters
    if len(s) > 1 and len(s) < 7:
        # turn user input into a list
        plate_list = list(s)
        # checking that the first and second chr of user input is str
        if plate_list[0].isalpha() and plate_list[1].isalpha():
                # making sure there are no digits in the middle of user input
                first_digit = False

                for plate in plate_list:
                    if plate.isdigit():
                         if not first_digit and plate == '0':
                              return False
                         
                         first_digit = True
                    elif first_digit and not plate.isalpha():
                         return False
                return True
        return False

                
             
                
    
      




main()