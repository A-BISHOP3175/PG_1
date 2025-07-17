import random

player_score = 5
luckynumber = random.randint(1, 10)

while True:
    guess = int(input("1から10までの一つの数字を当ててください: "))

    if guess == luckynumber:
        player_score += 10
        print("当たりです！スコア:", player_score)
        break
    else:
        player_score -= 1
        print("残念です！もう一度試してください。スコア:", player_score)

        if player_score <= 0:
            print("スコアが0になりました。ゲームオーバー。正解は", luckynumber)
            break

        
