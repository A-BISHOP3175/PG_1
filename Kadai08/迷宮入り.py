import random

# 容疑者、犯罪現場、凶器
suspects = ["田中", "嶋", "谷浦", "羽地"]
locations = ["台所", "和室", "庭", "図書館"]
weapons = ["ナイフ", "銃", "毒", "弓矢"]

# 正解をランダムに決定
murderer = random.choice(suspects)
murder_location = random.choice(locations)
murder_weapon = random.choice(weapons)

# ゲームスタート
print("==== 迷宮入り: Murder Mystery Game ====")
print("ジョンさんが殺人されました！事件を解きましょう！")
print("容疑者：", ", ".join(suspects))
print("犯罪現場：", ", ".join(locations))
print("凶器：", ", ".join(weapons))

clues_found = 0
while clues_found < 3:
    print("\n何をしますか？")
    print("1: 容疑者を尋問する")
    print("2: 現場を捜査する")
    print("3: 凶器を検査する")
    choice = input("1, 2, 3 を一つ選んで下さい: ")

    if choice == "1":
        suspect = random.choice(suspects)
        if suspect == murderer:
            print(f"{suspect} は緊張しているようで、答えに一貫性がありません...")
        else:
            print(f"{suspect} の主張はおかしくないようです。")

    elif choice == "2":
        loc = random.choice(locations)
        if loc == murder_location:
            print(f"{loc} で手掛かりが見つかりました！")
        else:
            print(f"{loc} では何も見つかりませんでした。")

    elif choice == "3":
        weap = random.choice(weapons)
        if weap == murder_weapon:
            print(f"{weap} に血痕が付いています！")
        else:
            print(f"{weap} は使われた証拠がありません。")

    else:
        print("無効な選択です。")
        continue

    clues_found += 1

# 最終推理
print("\n=== 事件を解く時間になりました ===")
guess_suspect = input("犯人は誰ですか？ ")
guess_location = input("犯罪現場はどこですか？ ")
guess_weapon = input("犯人はどの凶器を使いましたか？ ")

if (guess_suspect == murderer and
    guess_location == murder_location and
    guess_weapon == murder_weapon):
    print("当たりました! 事件を上手く解けました。犯人は逮捕されました。")
else:
    print("間違えました！ 事件はまだ迷宮入りです...")
    print(f"真実は: 犯人 {murderer}, 現場 {murder_location}, 凶器 {murder_weapon}.")

