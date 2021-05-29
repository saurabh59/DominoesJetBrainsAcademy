import random
from random import choice, shuffle


domino_set = []
double = [[x, y] for x in range(7) for y in range(7) if x == y]

for x in range(7):
    for y in range(x, 7):
        domino_set.append([x, y])
shuffle(domino_set)

def domino_score(a, b):
    dict_a = {}
    new_list = []
    for x in a:
        dict_a[tuple(x)] = str(ai_counter(a, b, x[0]) + ai_counter(a, b, x[1]))
    for key, value in dict_a.items():
        new_list.append([int(value), key])
    new_list.sort(reverse=-1)
    return new_list


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


def ai_counter(a, b, r):
    k = a + b
    open_list = []
    for x in k:
        for y in x:
            open_list.append(y)
    return open_list.count(r)


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
        counter = 0
        k = domino_score(computer, domino_snake)
        computer_input = list(k[counter][1])
        while True:
            if domino_snake[-1][1] in computer_input:
                if computer_input.index(domino_snake[-1][1]) == 0:
                    domino_snake.append(computer_input)
                else:
                    k = computer_input[0]
                    m = computer_input[1]
                    domino_snake.append([m, k])
                computer.remove(computer_input)
                status = "player"
                break
            elif domino_snake[0][0] in computer_input:
                if computer_input.index(domino_snake[0][0]) == 1:
                    domino_snake = [computer_input]+ domino_snake
                else:
                    k = computer_input[0]
                    m = computer_input[1]
                    domino_snake = [[m, k]] + domino_snake
                computer.remove(computer_input)
                counter = 0
                status = "player"
                break
            else:
                counter += 1
                if counter >= len(k):
                    if len(stock) > 0:
                        computer.append(stock[-1])
                        del stock[-1]
                        status = "player"
                        break
                    else:
                        break
                else:
                    computer_input = list(k[counter][1])
                    continue

