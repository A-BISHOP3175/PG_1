# coin_change.py

amount = int(input("お釣りの金額を入力してください（円）: "))

# コインの計算
coin_100 = amount // 100
amount %= 100

coin_10 = amount // 10
amount %= 10

coin_1 = amount

# 結果の表示
print(f"100円玉: {coin_100} 枚")
print(f"10円玉: {coin_10} 枚")
print(f"1円玉: {coin_1} 枚")

