import serial


def xorCksm(arr):
    rolling_xor = 0
    for e in arr:
        rolling_xor = rolling_xor ^ e
    return rolling_xor


def convertToBytes(val):
    arr = []
    while val > 0:
        arr.append(val % 256)
        val = val // 256
    arr.reverse()
    return arr


def convertToBstr(arr):
    bstr = b""
    for e in arr:
        bstr = bstr + e.to_bytes(1, "big")
    return bstr


# client functions

DRY_MAX = 495
WET_MAX = 190


def dryThresholdFromPercent(percent: float):
    if (percent < 0) or (percent > 1):
        print("you passed a dry threshold outside of 0 - 1")
        return DRY_MAX

    return percent * (DRY_MAX - WET_MAX) + WET_MAX


def setPlanterPumps(val):
    # 1 = on, 0 = off
    msg_buf = [255, 1, val, val]
    with serial.Serial("/dev/ttyS0", 9600, timeout=1) as ser:
        ser.write(msg_buf)
        response_bstr = ser.read(4)
        return response_bstr == convertToBstr(msg_buf)


def setHydroPump(val):
    # 1 = on, 0 = off
    msg_buf = [255, 2, val, val]
    with serial.Serial("/dev/ttyS0", 9600, timeout=1) as ser:
        ser.write(msg_buf)
        response_bstr = ser.read(4)
        return response_bstr == convertToBstr(msg_buf)


def setDryThreshold(val):
    byte_arr = convertToBytes(val)
    if len(byte_arr) > 2:
        print("Number too large, must fit in 2 bytes")
        return False
    if len(byte_arr) < 2:
        byte_arr = [0] * (2 - len(byte_arr)) + byte_arr
    msg_buf = [255, 3] + byte_arr + [xorCksm(byte_arr)]
    with serial.Serial("/dev/ttyS0", 9600, timeout=1) as ser:
        ser.write(msg_buf)
        response_bstr = ser.read(5)
        return response_bstr == convertToBstr(msg_buf)


def setFlowTime(val):
    # flow time in ms
    byte_arr = convertToBytes(val)
    if len(byte_arr) > 4:
        print("Number too large, must fit in 4 bytes")
        return False
    if len(byte_arr) < 4:
        byte_arr = [0] * (4 - len(byte_arr)) + byte_arr
    msg_buf = [255, 4] + byte_arr + [xorCksm(byte_arr)]
    with serial.Serial("/dev/ttyS0", 9600, timeout=1) as ser:
        ser.write(msg_buf)
        response_bstr = ser.read(7)
        return response_bstr == convertToBstr(msg_buf)


def getSensorValues():
    with serial.Serial("/dev/ttyS0", 9600, timeout=1) as ser:
        ser.write([255, 5, 1, 1])
        response_bstr = ser.read(17)
        if len(response_bstr) < 17:
            return False
        if response_bstr[16] != xorCksm(response_bstr[:-1]):
            return False
        readings = []
        for i in range(8):
            readings.append((response_bstr[i * 2] << 8) + (response_bstr[i * 2 + 1]))
        return readings


# print(setPlanterPumps(False))
# print(setHydroPump(False))
# print(setDryThreshold(490))
# print(setFlowTime(1230))
print(getSensorValues())
