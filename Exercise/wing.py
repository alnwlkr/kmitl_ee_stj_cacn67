# 1
# **

# 4
# *------*
# **----**
# ***--***
# ********
# ***--***
# **----**
# *------*
symbol = '*'
space = ' '
try:
    n = int(input("Input : "))
    # n = 4
    i = 1
    j = 1
    while i <= (n*2)-1 :
        # print(i,' ',end='')
        print(symbol*j,sep='',end='')
        print(space*abs(2*n-2*i),sep='',end='')
        print(symbol*j,sep='')
        if i < n:
            j = j + 1
        else:
            j = j - 1
        i = i + 1

except:
    ...