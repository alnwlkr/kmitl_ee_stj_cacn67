#Enter a numbers and display even number
#Using for loop
print(" *** Filter only even number ***")
lst_ip = input("Enter some numbers : ").split()
print(lst_ip)
len_ip = len(lst_ip)

for i in range(len_ip):
    number = int(lst_ip[i])
    if number % 2 == 0:
        print(f'{number}',end='')
        if i < len_ip - 1:
            print(f' ',end='')
print("")