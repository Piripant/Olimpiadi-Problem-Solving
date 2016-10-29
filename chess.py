# Fatto da Davide Barbini

import operator

moves_dict = {"nne": [1, 2], "sse": [1, -2], "nno": [-1, 2], "sso": [-1, -2], "ene": [2, 1], "ese": [2, -1], "ono": [-2, 1], "oso": [-2, -1]}

def set_moves(names=[]):
    dictio = moves_dict
    for name in names:
        dictio.pop(name)
    return list(dictio.values())

def init_chess(x=3, y=3):
    table = []
    for _ in range(y):
        table.append([0]*x)
    return table

def add_prize(chessboard, x, y, prize): # -1 Per aggiungere una cella interdetta
    chessboard[x-1][y-1] = prize

def sumvec(vec1, vec2):
    return [vec1[0] + vec2[0], vec1[1] + vec2[1]]

def toUserPos(pos):
    if type(pos[0]) != list:
        return [pos[0]+1, pos[1]+1]
    else:
        values = []
        for p in pos:
            values.append(toUserPos(p))
        return values

def toCompPos(pos):
    return [pos[0]-1, pos[1]-1]

def find_all_paths(chessboard, moves, pos, end_pos, searched=[], prize=0):
    returns = []
    if pos == end_pos:
        return toUserPos(searched + [pos]), prize + chessboard[pos[0]][pos[1]]

    for move in moves:
        next_pos = sumvec(pos, move)
        if next_pos[0] < len(chessboard[0]) and next_pos[0] >= 0 and next_pos[1] < len(chessboard) and next_pos[1] >= 0: # Le coordinate sono fuori dalla mappa?
            if next_pos not in searched and chessboard[next_pos[0]][next_pos[1]] != -1: # La cella era stata già cercata? O è interdetta?
                paths = find_all_paths(chessboard, moves, next_pos, end_pos, searched + [pos], prize + chessboard[pos[0]][pos[1]])
                if len(paths) != 0:
                    returns.append(paths) if type(paths) != list else returns.extend(paths)

    return returns

# Utilizzo: variablie_mosse = set_moves(['mossa_proibita1', 'mossa_proibita2', etc...])
moves = set_moves(['oso', 'sso', 'sse', 'ese'])

# Utilizzo: variabile_scacchiera = init_chess(lunghezza, altezza)
chessboard = init_chess(8, 8)

# Utilizzo: add_prize(chessboard, coordinate_x, coorditante_y, premio)
# Utilizzo per celle interdette: add_prize(chessboard, coordinate_x, coorditante_y, -1)
add_prize(chessboard, 3, 2, 5)
add_prize(chessboard, 3, 1, -1)

start_pos = toCompPos([1, 1])
end_pos = toCompPos([8, 8])

sortpaths = sorted(find_all_paths(chessboard, moves, start_pos, end_pos), key=operator.itemgetter(-1))

for path in sortpaths:
    print(path)
