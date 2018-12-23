import string
#function to convert letter to index
def letterIndex(letter):
    return string.ascii_uppercase.find(letter)

#function to convert index to letter
def indexLetter(index):
    return string.ascii_uppercase[index]

#import the list of guard events from the file
input_file = open('input.txt', 'r')
requirements = input_file.readlines()

#initialize solution string
order = ''

#list of pre_reqs for every letter
pre_req = [[] for letter in string.ascii_uppercase]

#creates list of pre_reqs for each letter
for requirement in requirements:
    pre_req[letterIndex(requirement[36])].append(requirement[5])

#empty list once parsing is complete
empty_list = ['.' for letter in string.ascii_uppercase]

#loop through until all letters have been added to the order list
while pre_req != empty_list:
    #find first letter index that has all pre_reqs completed
    new_step = pre_req.index([])

    #mark the pre_req as '.' so that it doesn't get flagged again
    pre_req[new_step] = '.'

    #add the letter to the order based on the index
    order += indexLetter(new_step)

    #remove the letter from all other pre_reqs
    for req in range(len(pre_req)):
        if indexLetter(new_step) in pre_req[req]:
            pre_req[req].remove(indexLetter(new_step))

#print the solution
print(order)
