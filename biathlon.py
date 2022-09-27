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

# is_open & is_closed ger antingen True eller False beroende på om 
# målet är öppet eller stängd. Är målet öppet och is_open() ropas
# så ger funktionen värdet "True" tillbaka.

def is_open(target):
    if target == open():
        return True
    else: return False

def is_closed(target):
    if target == closed():
        return True
    else: return False

def new_targets():
    # skapar fem nya element i en lista som representerar våra tavlor.
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
    # Kollar hur många hits vi har totalt i tavlan
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
    else: return

def targets_to_string(targets):
    # Konverterar 0 1 till mer representativa symboler för användaren.
    # funktionen används av "view_targets()"
    str_targets = ""
    for target in targets:
        str_targets = str_targets + f"{target_to_string(target)}"
    return str_targets

def view_targets(targets):
    # Gör tavlan mer läsbart för användaren.
    print(f"""
    1 2 3 4 5
    
    {targets_to_string(targets)}
    """)
    

def random_hit():
    # 50/50 chans att vi träffar målet.
    if randint(0, 1) == 1:
        return True
    else: return False

def shoot(targets, target):
    # Kolla först om skottet träffar. Om nej, var det miss (inget sker)
    # Om ja, kontrollerar vi om tavlan är öppen eller stängd.
    # och returnera värdet allt eftersom.
    if random_hit():
        if is_open(targets[target]):
            close_target(target, targets)
            return "Hit on open target"
        else: return "Hit on closed target"
    else: return "miss"
    
def parse_target(string):
    if string.isnumeric():
        # Om strängen är numerisk, så konverterar vi den till en int.
        int_target = int(string)
        if int_target <= 5 and int_target >= 1:
            return int_target - 1 
    return None
       

## game

def game():
    # initiera tavlan och antal skott
    ts = new_targets()
    i = 1
    splash()
    print("You got 5 shots")

    # While loopen körs tills i-värdet är 6. Värdet blir 6 efter 5 skott/körningar. 
    while i <= 5:
        view_targets(ts)
        user_input = parse_target(input(f"shot nr {i} at: "))

        # Kontrollerar att användaren ger ett godtyckligt värde, annars får användaren
        # prova igen.
        # Om värdet inte är None så skjuter vi skottet på det målet som användaren vill. 
        if user_input != None:
            print(shoot(ts, user_input))
            i += 1

    print(f"You hit {hits(ts)} of 5 targets")

game()
