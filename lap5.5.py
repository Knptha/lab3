def Fa(c):
    f = (9/5)*c+32
    return f

def ka(c):
    k = c+273.15
    return k

c = int(input("รับค่าองศาเซลเซียส:"))
print("องศาฟาเรนไฮล์ %.2f" % Fa(c))
print("องศาเคลวิน %.2f" % ka(c))