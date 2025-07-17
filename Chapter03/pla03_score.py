englishScore = int(input("英語試験の点数を入力してください: "))
mathScore = int(input("数学試験の点数を入力してください: "))

if englishScore >= 90 and mathScore >= 90:
    print("成績：S")
elif (70 <= englishScore < 70) or (70 <= mathScore < 90):
    print("成績：A")
elif (50 <= englishScore < 70)  and (50 <= mathScore < 70):
    print("成績：B")
else: 
    print("成績：C")

