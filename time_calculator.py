import math


def getHours(time):
    split = time.split(":")
    return int(split[0])


def convertToDecimal(time):
    conv = time.replace(":", ".")
    return float(conv)


def add_time(start, duration):
    new_time = ""
    new_hours = 0

    # separate AM/PM
    strTime = start.split(" ")
    durTime = duration.split(" ")

    # convert time to minutes
    strDec = convertToDecimal(strTime[0])
    durDec = convertToDecimal(durTime[0])

    strHours = getHours(strTime[0])
    durHours = getHours(durTime[0])

    if (durHours >= 12):
        rotations = math.floor(durHours / 12)
        leftOver = durHours % 12
        isEven = (leftOver % 2) == 0

        # if (isEven == False):

        new_hours = strHours + leftOver
    else:
        new_hours = strHours + durHours

    if (new_hours > 12):
        new_hours -= 12

    new_time += str(new_hours)

    return new_time
