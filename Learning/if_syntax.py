dayType = 2

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType ==2:
    pass
else:
    pass
#dziwna notacja do przetwarzania danych:
dayDescription = 'weekend' if dayType == 1 else "workday" if dayType == 2 else "holiday"
print(dayDescription)