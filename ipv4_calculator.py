import binary_calculator as bc

def confBits(orgbits: str, wantedbits: int) -> str:
    if len(orgbits) > wantedbits: return orgbits[len(orgbits) - wantedbits:]

    wantedbits -= len(orgbits)
    add = ""
    for i in range(wantedbits):
        add += "0"
    return add + orgbits

def IPv4ToIPv4B(ip: str) -> str:
    IPv4 = ip.split(".")
    IPv4B = []
    for i in IPv4:
        x = bc.intToBin(int(i))
        x = confBits(x, 8)
        IPv4B.append(x)
    return "{}.{}.{}.{}".format(*IPv4B)

def IPv4BToIPv4(ip: str) -> str:
    IPv4B = ip.split(".")
    IPv4 = []
    for i in IPv4B:
        IPv4.append(bc.binToInt(i))
    return "{}.{}.{}.{}".format(*IPv4)

def getClass(ip: str, isbinary: bool = False) -> str:
    if isbinary: x = bc.binToInt(ip.split(".")[0])
    else: x = int(ip.split(".")[0])

    if x >= 0 and x <= 127: res = "A"
    elif x >= 128 and x <= 191: res = "B"
    elif x >= 192 and x <= 223: res = "C"
    elif x >= 224 and x <= 239: res = "D"
    elif x >= 240 and x <= 255: res = "E"
    else: res = "?"

    return res
