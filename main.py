# IMPORTS
import pygame
import variables as var
import methods as mth

# INITS
pygame.init()

# CREATE WINDOW
screen = pygame.display.set_mode((var.WIDTH,var.HEIGHT))
pygame.display.set_caption("UNO!")

collide_box = pygame.draw.rect(screen,var.DARK_GREY,(var.WIDTH//2-50,var.HEIGHT//2-60,100,120))

def draw_screen():
	screen.fill(var.BLACK)

	# DRAW COLLISION BOX
	collide_box = pygame.draw.rect(screen,var.DARK_GREY,(var.WIDTH//2-50,var.HEIGHT//2-60,100,120))

	# DRAW STARTING CARD
	mth.starter_card(screen,collide_box)

	for card in var.used:
		screen.blit(card.image,(collide_box.x+18,collide_box.y+12))

	# DRAW CARD
	var.players[var.cur_player].show_hand(screen)

	pygame.display.update()

def run_game():
	while var.run:
		
		for event in pygame.event.get():
			mth.check_turn()
			if event.type == pygame.QUIT:
				var.run = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				var.players[var.cur_player].commands()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				var.players[var.cur_player].sel_card(event)
				print(f"CUR PLAYER: {var.players[var.cur_player].name} CARDS:  {len(var.players[var.cur_player].hand)}")
			elif event.type == pygame.MOUSEBUTTONUP:
				var.players[var.cur_player].let_go(event)
				var.players[var.cur_player].drop_card(collide_box)
			elif event.type == pygame.MOUSEMOTION:
				var.players[var.cur_player].move_card(event)

				
		mth.check_turn()
		# DRAW TO SCREEN
		draw_screen()

# RUN GAME
if __name__ == "__main__":
	mth.register_players()
	run_game()
