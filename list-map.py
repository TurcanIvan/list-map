## Use a list to remember a 1d mad

# [ x ]  [  ]  [ x ]  [  ] [ x ]
# 0 - free
# 1 - occupied
 
parking = [ 0,0,1,0,1,0,1 ]
# index        ^

#user input

index_to_park = int(input("Where?  "))
#HW1. check if the index is NOT OUT OF RANGE!!!
if index_to_park > -1 and index_to_park < 7:       
    if parking[index_to_park] == 1:
        print("Occupied !!!")
    else:
        print("You can park there!")
        parking[index_to_park] = 1
else:
        print("I can't park in that place!!!")

for index in range(0,len(parking)):
    if parking[index] == 1:
        print(index,"[ x ]",end=" ")
    elif parking[index] == 0:
            print(index,"[   ]",end=" ")
