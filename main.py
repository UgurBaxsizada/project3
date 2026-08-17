age=int(input("yasinizi daxil edin: "))
if 0<=age<=5:
    qiymet=0
elif 6<=age<=12:
    qiymet=50
elif 13<=age<=17:
    qiymet=80
elif 18<=age<=59:
    qiymet=120
elif 60<=age:
    qiymet=70
else:
    print("yasinizi duzgun daxil edin")

seyahet_tipi=input("seyahet tipi, bir terefli veya gedis-donus")
if seyahet_tipi=="bir terefli":
    qiymet=qiymet
elif seyahet_tipi=="gedis-donus":
    qiymet=qiymet*1.8
else:
    print("seyahet tipini duzgun daxil edin")

elave_baqaj=input("elave baqaj isteyirsiniz?xeyr,10kq,20kq,30kq: ")
if elave_baqaj=="xeyr":
    qiymet=qiymet
elif elave_baqaj=="10kq":
    qiymet=qiymet+10
elif elave_baqaj=="20kq":
    qiymet=qiymet+20
elif elave_baqaj=="30kq":
    qiymet=qiymet+30
else:
    print("duzgun daxil edin")

print(f'yekun qiymet={qiymet}azn')
