def exp(num: int, times: int) -> int:
    if times == 0: return 1
    elif times < 0: negative = True
    else: negative = False

    res = num
    for i in range(abs(times) - 1):
        res *= num

    if negative: res = -res
    return round(res)

def binToInt(binarystr: str) -> int:
    res = 0
    counter = len(binarystr) - 1
    for i in binarystr:
        if i == "1": res += exp(2, counter)
        counter -= 1

    return res

def intToBin(num: int) -> str:
    x = 0
    bits = 0
    while num > x:
        x = exp(2, bits)
        bits += 1

    res = ""
    for i in reversed(range(bits)):
        x = exp(2, i)
        if num >= x:
            num -= x
            res += "1"
        else:
            res += "0"

    return res