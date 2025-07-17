星座名 = [' ','山羊座', '水瓶座', '魚座', '牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座']

print("Please enter your 生まれ月 (1–12):")
userinput = int(input())

if userinput == 1:
    print(f"Your 星座 is {星座名[0]}!")
elif userinput == 2:
    print(f"Your 星座 is {星座名[1]}!")
elif userinput == 3:
    print(f"Your 星座 is {星座名[2]}!")
elif userinput == 4:
    print(f"Your 星座 is {星座名[3]}!")
elif userinput == 5:
    print(f"Your 星座 is {星座名[4]}!")
elif userinput == 6:
    print(f"Your 星座 is {星座名[5]}!")
elif userinput == 7:
    print(f"Your 星座 is {星座名[6]}!")
elif userinput == 8:
    print(f"Your 星座 is {星座名[7]}!")
elif userinput == 9:
    print(f"Your 星座 is {星座名[8]}!")
elif userinput == 10:
    print(f"Your 星座 is {星座名[9]}!")
elif userinput == 11:
    print(f"Your 星座 is {星座名[10]}!")
elif userinput == 12:
    print(f"Your 星座 is {星座名[11]}!")
else:
    print("あなたの生まれ月は存在していません")  


