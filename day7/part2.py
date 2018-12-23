import string
#function to convert letter to index
def letterIndex(letter):
    return string.ascii_uppercase.find(letter)

#function to convert index to letter
def indexLetter(index):
    return string.ascii_uppercase[index]

#function to remove a task from the pre_req list
def removeReq(list, completed):
    #go through each task in the list and remove the completed tasks from pre_reqs
    for req in range(len(list)):
        if completed in list[req]:
            list[req].remove(completed)
    return list

#import the list of guard events from the file
input_file = open('input.txt', 'r')
requirements = input_file.readlines()

#define how many workers
num_workers = 5
#initialize solution string
completed_letters = ''
#track current tasks of workers
worker_task = ['' for worker in range(num_workers)]
#track duration of current task for workers
worker_time = [0 for worker in range(num_workers)]
total_time = 0

#list of pre_reqs for every letter
pre_req = [[] for letter in string.ascii_uppercase]

#creates list of pre_reqs for each letter
for requirement in requirements:
    pre_req[letterIndex(requirement[36])].append(requirement[5])

#empty list once parsing is complete
empty_list = ['.' for letter in string.ascii_uppercase]

print(pre_req)
#loop through until all letters have been added to the order list
while True:

    #check if the workers completed their tasks yet
    for worker in range(num_workers):
        #if the worker doesn't have a task, nothing to check
        if worker_task[worker] != '':
            #if the worker has worked on the task for enough time, consider it completed
            if worker_time[worker] > (60 + letterIndex(worker_task[worker])):
                #clear the pre_req for the task
                pre_req[letterIndex(worker_task[worker])] = '.'
                #remove the task from other pre_reqs
                pre_req = removeReq(pre_req, worker_task[worker])
                print(f'Worker #{worker} completed task {worker_task[worker]} at second #{total_time}')
                #clear the workers task
                worker_task[worker] = ''

    #if the pre_req list has been cleared, break
    if pre_req == empty_list: break
    
    #assign the worker a new task
    for worker in range(num_workers):
        #if the worker already has a task, nothing to do
        if worker_task[worker] == '':
            #check if any tasks are available
            if [] in pre_req:
                #if a task is available, set the worker to that task, and set time on task to 0
                worker_task[worker] = indexLetter(pre_req.index([]))
                worker_time[worker] = 0
                print(f'Worker #{worker} is starting task {worker_task[worker]} at second #{total_time}')
                #set that task's pre_reqs to in progress so it doesn't come up for another elf
                pre_req[pre_req.index([])] = 'in progress'
        #increment the time worked on the current task
        worker_time[worker] += 1
        
    if pre_req == empty_list: break
    #increment total time
    total_time += 1


#print the solution
print(f' it took a total time of {total_time} seconds')
