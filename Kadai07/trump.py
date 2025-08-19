import random

suits = ['ハート', 'スペード', 'ダイヤ', 'クラブ']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = []
for s in suits:
    for v in values:
        deck.append(v + " of " + s)

print("選んだカード:")
for i in range(5):
    card = random.choice(deck)
    print(card)

