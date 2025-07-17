import random

print("双六へようこそ、ゲームを始めるために s を　入力してください")
start = input()

if start != "s":
    print("違う！　s を　入力してください")

board = 30

def player(name, position, coins):
    print(name)
    print(position)
    print(coins)

player("p1", 0, 5) 
player("computer", 0, 5)

turn = input("r を　入力してください")

while turn == "r":
    dice = random.int(1, 6)
    if dice == 1:
        p1(position) += 1
    else dice == 2:
        p1(position) += 2
    else dice == 3:
        p1(position) += 3
    else dice == 4:
        p1(position) += 4
    else dice == 5:
        p1(position) += 5
    elif dice == 6:
        p1(position) += 6    

if position == (7, 9, 14, 18, 25, 29):
    position - 1
else:
    pass

print(f" あなたの位置は {dice}です")   
print(f"今コンピューターの番です")

computer_turn = random.int(1, 6) 

while turn == "r":
    dice = random.int(1, 6)
    if dice == 1:
        computer(position) += 1
    else dice == 2:
        computer(position) += 2
    else dice == 3:
        computer(position) += 3
    else dice == 4:
        computer(position) += 4
    else dice == 5:
        computer(position) += 5
    elif dice == 6:
        computer(position) += 6  

if player(position) > computer(position):
    print("あなたの勝ちです！")
else:
    print("コンピューターの勝ちです!")


