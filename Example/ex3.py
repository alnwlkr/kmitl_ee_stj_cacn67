#Example III – Factorial

# ip = input("Enter Integer Value : ")
ip = "0"
try:
    ans = 1
    float_ip = float(ip)
    int_ip = int(float_ip)
    #If It's int, we do factorial
    if float_ip == int_ip:
        if int_ip > 0:
            step = -1
        else:
            step = 1
        print(list(range(int_ip,0,step)))
        for i in range(int_ip,0,step):
            ans = ans*i
            #ans =* i
        print(f'{int_ip}! = {ans}')
    else:
        print("Only Integer Value is accepted.")
    
except:
    print("Only Integer Value is accepted.")