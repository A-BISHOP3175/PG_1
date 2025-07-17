import random 

luckynum = random.randint(1, 10)

guess = int(input("1から10までの数字を一つ当ててください："))

if guess < luckynum:
    print("違う！数字は　↑　")
elif guess > luckynum:
    print("違う！数字　↓　")
else:
    print("当たりです！")
