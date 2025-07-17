#じゃんけんゲーム

import random 

handshape = ["p", "s", "r"]

com = random.choice(handshape)
player_guess = input("Welcome to PSR: pick your hand, P = Paper（パー）, S = Scissors　（チョキ） and R = Rock　（グー）")
print("Computer chose: ", com)

if player_guess == com:
    print("It's a tie! 同点")
elif (player_guess == "p" and com == "r") or \
     (player_guess == "r" and com == "s") or \
     (player_guess == "s" and com == "p"):
    print("You win!　勝ち")
else:
    print("You lose!　負けた")
