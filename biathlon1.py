# Vi importerar från biblioteket "random" funktionen randint(a, b) som
# genererar ett slumpmässigt heltal mellan a och b.

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

# is_open och is_closed tar ett argument: målet (target)
# Den kontrollerar om målet är öppet eller stängt i resp. funktion
# genom att kontrollera om den är lika med open() resp. closed()
def is_open(target):
    if target == open():
        return True
    else: return False
    
def is_closed(target):
    if target == closed():
        return True
    else: return False
    
# Genererar en ny lista med fem nya måltavlor som är öppna. 
def new_targets():
    targets = []
    for _ in range(5):
        targets.append(open())
    return targets
    
# Tar en tavla (targets) och ett index i den här tavlan (target).
# close_target ändrar värdet på de valda indexet till closed()
def close_target(target, targets):
    targets[target] = closed()

# Räknar antal träffar genom att kontrollera vilka mål som är stängda. 
def hits(targets):
    n = 0
    for x in targets:
        if x == closed():
            n = n + 1
    return n

# tar ett mål (target) och omvandlar denna till ett tecken beroende på om den är
# stängd eller öppen. Detta gör vi för att det ska vara mer visuellt för användaren.
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

# 50/50 chans att vi träffar. Om det slumpmässiga talet blir 1
# har vi träffat.
def random_hit():
    if randint(0, 1) == 1:
        return True
    else: return False
    
# 1. Kontrollera om vi träffat genom random_hit().
# 2. om random_hit() ger tillbaka True betyder det att skottet
# har träffat. 
# 3. Kontrollera om målet som vi vill skjuta på är stängt.
# 4. Om ja, träff och vi skriver att det var en träff på öppet mål.
# 5. Om nej, träff men vi skriver attt det var en träff på stängt mål.        
def shoot(targets, target):
    if random_hit() == True:
        if is_open(targets[target]) == True:
            close_target(target, targets)
            return "hit on open target"
        else: return "hit on closed target"
    else: return "miss"
    
    
