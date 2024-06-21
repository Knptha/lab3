print("โปรดกรอกข้อมูล")
a = int(input("น้ำหนักตัว : "))
b = int(input("ส่วนสูง :  "))
bmi = a/(b/100)**2
print(bmi)
if bmi<18.50:
    print("น้ำหนักน้อย/ผอม")
elif bmi>18.50 and bmi <=22.90:
    print("ปกติ(สุขภาพดี")
elif bmi>23 and bmi <=24.90:
    print("ท้วม/โรคอ้วนระดับ1")
elif bmi >=25 and bmi <=29.90:
    print("อ้วน/โรคอ้วนระดับ2")
else:
    print("อ้วนมาก/โรถอ้วนระดับ3")
    
    
