#import the list of frequency changes and create frequency int
input_file = open("input.txt", "r")
freq_changes = input_file.readlines()
frequency = 0

#sum frequency changes and print the result
for index in range(len(freq_changes)):
    frequency += int(freq_changes[index])

print(frequency)
