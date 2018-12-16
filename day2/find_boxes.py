#import the list of tags
input_file = open("input.txt", "r")
box_IDs = input_file.readlines()

#initialize parameters for use within list
#ID being checked against other IDs
current_ID = ""
#ID being checked against by current_ID
crosscheck_ID = ""
#number of characters that don't match between the two IDs
mismatch_count = 0
#position of the last mismatch
mismatch_pos = 0
#common letters between the two IDs
common_letters = ""



##loop through each box ID
for index1 in range(len(box_IDs)):

    #save current box_ID to be checked with new line character removed
    #last string doesn't contain new line character, so caused issues
    current_ID = box_IDs[index1].replace("\n", "")
    
    #check against other IDs, can start at index1 because
    #already checked against all previous index1 occurances
    for index2 in range(index1 + 1, len(box_IDs)):

        #reset mismatch_count parameter
        mismatch_count = 0
        
        #avoid checking against itself
        crosscheck_ID = box_IDs[index2].replace("\n","")
        #assumes that all strings are the same length
        for letter in range(len(current_ID)):

            #checks each letter in the two IDs and flags any mismatches
            if current_ID[letter] != crosscheck_ID[letter]:
                mismatch_count += 1
                mismatch_pos = letter
                
        #if exactly one mismatch was found, prints which IDs match, and what the common letters are
        if mismatch_count == 1:
            common_letters = current_ID[:mismatch_pos] + current_ID[mismatch_pos + 1:]
            print("The two matching boxes are boxes " + str(index1) + " and " + str(index2))
            print("The common letters between these two boxes are: " + common_letters)


