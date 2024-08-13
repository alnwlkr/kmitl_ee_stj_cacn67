#Even integer Summation from 1 to n

print("*** even integer summation from 1 to n ***")
ip = input("Enter an integer(n) : ")
try:
    float_ip = float(ip)
    n = int(float_ip)
    if float_ip == n and n >= 0:
        ans = 0
        lst = range(2,n + 1,2)
        # print(*lst)
        for number in range(2,n+1,2):
            ans = ans + number
        print(f'Summation => ', end='')
        print(*lst,sep='+',end='')
        print(f' = {ans}')
except:
    ...