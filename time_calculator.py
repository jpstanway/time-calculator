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
        calc = abs(interval - leftOver - start)
    else:
        calc = start + time

    if (calc > interval):
        calc -= interval

    calc = str(calc)

    if (type == 'mins' and len(calc) == 1):
        calc = "0" + calc

    return calc


def add_time(start, duration):
    new_time = ""

    # separate AM/PM
    strTime = start.split(" ")

    # convert time to minutes
    strSplit = splitTime(strTime[0])
    durSplit = splitTime(duration)

    newHours = calcTime(strSplit['hours'], durSplit['hours'], 'hours')
    newMins = calcTime(strSplit['mins'], durSplit['mins'], 'mins')
    newPeriod = calcPeriod(strSplit['hours'], strTime[1])

    new_time += newHours + ":" + newMins + " " + newPeriod

    return new_time
