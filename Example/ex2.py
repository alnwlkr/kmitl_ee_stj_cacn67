#Example II – Isn’t it float?

ip = input("Enter Integer Value : ")
try:
    float_ip = float(ip)
    int_ip = int(float_ip)
    if float_ip == int_ip:
            print("It's an Int!")
    else:
         print("It's a Float!")
    
except:
    print("Only Integer Value is accepted.")