import string

#import the list of guard events from the file
input_file = open('input.txt', 'r')
base_polymer = input_file.readlines()[0]

#delete new line character
base_polymer = base_polymer.replace('\n','')

#create string of letters
letters = string.ascii_lowercase
removed_type_result = [0 for x in range(len(letters))]

#set flags for while loops
#complete indicates a full pass through the polymer was completed with no reactions
complete = False
#reaction_occured indicates if a reaction has occured during this pass through the polymer
reaction_occured = False
end_of_polymer = False

#number of passes for curiosity
num_passes_occured = 0

for letter in range(len(letters)):
    polymer = base_polymer
    polymer = polymer.replace(letters[letter], '')
    polymer = polymer.replace(letters[letter].capitalize(), '')
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

    #set complete to false again so that it can do the next letter
    complete = False

    #log what the length was for that letter
    removed_type_result[letter] = len(polymer)

print(removed_type_result)                       
best_result = min(removed_type_result)
best_polymer = removed_type_result.index(best_result)
removed_type = letters[best_polymer]
                       
print(f'The most successful reaction was when removing {letters[best_polymer]}/{letters[best_polymer].capitalize()}')
print(f'This resulted in a final polymer of size {best_result}')


