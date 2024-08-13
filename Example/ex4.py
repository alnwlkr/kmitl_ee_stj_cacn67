#Example IV – Find the median

print("Enter Values : ", end='')
ip = input()
lst = []
while ip != "END":
    lst.append(float(ip))
    ip = input()

lst.sort()
print(lst)

len_lst = len(lst)
if len_lst % 2 == 0:
    med = (lst[(len_lst // 2) - 1] + lst[(len_lst // 2)]) / 2
    print(f'Median of {lst} is {med:.2f}')
else:
    med = lst[(len_lst) // 2]
    print(f'Median of {lst} is {med:.2f}')