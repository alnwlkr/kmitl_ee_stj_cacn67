#Permutation รับเลขจำนวนเต็ม 2 จำนวน คำนวนหา Permutation P(n,r) โดย n>r
#Pnr = n!/(n - r)!

ip = input("Enter n,r to Permute: ")
lst_ip = ip.split()

if len(lst_ip) == 2:
    try:
        n = int(lst_ip[0])
        r = int(lst_ip[1])

        if n > r:
            # Compute Pnr
            n_frac = 1
            # Compute n_frac by starting at n and decrease until 1
            for i in range(n,0,-1):
                n_frac = n_frac * i
            # print(n_frac)
            # Compute n-r frac
            nr_frac = 1
            for i in range(n-r,0,-1):
                nr_frac = nr_frac * i
            # print(nr_frac)
            pnr = n_frac / nr_frac
            print(f'P({n},{r}) = {pnr:.0f}')

    except:
        ...