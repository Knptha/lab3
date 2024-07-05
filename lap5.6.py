def beforMidterm(a,b,c):
    h = a+b+c
    return h

s = int(input("รับค่าคะแนนเก็บ:"))
j = int(input("รับค่าคะแนนจิตพิสัย:"))
m = int(input("รับค่าคะแนนกลางภาค:"))

if s <= 20 and j <= 10 and m <= 20:
    print("คะแนนเก็บ %d" % beforMidterm(s, j, m))
else:
    print("คะแนนเกิน")



