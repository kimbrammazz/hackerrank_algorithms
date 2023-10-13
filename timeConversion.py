# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example

# s = '12:01:00PM'
# Return '12:01:00'.

# s = '12:01:00AM"
# Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in 12 hour format
# Returns

# string: the time in 12 hour format
# Input Format

# A single string  that represents a time in -hour clock format (i.e.:  or ).

def timeConversion(s):
    # Write your code here
    time = s.split(":")
    print(time)
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    ntime = ':'.join(time)
    print(ntime)
    print(str(ntime[:-2]))


timeConversion("07:05:45PM")
timeConversion("12:01:00AM")
