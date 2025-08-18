#Eric Somogyi ID Logging Scripts"
print()

'''
1) 2 Points: Write a Python function that when provided a start_time, end_time, and log file,
will parse through the log entries of the given file. The function will check to see if the 
timestamp for the log entry is within the range provided, and if it is, add the
log entry to a list. It should also increment a counter. Print both the counter value and
log list.

Caveats:
Your logic should use the Time/DateTime object(s) to parse through the log entries.
The start time and end times provided (upon function call) should not be modified when
turning in your assignment. However, feel free to adjust while testing.
The log file name should not be modified.
Hint: There should be 25 entries that match.
'''

print("Question 1:")
print()
from datetime import datetime

def parse_logs(start_time, end_time, log_file):
    logcount = 0
    loglist = []
    
    start = datetime.strptime(start_time, "%b %d %H:%M:%S")
    end = datetime.strptime(end_time, "%b %d %H:%M:%S")
    
    with open(log_file, 'r') as f:
        for line in f:
            logged_time = datetime.strptime(line[0:15], "%b %d %H:%M:%S")
            if start <= logged_time <= end:
                loglist.append(line.strip())
                logcount += 1

    print(logcount)
    print(*loglist, sep="\n") # log entry to a new line

parse_logs("Oct 14 14:00:00", "Oct 14 19:00:00", "system.log")
print()


'''
2) 2 Points: Write a Python Logger object that accomplishes the following:
    - Creates a logger instance named <yourlastname>_logger
    - Writes INFO and above messages to the console
    - Writes ERROR and above messages to your log file
    - Uses a log format of timestamp, level, name, message. Each separated by the | symbol.

Your logger object should be written in the custom_logger function below.

Caveats:
Do not change the logger messages within the custom_logger function.
'''

print("Question 2:")
print()
import logging

def custom_logger(somogyi_logger):
    #my code goes here

    #- Creates a logger instance named <yourlastname>_logger
    logger = logging.getLogger('somogyi_logger')
    logger.setLevel(logging.INFO)

    #- Writes INFO and above messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Only warnings and above go to console

    #- Writes ERROR and above messages to your log file
    file_handler = logging.FileHandler('somogyi_logger.log')
    file_handler.setLevel(logging.ERROR)  # All messages get logged in file (Lowest)

    #- Uses a log format of timestamp, level, name, message. Each separated by the | symbol.
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)                     

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    #- Log Tests
    logger.debug("New user 'newuser' created successfully")
    logger.info("Stopping MySQL Database Server...")
    logger.warning("Apache Web Server stopped.")
    logger.error("Could not remove user properties from database.")
    logger.critical("System Restarted")

custom_logger('somogyi_logger.log')
print()


