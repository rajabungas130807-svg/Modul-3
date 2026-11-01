n = int(input())

hari = n//3600//24
jam= n// 3600 % 24
menit = n % 3600 // 60
detik = n % 60

if hari>0:
    print(f"{hari} hari {jam:02d}:{menit:02d}:{detik:02d}")
else :
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")

