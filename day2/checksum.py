#import the list of tags
input_file = open("input.txt", "r")
box_IDs = input_file.readlines()

#initialize parameters to calculate checksum
dupe_count = 0
trip_count = 0
checksum = 0

#initialize parameters for use within list
letter_count = 0
dupe_occured = False
trip_occured = False

#check for duplicate or tripple occurances in each parameter
##loop through each box ID
for index in range(len(box_IDs)):

    ##Check each letter in the box_ID for multiple occurances
    for letter in box_IDs[index]:
        letter_count = box_IDs[index].count(letter)

        #flag if a duplicate or tripple occurance appeared
        if letter_count == 2: dupe_occured = True
        if letter_count == 3: trip_occured = True

    #log that a duplicate or triple occurance appeared
    if dupe_occured == True: dupe_count += 1
    if trip_occured == True: trip_count += 1

    #reset flags to False
    dupe_occured = False
    trip_occured = False

#calculate checksum as product of dupe_count and trip_count
checksum = dupe_count * trip_count

#print checksum
print(checksum)
