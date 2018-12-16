#import the list of frequency changes and calculate it's size
import math
input_file = open("input.txt", "r")
freq_changes = input_file.readlines()
list_size = len(freq_changes)


#added new parameters, list of frequencies experineced, duplicate
frequency = 0
frequency_list = []
duplicate_found = False

index = 0

#sum frequency changes and add them to the list of frequencies experienced
#loop until a duplicate is found
while (duplicate_found == False):
    #use % operator for looping around
    frequency += int(freq_changes[index % list_size])
    if frequency in frequency_list : duplicate_found = True
    frequency_list.append(frequency)
    index+=1


print("The first duplicate frequency is " + str(frequency) + " after " + str(index) + " frequency changes")

#curiosity
print("This occured on the " + str(math.ceil(index/list_size)) + " pass through the list")
