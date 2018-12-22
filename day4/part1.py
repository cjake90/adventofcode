from day4classes import TimeLog
from day4classes import Guard
from day4classes import EventType



#import the list of guard events from the file
input_file = open('input.txt', 'r')
events_list = input_file.readlines()

#sort the events chronologically
events_list.sort()
with open('sorted.txt', 'w') as s:
    for item in events_list:
        s.write(item)

#creates a list of guards for tracking each guard's status
guard_status   = [Guard() for x in range(10000)]
active_guard   = 0
last_sleep_log = 0

#flag for error checking
guard_asleep   = 0

#variables to track the most time slept by a single guard
max_sleep_time  = 0
sleepiest_guard = 0

#populate the guard_log as needed
for index in range(len(events_list)):
    
    #create local variable to process
    currentLog = TimeLog(events_list[index])

    #If guard is starting a shift, then log him as the active guard
    if currentLog.event_type == EventType.SHIFT_STARTS:
        #if the last guard never woke up, an error occured
        if guard_asleep == 1:
            print(f'ERROR! Guard #{active_guard} never woke up!')
            print(f'Current time = {currentLog.timestamp}')

        #determine the guard's number and set him as the active guard
        start = currentLog.event.find('#') + 1
        end   = currentLog.event.find(' begins')
        active_guard = int(currentLog.event[start:end])

    #if guard is falling asleep, then log what time he fell asleep
    elif currentLog.event_type == EventType.GUARD_SLEEPS:
        #if the guard never woke up, an error occured
        if guard_asleep == 1:
            print(f'ERROR! Guard #{active_guard} never woke up!')
            print(f'Current time = {currentLog.timestamp}')

        #set guard as asleep
        guard_asleep = 1
        
        #save sleep log to be used to determine time asleep
        last_sleep_log = currentLog
        
    #if guard is woke up, then determine how long he was asleep
    elif currentLog.event_type == EventType.GUARD_WAKES:
        #if the guard never fell asleep, an error occured
        if guard_asleep == 0 :
            print(f'ERROR! Guard #{active_guard} never fell alseep')
            print(f'Current time = {currentLog.timestamp}')

        #set guard as awake
        guard_asleep = 0

        #calculate how much the guard slept between logs
        guard_status[active_guard].calculateSleep(last_sleep_log, currentLog)
        
        #check if this guard has slept more than any others so far, if so mark him as the sleepiest guard
        if guard_status[active_guard].minutes_asleep > max_sleep_time:
            max_sleep_time = guard_status[active_guard].minutes_asleep
            sleepiest_guard = active_guard


#print who the sleepiest guard is and how much he slept
print(f'The sleepiest guard is Guard #{sleepiest_guard}')
print(f'He fell asleep {guard_status[sleepiest_guard].times_asleep} times for a total of {guard_status[sleepiest_guard].minutes_asleep} minutes')


#calculate what the exact time was that he slept the most
maxtimes = str(max(guard_status[sleepiest_guard].minute_status))
sleepiest_minute_abs = guard_status[sleepiest_guard].minute_status.index(int(maxtimes))
sleepiest_hour       = int(sleepiest_minute_abs / 60)
sleepiest_minute     = sleepiest_minute_abs % 60

#print out the results to the puzzle
print(f'He was asleep {maxtimes} times at {sleepiest_hour:02d}:{sleepiest_minute:02d} (minute {sleepiest_minute_abs})')
print(f'His ID*minutes asleep at that minute = {sleepiest_guard*sleepiest_minute_abs}')
