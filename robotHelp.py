# Fatto da Davide Barbini

# Posizione iniziale
pos = [[6, 6]]

# DIREZIONI:
# Sud è [0, -1]
# Est è [1, 0]
# Nord è [0, 1]
# Ovest è [-1, 0]
direc = [[0, -1]]

poss_cmd = ["f", "a", "o"]
def move(commands=""):
    commands = list(commands.lower().split(","))
    for cmd in commands:
        if cmd in poss_cmd:
            # Command list is to make a copy
            direc.append(list(direc[-1]))
            pos.append(list(pos[-1]))

            if cmd == "f":
                pos[-1][0] += direc[-1][0]
                pos[-1][1] += direc[-1][1]

            elif cmd == "o":
                direc[-1][1], direc[-1][0] = -direc[-1][0], direc[-1][1]

            elif cmd == "a":
                direc[-1][1], direc[-1][0] = direc[-1][0], -direc[-1][1]

        else:
            print("Something went wrong: command unknown")
            return

        print(str(pos[-1]) + get_dir(direc[-1]))

def get_dir(direction=[]):
    if direction == [0, -1]:
        return "↓"
    elif direction == [-1, 0]:
        return "←"
    elif direction == [0, 1]:
        return "↑"
    elif direction == [1, 0]:
        return "→"

# Utilizzo: move('lista_comandi')
move("f,f,a,f,f,a,f,f,a,f,f,o,f,f,o,f,f,o,f,o")

# Oppure puoi dare comando per comando
while True:
    cmd = input("Enter command: ")
    if cmd == "undo":
        if len(pos) > 1:
            pos.pop()
            direc.pop()
        else:
            print("Cannot undo anymore")
    elif cmd == "reset":
        pos = [pos[0]]
        direc = [direc[0]]
    else:
      move(cmd)
