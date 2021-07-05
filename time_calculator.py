def convertToDecimal(time):
    conv = time.replace(":", ".")
    return float(conv)


def add_time(start, duration):
    new_time = ""

    # separate AM/PM
    strTime = start.split(" ")
    durTime = duration.split(" ")
    print(durTime)

    # convert time to minutes
    strDec = convertToDecimal(strTime[0])
    durDec = convertToDecimal(durTime[0])
    print(strDec, durDec)

    return new_time
