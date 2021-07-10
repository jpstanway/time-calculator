import math


def splitTime(time):
    split = time.split(":")
    hours = int(split[0])
    mins = int(split[1])

    return {
        'hours': hours,
        'mins': mins,
    }


def calcPeriod(hours, period):
    rotations = math.floor(hours / 12)
    isEven = (rotations % 2) == 0

    if (isEven == False):
        return "PM" if period == "AM" else "AM"
    else:
        return period


def calcTime(start, time, type):
    calc = 0
    intervals = {
        'hours': 12,
        'mins': 60
    }
    interval = intervals[type]

    if (time >= interval):
        leftOver = time % interval
        calc = start + leftOver
    else:
        calc = start + time

    if (calc > interval):
        calc -= interval

    calc = str(calc)

    if (type == 'mins' and len(calc) == 1):
        calc = "0" + calc

    return calc


def calcDays(start, hours, period):
    added = start + hours

    if (period == 'PM'):
        added += 12

    return math.floor(added / 24)


def add_time(start, duration, weekday=''):
    new_time = ""

    # separate AM/PM
    strTime = start.split(" ")

    # convert time to minutes
    strSplit = splitTime(strTime[0])
    durSplit = splitTime(duration)

    newHours = calcTime(strSplit['hours'], durSplit['hours'], 'hours')
    newMins = calcTime(strSplit['mins'], durSplit['mins'], 'mins')
    newPeriod = calcPeriod(durSplit['hours'], strTime[1])
    days = calcDays(strSplit['hours'], durSplit['hours'], strTime[1])

    if (strSplit['mins'] + durSplit['mins'] >= 60):
        newHours = str(int(newHours) + 1)
        newPeriod = "PM" if newPeriod == "AM" else "AM"

    new_time += newHours + ":" + newMins + " " + newPeriod

    if (weekday):
        new_time += ', ' + weekday

    if (days == 1):
        new_time += ' (next day)'
    elif (days > 1):
        new_time += ' (' + str(days) + ' days later)'

    return new_time
