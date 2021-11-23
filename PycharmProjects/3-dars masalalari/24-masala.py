a = int(input("Kunni kiriting: "))
b = a % 7
print("Haftaning bu kuni", end = " ")
if(b == 0):
    print("yakshanba")
elif(b == 1):
    print("dushanba")
elif(b == 2):
    print("seshanba")
elif(b == 3):
    print("chorshanba")
elif(b == 4):
    print("payshanba")
elif(b == 5):
    print("juma")
elif(b == 6):
    print("shanba")