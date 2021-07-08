import math


def splitTime(time):
    split = time.split(":")
    hours = int(split[0])
    mins = int(split[1])

    return {
        'hours': hours,
        'mins': mins,
    }


def calcTime(start, time, type):
    calc = 0
    intervals = {
        'hours': 12,
        'mins': 60
    }
    interval = intervals[type]

    if (time >= interval):
        rotations = math.floor(time / interval)
        leftOver = time % 12
        isEven = (leftOver % 2) == 0

        calc = start + leftOver
    else:
        calc = start + time

    if (calc > interval):
        calc -= interval

    return str(calc)


def add_time(start, duration):
    new_time = ""

    # separate AM/PM
    strTime = start.split(" ")
    # durTime = duration.split(" ")

    # convert time to minutes
    strSplit = splitTime(strTime[0])
    durSplit = splitTime(duration)

    newHours = calcTime(strSplit['hours'], durSplit['hours'], 'hours')
    newMins = calcTime(strSplit['mins'], durSplit['mins'], 'mins')

    new_time += newHours + ":" + newMins + strTime[1]

    return new_time
