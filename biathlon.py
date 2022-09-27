from random import randint

def splash():
    print("""
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Biathlon

            a hit or miss game
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """)
    return None

def open():
    return 0

def closed():
    return 1

def is_open(target):
    if target == open():
        return True
    else: return False

def is_closed(target):
    if target == closed():
        return True
    else: return False

def new_targets():
    new_target_list = []
    for _ in range(5):
        new_target_list.append(open())
    return new_target_list

def close_target(target, targets):
    # target - heltal mellan 0-4 som avgör vilken lucka vi vill stänga
    # targets - är en lista med fem element som representerar om måltavlan är stängd eller öppen
    targets[target] = closed()
    return targets

def hits(targets):
    i = 0
    for target in targets:
        if is_closed(target):
            i += 1
    return i

def target_to_string(target):
    if is_open(target):
        return "* "
    elif is_closed(target):
        return "0 "
    else: return None

def targets_to_string(targets):
    str_targets = ""
    for target in targets:
        str_targets = str_targets + f"{target_to_string(target)}"
    return str_targets

def view_targets(targets):
    print(f"""
    0 1 2 3 4
    
    {targets_to_string(targets)}
    """)
    return None

def random_hit():
    if randint(0, 1) == 1:
        return True
    else: return False

def shoot(targets, target):
    # Kolla först om skottet träffar. Om nej, var det miss (inget sker)
    # Om ja, kontrollerar vi om tavlan är öppen eller stängd.
    # och returnera värdet allt eftersom.
    # 
    if random_hit():
        if is_open(targets[target]):
            close_target(target, targets)
            return "Hit on open target"
        else: return "Hit on closed target"
    else: return "miss"
    
