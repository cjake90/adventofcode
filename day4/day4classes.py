from enum import Enum

class EventType(Enum):
    UNKNOWN      = 0
    SHIFT_STARTS = 1
    GUARD_SLEEPS = 2
    GUARD_WAKES  = 3

class TimeLog:
    #This is the timelog class
    event_type = EventType.UNKNOWN

    #initialize by pulling out the information from the log
    def __init__(log, log_string):
        log.year  = int(log_string[1:5])
        log.month = int(log_string[6:8])
        log.day   = int(log_string[9:11])
        log.hour  = int(log_string[12:14])
        log.min   = int(log_string[15:17])
        log.event = log_string[19:]
        #calculate a timestamp with only numbers
        log.timestamp  = f"{log.year:04d}{log.month:02d}{log.day:02d}{log.hour:02d}{log.min:02d}"
        
        log.eventType()

    #return what type of log it is
    def eventType(log):
        if log.event.find("Guard") != -1:
            log.event_type = EventType.SHIFT_STARTS
        elif log.event.find("falls") != -1:
            log.event_type = EventType.GUARD_SLEEPS
        elif log.event.find("wakes") != -1:
            log.event_type = EventType.GUARD_WAKES


    #icrement the log by one minute
    def increment_time(log):
        log.min += 1

        #if at 60 minutes, increment the hour by one
        if log.min == 60:
            log.min = 0
            log.hour += 1

        #if at 24 hours, increment the day by one
        if log.hour == 24:
            log.hour = 0
            log.day += 1

        #end of month       
        if (log.day == 30) & (log.month == 2):
            log.day = 1
            log.month += 1
            
        elif (log.day == 31) & (log.month in [4,6,9,11]):
            log.day = 1
            log.month += 1
                
        elif (log.day == 32) & (log.month in [1,3,5,7,8,10,12]):
            log.day = 1
            log.month += 1

        #end of year
        if log.month == 13:
            log.month = 1
            log.year += 1

        #resulting timestamp
        log.timestamp = f"{log.year:04d}{log.month:02d}{log.day:02d}{log.hour:02d}{log.min:02d}"
        

class Guard:
    #initialize the guard
    def __init__(guard):
        #list of 1440 minutes in the day, all initialized to never slept (0)
        guard.minute_status  = [0 for min in range(1440)]
        guard.times_asleep   = 0
        guard.minutes_asleep = 0

    #calculate how much the guard slept between two logs
    def calculateSleep(guard, start_log, stop_log):
        #mark that this is a new time that the guard fell asleep
        guard.times_asleep += 1

        #increment the start log and log it as a minute asleep until it is the same time as the stop log
        #this increments the minute that it started, but not the minute of the stop log
        while start_log.timestamp != stop_log.timestamp:
            
            #calculate the minute in the day he was asleep and increment times asleep
            guard.minute_status[start_log.hour * 60 + start_log.min] += 1

            #increment total minutes asleep
            guard.minutes_asleep += 1

            #increment start log time
            start_log.increment_time()
    
