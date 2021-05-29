from random import choice, shuffle


domino_set = []
double = [[x, y] for x in range(7) for y in range(7) if x == y]

for x in range(7):
    for y in range(x, 7):
        domino_set.append([x, y])
shuffle(domino_set)


def distribute(domino):
    computer_d = []
    player_d = []
    domino_dup = domino
    for k in range(7):
        computer_d.append(choice(domino))
        domino.remove(computer_d[k])
        player_d.append(choice(domino))
        domino.remove(player_d[k])
    return domino, domino_dup, computer_d, player_d


stock, domino_set, computer, player = distribute(domino_set)
domino_computer = []
domino_player = []

while not domino_computer and not domino_player:
    if any(x for x in double if x in computer):
        domino_computer = [value for value in computer if value in double]
    if any(x for x in double if x in player):
        domino_player = [value for value in player if value in double]
    else:
        shuffle(domino_set)
        stock, domino_set, computer, player = distribute(domino_set)
domino_computer.sort()
domino_player.sort()
if domino_computer > domino_player:
    status = "player"
    domino_snake = domino_computer[-1]
    computer.remove(domino_snake)
else:
    status = "computer"
    domino_snake = domino_player[-1]
    player.remove(domino_snake)
print("======================================================================")
print("Stock size:", len(stock))
print("Computer pieces:", len(computer))
print()
print(domino_snake)
print()
print("Your pieces:")
count = 1
for x in player:
    print(f"{count}:{x}")
    count += 1
print()
if status == "player":
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print("Status: Computer is about to make a move. Press Enter to continue...")
