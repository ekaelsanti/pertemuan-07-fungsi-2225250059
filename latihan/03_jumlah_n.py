# Latihan 3: Akumulasi Jumlah 1 sampai n
def jumlah_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Pengujian test case n = 1, 5, 10, 100
for val in [1, 5, 10, 100]:
    print(f"Jumlah 1..{val} = {jumlah_n(val)}")