import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def draw():
    return random.choice(cards)
def play():
    player_score=0
    dealer_score=0
    players=[]
    dealer=[]
    for i in range(2):
        card=draw()
        if card==11:
            if player_score>10:
                players.append(1)
                player_score+=1
            else:
                players.append(card)
                player_score+=card
        else:
            players.append(card)
            player_score+=card
        card=draw()
        dealer.append(card)
        dealer_score+=card

    print(f"Your cards:{players}, current score : {player_score}")
    print(f"Computer's first card: {dealer[0]}")
    continue_play=True
    while continue_play:
        ask=input("Type 'y' to get another card, type 'n' to pass:")
        if ask=='y':
            card=draw()
            players.append(card)
            player_score+=card
            if player_score>21:
                print(f"Your cards:{players}, current score : {player_score}")
                print(f"Computer's first card: {dealer[0]}")
                print(f"Your final:{players}, final score : {player_score}")
                print(f"Computer's final card: {dealer},final score {dealer_score}")
                print("You went over. You lose")
                break
            else:
                print(f"Your cards:{players}, current score : {player_score}")
                print(f"Computer's first card: {dealer[0]}")
        if ask=='n':
            continue_play=False
            while dealer_score<17:
                card=draw()
                dealer.append(card)
                dealer_score+=card
            if dealer_score<=21:
                if player_score>dealer_score:
                    print(f"Your cards:{players}, current score : {player_score}")
                    print(f"Computer's first card: {dealer[0]}")
                    print(f"Your final:{players}, final score : {player_score}")
                    print(f"Computer's final card: {dealer},final score {dealer_score}")
                    print("You win")
                    break
                elif player_score<dealer_score:
                    print(f"Your cards:{players}, current score : {player_score}")
                    print(f"Computer's first card: {dealer[0]}")
                    print(f"Your final:{players}, final score : {player_score}")
                    print(f"Computer's final card: {dealer},final score {dealer_score}")
                    print("Dealer's score is more. You lose")
                    break
                else:
                    print(f"Your cards:{players}, current score : {player_score}")
                    print(f"Computer's first card: {dealer[0]}")
                    print(f"Your final:{players}, final score : {player_score}")
                    print(f"Computer's final card: {dealer},final score {dealer_score}")
                    print("DRAW")
                    break
            else:
                print(f"Your cards:{players}, current score : {player_score}")
                print(f"Computer's first card: {dealer[0]}")
                print(f"Your final:{players}, final score : {player_score}")
                print(f"Computer's final card: {dealer},final score {dealer_score}")
                print("You win")
                break
while input("Type 'y' to play, type 'n' to pass:")=='y':
    play()