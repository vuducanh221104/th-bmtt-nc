def kiem_tra_so_nguyen_to(n):
    if n <=1:
        return False
    for i in range(2, int(n ** 0.5)+ 1):
        if n % 1 == 0:
            return False
        return True
number = int(input("Nhap vao so can kiem tra:"))
if kiem_tra_so_nguyen_to(number):
     print(number,"toi la so nguyen to.")
else:
        print(number,"0 la so nguyen to.")
