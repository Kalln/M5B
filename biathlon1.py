from random import randint

def splash():
    print("""
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  Biathlon
                  
             a hit or miss game
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    """)
    
def open():
    return 0


def closed():
    return 1

def is_open(target):
    if target == open():
        return True
    else: return False
    
def is_closed(target):
    if taget == closed():
        return True
    else: return False
    
def new_targets():
    targets = []
    for _ in range(5):
        targets.append(open())
    return targets
    
def close_target(target, targets):
    targets[target] = closed()

def hits(targets):
    n = 0
    for x in targets:
        if x == closed():
            n = n + 1
    return n

def target_to_string(target):
    if is_open(target):
        return "* "
    elif is_closed(target):
        return "O "
   
def targets_to_string(targets):
    # Konvertera 0 och 1 till * och O för att det ska
    # bli lättare att läsa för användaren.
    s = ""
    for target in targets:
        s = s + target_to_string(target)
    return s

def view_targets(targets):
    print(f"""
    
    0 1 2 3 4
    
    {targets_to_string(targets)}
    
    """)

def random_hit():
    if randint(0, 1) == 1:
        return True
    else: return False
    
        
def shoot(targets, target):
    if random_hit() == True:
        if is_open(targets[target]) = True:
            close_target(target, targets)
            return "hit on open target"
        else: return "hit on closed target"
    else: return "miss"
    
    
    
    
    
    
    
    
    