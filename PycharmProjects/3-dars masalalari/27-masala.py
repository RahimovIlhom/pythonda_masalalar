a = int(input("Kunni kiriting: "))
b = a % 7
print("Haftaning bu kuni", end = " ")
if(b == 2):
    print("yakshanba")
elif(b == 3):
    print("dushanba")
elif(b == 4):
    print("seshanba")
elif(b == 5):
    print("chorshanba")
elif(b == 6):
    print("payshanba")
elif(b == 0):
    print("juma")
elif(b == 1):
    print("shanba")