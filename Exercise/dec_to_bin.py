#Convert decimal to binary

ip = input("Enter a Decimal value <=255:")
try:
    float_ip = float(ip)
    int_ip = int(float_ip)
    if float_ip == int_ip:
        if int_ip <= 255:
            #reverse string and don't display 0b
            print(bin(int_ip)[:1:-1])
        else:
            print("Number > 255")
    else:
        print("It's Float Value")
except:
    ...

#Python List Slicing
#Lst[ Initial : End : IndexJump ]