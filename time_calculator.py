import math


def totalTime(start, duration, period):
    total = 0
    strSplit = start.split(":")
    durSplit = duration.split(":")

    # add hours in current day to duration
    currentHours = int(strSplit[0])

    if (period == 'PM' and currentHours != 12):
        currentHours += 12
    elif (period == 'AM' and currentHours == 12):
        currentHours = 0

    hours = int(durSplit[0]) + currentHours

    # add up mins, and add to hours if needed
    mins = int(strSplit[1]) + int(durSplit[1])

    if (mins >= 60):
        hours += 1
        mins -= 60

    total = str(hours) + ":" + str(mins)

    return total


def calcPeriod(hours, period):
    rotations = math.floor(int(hours) / 12)
    isEven = (rotations % 2) == 0

    if (isEven == False):
        return "PM" if period == "AM" else "AM"
    else:
        return period


def calcHour(hours):
    leftOver = int(hours) % 12

    if (leftOver == 0):
        leftOver = 12

    return str(leftOver)


def add_time(start, duration, weekday=''):
    new_time = ""

    strTime = start.split(" ")

    total = totalTime(strTime[0], duration, strTime[1])
    totalSplit = total.split(":")

    days = math.floor(int(totalSplit[0]) / 24)
    hour = calcHour(totalSplit[0])
    mins = totalSplit[1]
    period = calcPeriod(totalSplit[0], strTime[1])

    if (len(mins) == 1):
        mins = "0" + mins

    new_time = hour + ":" + mins + " " + period

    if (weekday):
        new_time += ", " + weekday

    if (days == 1):
        new_time += " (next day)"
    elif (days > 1):
        new_time += " (" + str(days) + " days later)"

    return new_time
