# Fatto da Davide Barbini

def add_rule(rule_index, out_var="", in_vars=[], rules={}):
    if out_var in in_vars:
        print("Invalid rule: output var is in input vars")
        return
    if rule_index not in rules:
        rules[rule_index] = [out_var, []]

    else:
        print("Warning, you might be overriding an existing rule, (maybe you forgot to change the rule's index?)")

    rules[rule_index][1] = in_vars

def order_rules(rules=[]):
    return sorted(rules, key=len)

def has_vars(list1=[], list2=[]):
    for e1 in list1: # Per ogni var necessaria
        if e1 not in list2: # Se la variabile non è conosciuta
            return False

    # Se raggiunge questo punto ha provato tutte le variabili
    return True

def find_all_paths(rules={}, end='', known_vars = [], searched_rules=[]):
    returns = []
    if end in known_vars:
        return searched_rules
    for rule_index in rules:
        rule = rules[rule_index]

        can_discover = has_vars(rule[1], known_vars)
        if rule_index not in searched_rules and can_discover: # Se non ha ancora cercato la regola e la variabile si puo dedurre
            paths = find_all_paths(rules, end, known_vars + [rule[0]], searched_rules + [rule_index])
            # Se paths è una lista deve essere una lista di percosi e deve essere usato extend, non append ex: [[1, 4, 6], [3, 5, 2]]
            # In caso contrario, deve usare append, perché contiene solo un percorso ex: [1, 2, 3]
            returns.append(paths) if type(paths[0]) != list else returns.extend(paths)


    return returns

rules = {}

# Utilizzo: add_rule(numero, variabile_da_ottenere, [variabile_conosciuta1, variabile_conosciuta2, etc...], dizionario_regole)

add_rule(1, 'a', ['b', 'c'], rules)
paths = find_all_paths(rules, 'a', ['b', 'c'])

# Utilizzo: find_all_paths(dizionario_regole, variabile_di_arrvio, [variabile_iniziale1, variabile_iniziale2])
paths = find_all_paths(rules, 'b', ['a', 'r', 'w'])
solutions = order_rules(paths)

print(solutions)
