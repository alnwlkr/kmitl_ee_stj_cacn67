ip = input("Enter Integer Value : ")

try:
    float_ip = float(ip)
    print(float_ip,round(float_ip))
    if float_ip == round(float_ip,0): #42.42 => 42
        print("Int")
    else:
        print("Float")
except:
    print("Error naja.")