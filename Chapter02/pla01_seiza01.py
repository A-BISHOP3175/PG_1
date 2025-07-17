astro = ["", "山羊座", "水瓶座", "魚座", "牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座"]
month = int(input("生まれた月を入力してください"))
day = int(input("生まれた日を入力してください"))
seiza = month - 1
if month == 1 and day>= 20: #山羊座
    month+= 1
elif month == 2 and day>= 20: #水瓶座
    month+= 1
elif month == 3 and day>= 20: #魚座
    month+= 1
elif month == 4 and day>= 20: #牡羊座
    month+= 1
elif month == 5 and day>= 20: #牡牛座
    month+= 1
elif month == 6 and day>= 20: #双子座
    month+= 1
elif month == 7 and day>= 20: #蟹座
    month+= 1
elif month == 8 and day>= 20: #獅子座
    month+= 1
elif month == 9 and day>= 20: #乙女座
    month+= 1
elif month == 10 and day>= 20: #天秤座
    month+= 1
elif month == 11 and day>= 20: #蠍座
    month+= 1
else month == 12 and day>= 20: #射手座
    month+= 1

print(month)
print(day)
print("あなたの星座は{astro[seiza]}です")

　

