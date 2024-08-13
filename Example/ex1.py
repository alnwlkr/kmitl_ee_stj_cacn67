#Example I – DC Power Calculator

ip = input("Enter V I : ")
v, i = ip.split()
v = float(v)
i = float(i)
# print(ip.split())
p = v*i
print(f'V = {v:.3f} Volts')
print(f'A = {i:.3f} Amperes')
print(f'P = {p:.3f} Watts')
