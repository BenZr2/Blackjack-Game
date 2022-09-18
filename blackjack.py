import random
# Cards: 2 3 4 5 6 7 8 9 10 B D K A (52 cards)

print("                               ")
print("   _____    Blackjack          ")
print("  |A .  | _____                ")
print("  | /.\ ||A ^  | _____         ")
print("  |(_._)|| / \ ||A _  | _____  ")
print("  |  |  || \ / || ( ) ||A_ _ | ")
print("  |____V||  .  ||(_'_)||( v )| ")
print("         |____V||  |  || \ / | ")
print("                |____V||  .  | ")
print("                       |____V| ")


card_deck = []

card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'B': 10,
    'D': 10,
    'K': 10,
    'A': 11,
}


def refresh_card_deck():
    card_deck = []
    for card in card_values:
        for i in range(4):
            card_deck.append(card)
    return card_deck


def draw_random_card():
    card = random.choice(card_deck)
    card_deck.remove(card)
    return card


def sum_of_str_array(arr):
    sum = 0
    for char in arr:
        sum += card_values[char]
    return sum


money = 2500

# Start of game loop
while money > 0:
    print("\nYour money: " + str(money) + "€")
    try:
        bet = int(input("How much do you want to bet? "))
    except:
        bet = 100
        print("Invalid input. Your bet is now: " + str(bet))
    if bet > money:
        print("You cant bet more money than you have. Bet: " + str(money))
        bet = money
    card_deck = refresh_card_deck()
    # print(card_deck)
    player_cards = []
    dealer_cards = []
    for _ in range(2):
        player_cards.append(draw_random_card())
        dealer_cards.append(draw_random_card())
    print("\nYour cards: " + str(player_cards))
    player_cards_sum = sum_of_str_array(player_cards)
    print("Your value: " + str(player_cards_sum))
    print("Dealer card: " + dealer_cards[0])
    dealer_cards_sum = sum_of_str_array(dealer_cards)
    # print(dealer_cards_sum)
    choice = ""

    while choice != "stand" and player_cards_sum < 21:
        choice = input("\nDo you want to hit or stand? ")
        if choice == "hit":
            player_cards.append(draw_random_card())
            print("Your cards: " + str(player_cards))
            player_cards_sum = sum_of_str_array(player_cards)
            if player_cards_sum > 21 and 'A' in player_cards:
                player_cards_sum -= 10
            print("Your value: " + str(player_cards_sum))

    while dealer_cards_sum < player_cards_sum and player_cards_sum <= 21:
        dealer_cards.append(draw_random_card())
        dealer_cards_sum = sum_of_str_array(dealer_cards)

    print(player_cards_sum, dealer_cards_sum)
    if (dealer_cards_sum < player_cards_sum <= 21) or dealer_cards_sum > 21:
        print("You have won")
        money += bet
    else:
        print("You lost")
        money -= bet
