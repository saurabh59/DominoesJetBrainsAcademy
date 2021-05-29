import random
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


def game_win(p, c):
    if len(p) == 0:
        print("Status: The game is over. You won!")
        exit()
    elif len(c) == 0:
        print("Status: The game is over. The computer won!")
        exit()
    else:
        pass


def game_draw(k):
    checklist = []
    if k[0][0] == k[-1][1]:
        for x in k:
            for y in x:
                checklist.append(y)
        set_check = set(checklist)
        for x in set_check:
            counter = checklist.count(x)
            if counter >= 8:
                print("Status: The game is over. It's a draw!")
                exit()
    else:
        pass


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
domino_snake = []
if domino_computer > domino_player:
    status = "player"
    domino_snake.append(domino_computer[-1])
    computer.remove(domino_snake[-1])
else:
    status = "computer"
    domino_snake.append(domino_player[-1])
    player.remove(domino_snake[-1])
while True:
    print("======================================================================")
    print("Stock size:", len(stock))
    print("Computer pieces:", len(computer))
    print()
    if len(domino_snake) > 6:
        for x in domino_snake[0:3]:
            print(x, end="")
        print("...", end="")
        for x in domino_snake[-3::1]:
            print(x, end="")
    else:
        for x in domino_snake:
            print(x, end="")
    print()
    print()
    print("Your pieces:")
    count = 1
    for x in player:
        print(f"{count}:{x}")
        count += 1
    print()
    game_win(player, computer)
    game_draw(domino_snake)
    if status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
        player_input = input()
        while True:
            if player_input.lstrip('-').isnumeric():
                p = int(player_input)
                if abs(p) > len(player):
                    print("Invalid input. Please try again.")
                    player_input = input()
                    continue
                else:
                    if p != 0:
                        if p > 0:
                            if domino_snake[-1][1] in player[p - 1]:
                                if player[p - 1].index(domino_snake[-1][1]) == 0:
                                    domino_snake.append(player[p - 1])
                                else:
                                    k = player[abs(p) - 1][0]
                                    m = player[abs(p) - 1][1]
                                    domino_snake.append([m, k])
                                del player[p - 1]
                                status = "computer"
                                break
                            else:
                                print("Illegal move. Please try again.")
                                player_input = input()
                                continue
                        else:
                            if domino_snake[0][0] in player[abs(p) - 1]:
                                if player[abs(p) - 1].index(domino_snake[0][0]) == 1:
                                    domino_snake = [player[abs(p) - 1]] + domino_snake
                                else:
                                    k = player[abs(p) - 1][0]
                                    m = player[abs(p) - 1][1]
                                    domino_snake = [[m, k]] + domino_snake
                                del player[abs(p) - 1]
                                status = "computer"
                                break
                            else:
                                print("Illegal move. Please try again.")
                                player_input = input()
                                continue
                    else:
                        if len(stock) > 0:
                            player.append(stock[-1])
                            del stock[-1]
                            status = "computer"
                            break
                        else:
                            print("Illegal move. Please try again.")
                            player_input = input()
                            continue
            else:
                print("Invalid input. Please try again.")
                player_input = input()
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        dummy = input()
        computer_input = random.randint(-len(computer), len(computer))
        while True:
            if computer_input > len(computer):
                print("Invalid input. Please try again.")
                computer_input = random.randint(-len(computer), len(computer))
                continue
            else:
                if computer_input != 0:
                    if computer_input > 0:
                        if domino_snake[-1][1] in computer[computer_input - 1]:
                            if computer[computer_input - 1].index(domino_snake[-1][1]) == 0:
                                domino_snake.append(computer[computer_input - 1])
                            else:
                                k = computer[abs(computer_input) - 1][0]
                                m = computer[abs(computer_input) - 1][1]
                                domino_snake.append([m, k])
                            del computer[computer_input - 1]
                            status = "player"
                            break
                        else:
                            computer_input = random.randint(-len(computer), len(computer))
                            continue
                    else:
                        if domino_snake[0][0] in computer[abs(computer_input) - 1]:
                            if computer[abs(computer_input) - 1].index(domino_snake[0][0]) == 1:
                                domino_snake = [computer[abs(computer_input) - 1]] + domino_snake
                            else:
                                k = computer[abs(computer_input) - 1][0]
                                m = computer[abs(computer_input) - 1][1]
                                domino_snake = [[m, k]] + domino_snake
                            del computer[abs(computer_input) - 1]
                            status = "player"
                            break
                        else:
                            computer_input = random.randint(-len(computer), len(computer))
                            continue
                else:
                    if len(stock) > 0:
                        computer.append(stock[-1])
                        del stock[-1]
                        status = "player"
                        break
                    else:
                        print("Illegal move. Please try again.")
                        computer_input = random.randint(-len(computer), len(computer))
                        continue
