import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
	'''
	class for a Card
	'''
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank+" of "+self.suit

class Deck:
	'''
	class for a Card this class has a list of 52 cards
	'''
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand:
	'''
	class to represent the dealer and the player
	'''
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1
		
	def adjust_for_aces(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1
			
class Chips:
	''' 
	class for Chips 
	'''
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

#all the functioon definitions

def take_bet(chips):
	'''
	function to take bets
	'''
	while True:
		try:
			chips.bet = int(input("Enter the number of chips you want to bet "))
		except ValueError:
			print("Please enter the correct number format ")
		else:
			if chips.bet > chips.total:
				print("Sorry, your bet can't exceed ", chips.total)
			else:
				break

def hit(deck, hand):
	'''
	functionto take a hit
	'''
	hand.add_card(deck.deal())
	hand.adjust_for_aces()
	
def hit_or_stand(deck, hand):
	'''
	function to take a hit or stand
	'''
	global playing
	while True:
		choice = input("Do you want to hit or stand? Enter 'h' or 's' ")
		if choice[0].lower() == 'h':
			hit(deck, hand)
		elif choice[0].lower() == 's':
			print("Player standing, the dealer will continue ")
			playing = False
		else:
			print("Sorry, try again ")
			continue
		break
	
def show_some(player, dealer):
	'''
	show some cards
	'''
	print("\nDealer's Hand:")
	print(" <card hidden>")
	print('',dealer.cards[1])  
	print("\nPlayer's Hand:")
	for card in player.cards:
		print(card)
    
def show_all(player, dealer):
	'''
	show all cards
	'''
	print("\nDealer's Hand:")
	for card in dealer.cards:
		print(card)
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:")
	for card in player.cards:
		print(card)
	print("Player's Hand =",player.value)
	
def player_busts(player,dealer,chips):
	print("Player busts!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("Player wins!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Dealer busts!")
	chips.win_bet()
    
def dealer_wins(player,dealer,chips):
	print("Dealer wins!")
	chips.lose_bet()
    
def push(player,dealer):
	print("Dealer and Player tie! It's a push.")


'''
main program
'''
while True:
	# Print an opening statement
	print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
	Dealer hits until she reaches 17. Aces count as 1 or 11.')

	# Create & shuffle the deck, deal two cards to each player
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())
	    
	# Set up the Player's chips
	player_chips = Chips()  # remember the default value is 100    

	# Prompt the Player for their bet
	take_bet(player_chips)

	# Show cards (but keep one dealer card hidden)
	show_some(player_hand,dealer_hand)
	while playing:  # recall this variable from our hit_or_stand function
        
		# Prompt for Player to Hit or Stand
		hit_or_stand(deck,player_hand) 
		
		# Show cards (but keep one dealer card hidden)
		show_some(player_hand,dealer_hand)  
		
		# If player's hand exceeds 21, run player_busts() and break out of loop
		if player_hand.value > 21:
		    player_busts(player_hand,dealer_hand,player_chips)
		    break
	# If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
	if player_hand.value <= 21:

		while dealer_hand.value < 17:
		    hit(deck,dealer_hand)    

		# Show all cards
		show_all(player_hand,dealer_hand)

		# Run different winning scenarios
		if dealer_hand.value > 21:
		    dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
		    dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
		    player_wins(player_hand,dealer_hand,player_chips)

		else:
		    push(player_hand,dealer_hand)
	# Inform Player of their chips total 
	print("\nPlayer's winnings stand at",player_chips.total)

	# Ask to play again
	new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

	if new_game[0].lower()=='y':
		playing=True
		continue
	else:
		print("Thanks for playing!")
		break
