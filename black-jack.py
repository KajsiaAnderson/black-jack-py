import random
card = random.randint(1, 11)

import random
card2 = random.randint(1, 11)

card_total = (card + card2)

count = 1
while card_total < 32:
    if card_total <21:
        print(card_total)
        print('Hit me again!')
    elif card_total == 21:
        print(card_total)
        print('You win, Mr. Vegas!')
        break
    elif card_total > 21:
        print(card_total)
        print('You busted!')
        card_total = 0
        count += 1
    card_total += random.randint(1, 11)
    card_total += 1
print('Games played: ', count)