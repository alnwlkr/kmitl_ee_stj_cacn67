# input => char step length
# chat => single character (only lowercase)
# step => positive intger
# length => number of character to disp

# get input from user
print(" *** Alphabet Sequence (a-z) ***")
lst_ip = input("Enter character step length : ").split()
# lst_ip = ['a', '3', '26']
try:
    char = lst_ip[0]
    step = int(lst_ip[1])
    length = int(lst_ip[2])
    
    for i in range(length):
        print(char,end='')
        if i < length - 1:
            print("-",end='')
        char = chr(((ord(char) - 97 + step) % 26) + 97)
    print("")
except:
    ...