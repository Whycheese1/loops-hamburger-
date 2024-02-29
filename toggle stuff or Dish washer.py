#################
#Basic toggles and for loops
#J SANDERSON
#FEB 29 2024
#
#################

# Basic formant for a toggle switch and for loop


#function returns toggle state to console/shell
Chewy_hamburger = True

def Chew_hamburger_state():
    if Chewy_hamburger: 
        print("Hamburger is tender and ready to eat!")
    else:
        print("Hamburger is CHEWY and you are a BAD COOK!!")
#Loop returns toggle state 60 times before exiting 
for x in range(60):
    print("Minutes on Grill: ", x)
    Chew_hamburger_state()
    
#boolean toggle switch of current stale
Chewy_hamburger = not Chewy_hamburger
#final value of toggle state
Chew_hamburger_state()