#Write a function named `add_time` that takes in two required parameters and one
#optional parameter:
#* a start time in the 12-hour clock format (ending in AM or PM)
#* a duration time that indicates the number of hours and minutes
#* (optional) a starting day of the week, case insensitive
#The function should add the duration time to the start time and return the
#result.
#If the result will be the next day, it should show `(next day)` after the time.
#If the result will be more than one day later, it should show `(n days later)`
#after the time, where "n" is the number of days later.
#If the function is given the optional starting day of the week parameter, then
#the output should display the day of the week of the result. The day of the
#week in the output should appear after the time and before the number of days
#later.   add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

def add_time(time, duration, day=None):
    #find am or pm/time without am pm
    new_time , am_pm = time.split(' ')
    #print(am_pm)
    #extract hours, min
    startHour, startMin =  new_time.split(':')
    durHours , durMin = duration.split(':')
    #change to number
    startHour = int(startHour)
    startMin = int(startMin)
    #print(startHour, startMin)
    durHours = int(durHours)
    durMin = int(durMin)
    #print(durHours, durMin)

    #Turn to 24Hour clock
    if am_pm == 'PM':
        startHour = startHour + 12

    # get the new hour and min for your returned time
    totalHours = (startHour + durHours)
    totalMin = startMin + durMin
    finalMin = totalMin % 60
    addHourFromMin = totalMin // 60
    newHour = totalHours + addHourFromMin


    #Get your final hour (the modulo operator will give you the time in 24 hour,
    #then repeat the process with 12, for the 12 hour format
    finalHour = (newHour % 24) % 12
    if finalHour == 0:
        finalHour = finalHour + 12
    #check for case where min is less than 10
    if finalMin < 10:
        finalMin = '0' + str(finalMin)

    #deciding am or pm based on the 24Hour clock hour returned from newHour % 24
    if (newHour % 24) <= 11:
        am_pm = "AM"
    else:
        am_pm = "PM"

    # Find how many days later
    addDays = newHour // 24
    daysLater = ''
    if addDays < 2 and addDays > 0:
        daysLater = '(next day)'
    else:
        daysLater = '(' + str(addDays) + ' days later)'
    #print(daysLater)

    #set up for finding the new day
    daysOfWeek = {
        'Sunday': 1,
        'Monday': 2,
        'Tuesday': 3,
        'Wednesday': 4,
        'Thursday': 5,
        'Friday': 6,
        'Saturday': 7
        }
    #find the final day
    if day is not None:
            finalDay = (daysOfWeek[day.lower().capitalize()] + addDays) % 7
            for (key, value) in daysOfWeek.items():
                if value == finalDay:
                    newDay = key

    #Print the results

    if day is None and addDays > 0:
        return (str(finalHour) + ':' + str(finalMin) + ' ' + am_pm + ' ' +
        daysLater)

    elif day is None and addDays == 0:
        return (str(finalHour) + ':' + str(finalMin) + ' ' + am_pm)

    elif day is not None and addDays == 0:
        return (str(finalHour) + ':' + str(finalMin) + ' ' + am_pm + ', ' +
        newDay)

    elif day is not None and addDays > 0:
        return (str(finalHour) + ':' + str(finalMin) + ' ' + am_pm + ', ' +
        newDay + ' ' + daysLater)

    elif day is not None:
        return (str(finalHour) + ':' + str(finalMin) + ' ' + am_pm + ', ' +
        newDay)

    elif day is None:
        return (str(finalHour) + ':' + str(finalMin) + ' ' + am_pm)




add_time("8:16 PM", "466:02", "tuesday")
#Returns: 6:18 AM, Monday (20 days later)
add_time("11:59 PM", "24:05", "Wednesday")
#Return: 12:04 AM, Friday (2 days later)
add_time("2:59 AM", "24:00", "saturDay")
#Returns: 2:59 AM, Sunday (next day)
add_time("3:30 PM", "2:12", "Monday")
#Return: 5:42 PM, Monday
add_time("5:01 AM", "0:00")
#Returns:5:01 AM
add_time("8:16 PM", "466:02")
#Returns: 6:18 AM (20 days later)
add_time("11:59 PM", "24:05")
#Returns: 12:04 AM (2 days later)
add_time("2:59 AM", "24:00")
#Returns: "2:59 AM (next day)"
add_time("3:30 PM", "2:12")
#Returns: 5:42 PM
add_time("11:55 AM", "3:12")
#Returns: 3:07 PM
add_time("9:15 PM", "5:30")
#Returns: 2:45 AM (next day)
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
add_time("11:43 PM", "24:20", "tueSday")
#Returns: 12:03 AM, Thursday (2 days later) DONE
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
