import random
options=("rock","papper","scissors")
playing=True
print('''
<-----==================---->
WINNING RULES OF ROCK PAPPER SCISSORS 
ROCK VS PAPPER --> PAPPER WINS
ROCK VS SCISSORS-->  ROCK WINS 
PAPPER VS SCISSORS--> SCISSORS WINS
<-----==================---->

''')
while playing:
    player_turn = None
    while player_turn not in options:
        player_turn = input("ENTER A CHOICE (rock ,papper,scissors)")
    computer_turn = random.choice(options)
    print(f"PLAYER CHOICE {player_turn}")
    print(f"COMPUTER CHOICE {computer_turn}")
    if player_turn == computer_turn:
        print('''
        .....<<<<<<< MATCH TIE  >>>>>>.....
        ''')
    elif player_turn == "rock" and computer_turn == "scissors":
        print("(: (: you wins (: (:")
    elif player_turn == "rock" and computer_turn == "papper":
        print("(: (: you wins (: (:")
    elif player_turn == "scissors" and computer_turn == "papper":
        print("(: (: you wins (: (:")
    else:
        print(":( :( you lose :( :(")
    if not input("Play again y/n :").lower() == 'y':
        playing = False

print("(: (: thanks for playing(: (:")

