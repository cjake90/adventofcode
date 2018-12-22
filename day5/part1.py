#import the list of guard events from the file
input_file = open('input.txt', 'r')
polymer = input_file.readlines()[0]

#delete new line character
polymer = polymer.replace('\n','')

#set flags for while loops
#complete indicates a full pass through the polymer was completed with no reactions
complete = False
#reaction_occured indicates if a reaction has occured during this pass through the polymer
reaction_occured = False
end_of_polymer = False

#number of passes for curiosity
num_passes_occured = 0

#loop until a full pass through the polymer occurs without a reaction
while complete == False:

    #set reaction occured to false before parsing the polymer
    reaction_occured = False

    #set starting index to 0
    index = 0 

    #used while loop since the length of the polymer will be changing
    while index < (len(polymer) - 1):

        #ensure polymer character is the same type with different polarities
        #won't match when compared, but when both capitalized, will match
        if (polymer[index] != polymer[index + 1]) & \
           (polymer[index].capitalize() == polymer[index + 1].capitalize()):

            #if index was 0, delete first two characters of string
            if index == 0: polymer = polymer[index + 2:]

            #if index non-zero, delete index and index + 1 from string
            else: polymer = polymer[:index] + polymer[index + 2:]

            #mark that a reaction occured during the pass
            reaction_occured = True

        #go to next item in the index
        index += 1
        
    #increment number of passes that have occured
    num_passes_occured += 1

    #if no reaction occured this pass, then it is complete
    if reaction_occured == False: complete = True

print(f'The final number of units in the polymer after completing the reactions is {len(polymer)}')


