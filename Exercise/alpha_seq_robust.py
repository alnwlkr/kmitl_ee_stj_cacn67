# input => char step length
# chat => single character (only lowercase)
# step => positive intger
# length => number of character to disp

# get input from user
print(" *** Alphabet Sequence (a-z) ***")
lst_ip = input("Enter character step length : ").split()
# lst_ip = ['a', '3', '26']
try:
    check = True
    #check if char is lower case
    if lst_ip[0] == lst_ip[0].lower():
        char = lst_ip[0]
        # print(f'char = {char}')
    else:
        check = False
    #check if step is a positive integer
    if float(lst_ip[1]) == int(float(lst_ip[1])) and int(float(lst_ip[1])) > 0:
        step = int(float(lst_ip[1]))
        # print(f'step = {step}')
    else:
        check = False
    #check if length is a positive integer
    if float(lst_ip[2]) == int(float(lst_ip[2])) and int(float(lst_ip[2])) > 0:
        length = int(float(lst_ip[2]))
        # print(f'length = {length}')
    else:
        check = False
    
    if check:
        for i in range(length):
            print(char,end='')
            if i < length - 1:
                print("-",end='')
            char = chr(((ord(char) - 97 + step) % 26) + 97)
        print("")
except:
    ...

#using function(def) will be easier for error handling