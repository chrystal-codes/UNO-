# IMPORTS
import pygame
import random
import variables as var

# CLASSES
class Card:
	def __init__(self, card):
		self.image = card["image"]
		self.action = card["action"]
		self.color = card["color"]
		self.incr = 0
		self.dragging = False
		self.rect = self.image.get_rect()

	def draw(self,screen):
		screen.blit(self.image,(self.rect.x,self.rect.y))

class Player:
	def __init__(self,name,turn):
		self.name = name
		self.hand = []
		self.turn = turn
		self.cur_card = 0
		self.rot = 30.0
		self.index = 0
		self.draw_hand()


	def draw_hand(self):
		add = 10
		for x in range(7):
			card = random.choice(var.deck)
			card_class = Card(card)
			card_class.rect.x = add
			card_class.rect.y = var.HEIGHT - 110
			self.hand.append(card_class)
			var.deck.remove(card)
			add += 64-10

	def add_card(self):
		card = random.choice(var.deck)
		card_class = Card(card)

		if len(self.hand) >= 1:
			# WRAPPING X POS
			if self.hand[-1].rect.x+65 >= var.WIDTH:
				card_class.rect.x = 10
				var.wrapping = True
			else:
				card_class.rect.x = self.hand[-1].rect.x + (64-10)
		else:
			card_class.rect.x = 10
		# WRAPPING Y POS
		if var.wrapping:
			card_class.rect.y = 14
		else:
			card_class.rect.y = var.HEIGHT - 110

		self.hand.append(card_class)
		var.deck.remove(card)

	def commands(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_d]:
			self.add_card()
		if key[pygame.K_SPACE]:
			var.cur_player += 1


	def show_hand(self,screen):
		for card in self.hand:
			card.draw(screen)

	def move_card(self,event):
		for card in self.hand:
			if card.dragging:
				mouse_x, mouse_y = event.pos
				card.rect.x = mouse_x + self.offset_x
				card.rect.y = mouse_y + self.offset_y

	def sel_card(self,event):
		for card in self.hand:
			mouse_x, mouse_y = event.pos
			if card.rect.collidepoint(event.pos):
				card.dragging = True
				self.offset_x = card.rect.x - mouse_x
				self.offset_y = card.rect.y - mouse_y

	def let_go(self,event):
		for card in self.hand:
			card.dragging = False

	def drop_card(self,box):
		for card in self.hand:
			if card.rect.colliderect(box):
				var.used.append(card)
				self.hand.remove(card)
				play = self.card_action()
				if play:
					var.cur_player += 1
				elif not play:
					var.used.remove(card)
					self.hand.append(card)

	def card_action(self):
		if var.used[-2].action == var.used[-1].action or var.used[-2].color == var.used[-1].color or var.used[-1].action == "color" or var.used[-1].action == "color +4":
			if var.used[-1].action == "reverse":
				print(f"BEFORE: {var.players}")
				var.players.sort(reverse=True,key=self.sort_players)
				print(f"AFTER: {var.players}")
			elif var.used[-1].action == "color":
				self.change_color(var.used[-1])
			elif var.used[-1].action == "+2":
				self.draw_cards(2)
			elif var.used[-1].action == "color +4":
				self.change_color(var.used[-1])
				self.draw_cards(4)
			elif var.used[-1].action == "skip":
				var.cur_player += 1
			return True
		else:
			var.used[-1].rect.x = self.hand[-1].rect.x+(64-10)
			var.used[-1].rect.y = var.HEIGHT -110	

	def draw_cards(self,num):
		for x in range(num):
			pos = var.cur_player+1
			if pos >= len(var.players):
				pos = 0
			var.players[pos].add_card()

	def change_color(self,card):
		colors = ["red","green","blue","yellow"]
		choice = input("What do you want to change the color to? [red,blue,green,yellow]")
		if choice.lower() not in colors:
			card.color = random.choice(colors)
			print("Color will be picked for you!")
		else:
			card.color = choice.lower()
		print(f"Color is now: {card.color}!")


	def sort_players(self,player):
		return player.turn


		

# FUNCTIONS


def register_players():
	while True:
		total = input("How many people will be playing?[2-6] ")
		if total.upper() == "-X":
			break
		if int(total) in range(2,6):
			for x in range(int(total)):
				name = input(f"What is the name of player {x+1}? ")
				player = Player(name,x+1)
				var.players.append(player)
			print("Thank You!")
			break
		else:
			print("Invalid Amount! Try Again!")

def check_turn():
	if var.cur_player >= len(var.players):
		var.cur_player = 0

def starter_card(screen,box):
	while not var.starter_card:
		card = random.choice(var.deck)
		card_class = Card(card)
		if card["action"] != "reverse" and card["action"] != "skip" and card["action"] != "+2" and card["action"] != "color" and card["action"] != "color +4":
			#screen.blit(card["image"],(box.x+18,box.y+12))
			var.deck.remove(card)
			var.used.append(card_class)
			var.starter_card = True
