# IMPORTS
import pygame
import random

# SCREEN VARIABLES
WIDTH, HEIGHT = 650, 550
run = True

# COLORS
BLACK = (0,0,0)
DARK_GREY = (60,60,60)

# PLAYERS
players = []
cur_player = 0

# IMAGES
red0 = {"image": pygame.image.load("imgs/Red0.png"),"action":0,"color":"red"}
red1 = {"image": pygame.image.load("imgs/Red1.png"),"action":1,"color":"red"}
red2 = {"image": pygame.image.load("imgs/Red2.png"),"action":2,"color":"red"}
red3 = {"image": pygame.image.load("imgs/Red3.png"),"action":3,"color":"red"}
red4 = {"image": pygame.image.load("imgs/Red4.png"),"action":4,"color":"red"}
red5 = {"image": pygame.image.load("imgs/Red5.png"),"action":5,"color":"red"}
red6 = {"image": pygame.image.load("imgs/Red6.png"),"action":6,"color":"red"}
red7 = {"image": pygame.image.load("imgs/Red7.png"),"action":7,"color":"red"}
red8 = {"image": pygame.image.load("imgs/Red8.png"),"action":8,"color":"red"}
red9 = {"image": pygame.image.load("imgs/Red9.png"),"action":9,"color":"red"}
red_reverse = {"image": pygame.image.load("imgs/RedReverse.png"),"action":"reverse","color":"red"}
red_skip = {"image": pygame.image.load("imgs/RedSkip.png"),"action":"skip","color":"red"}
red_two = {"image": pygame.image.load("imgs/RedTwo.png"),"action":"+2","color":"red"}

yellow0 = {"image": pygame.image.load("imgs/Yellow0.png"),"action":0,"color":"yellow"}
yellow1 = {"image": pygame.image.load("imgs/Yellow1.png"),"action":1,"color":"yellow"}
yellow2 = {"image": pygame.image.load("imgs/Yellow2.png"),"action":2,"color":"yellow"}
yellow3 = {"image": pygame.image.load("imgs/Yellow3.png"),"action":3,"color":"yellow"}
yellow4 = {"image": pygame.image.load("imgs/Yellow4.png"),"action":4,"color":"yellow"}
yellow5 = {"image": pygame.image.load("imgs/Yellow5.png"),"action":5,"color":"yellow"}
yellow6 = {"image": pygame.image.load("imgs/Yellow6.png"),"action":6,"color":"yellow"}
yellow7 = {"image": pygame.image.load("imgs/Yellow7.png"),"action":7,"color":"yellow"}
yellow8 = {"image": pygame.image.load("imgs/Yellow8.png"),"action":8,"color":"yellow"}
yellow9 = {"image": pygame.image.load("imgs/Yellow9.png"),"action":9,"color":"yellow"}
yellow_reverse = {"image": pygame.image.load("imgs/YellowReverse.png"),"action":"reverse","color":"yellow"}
yellow_skip = {"image": pygame.image.load("imgs/YellowSkip.png"),"action":"skip","color":"yellow"}
yellow_two = {"image": pygame.image.load("imgs/YellowTwo.png"),"action":"+2","color":"yellow"}

blue0 = {"image": pygame.image.load("imgs/Blue0.png"),"action":0,"color":"blue"}
blue1 = {"image": pygame.image.load("imgs/Blue1.png"),"action":1,"color":"blue"}
blue2 = {"image": pygame.image.load("imgs/Blue2.png"),"action":2,"color":"blue"}
blue3 = {"image": pygame.image.load("imgs/Blue3.png"),"action":3,"color":"blue"}
blue4 = {"image": pygame.image.load("imgs/Blue4.png"),"action":4,"color":"blue"}
blue5 = {"image": pygame.image.load("imgs/Blue5.png"),"action":5,"color":"blue"}
blue6 = {"image": pygame.image.load("imgs/Blue6.png"),"action":6,"color":"blue"}
blue7 = {"image": pygame.image.load("imgs/Blue7.png"),"action":7,"color":"blue"}
blue8 = {"image": pygame.image.load("imgs/Blue8.png"),"action":8,"color":"blue"}
blue9 = {"image": pygame.image.load("imgs/Blue9.png"),"action":9,"color":"blue"}
blue_reverse = {"image": pygame.image.load("imgs/BlueReverse.png"),"action":"reverse","color":"blue"}
blue_skip = {"image": pygame.image.load("imgs/BlueSkip.png"),"action":"skip","color":"blue"}
blue_two = {"image": pygame.image.load("imgs/BlueTwo.png"),"action":"+2","color":"blue"}

green0 = {"image": pygame.image.load("imgs/Green0.png"),"action":0,"color":"green"}
green1 = {"image": pygame.image.load("imgs/Green1.png"),"action":1,"color":"green"}
green2 = {"image": pygame.image.load("imgs/Green2.png"),"action":2,"color":"green"}
green3 = {"image": pygame.image.load("imgs/Green3.png"),"action":3,"color":"green"}
green4 = {"image": pygame.image.load("imgs/Green4.png"),"action":4,"color":"green"}
green5 = {"image": pygame.image.load("imgs/Green5.png"),"action":5,"color":"green"}
green6 = {"image": pygame.image.load("imgs/Green6.png"),"action":6,"color":"green"}
green7 = {"image": pygame.image.load("imgs/Green7.png"),"action":7,"color":"green"}
green8 = {"image": pygame.image.load("imgs/Green8.png"),"action":8,"color":"green"}
green9 = {"image": pygame.image.load("imgs/Green9.png"),"action":9,"color":"green"}
green_reverse = {"image": pygame.image.load("imgs/GreenReverse.png"),"action":"reverse","color":"green"}
green_skip = {"image": pygame.image.load("imgs/GreenSkip.png"),"action":"skip","color":"green"}
green_two = {"image": pygame.image.load("imgs/GreenTwo.png"),"action":"+2","color":"green"}

wild = {"image": pygame.image.load("imgs/Wild.png"),"action":"color","color":"black"}
wild_four = {"image": pygame.image.load("imgs/WildFour.png"),"action":"color +4","color":"black"}

deck = [red0,red0,red1,red1,red2,red2,red3,red3,red4,red4,red5,red5,red6,red6,red7,red7,red8,red8,red9,red9,red_reverse,red_reverse, red_skip, red_skip, red_two, red_two,yellow0,yellow0,yellow1,yellow1,yellow2,yellow2,yellow3,yellow3,yellow4,yellow4,yellow5,yellow5,yellow6,yellow6,yellow7,yellow7,yellow8,yellow8,yellow9,yellow9,yellow_reverse,yellow_reverse, yellow_skip, yellow_skip, yellow_two, yellow_two,green0,green0,green1,green1,green2,green2,green3,green3,green4,green4,green5,green5,green6,green6,green7,green7,green8,green8,green9,green9,green_reverse,green_reverse, green_skip, green_skip, green_two, green_two,blue0,blue0,blue1,blue1,blue2,blue2,blue3,blue3,blue4,blue4,blue5,blue5,blue6,blue6,blue7,blue7,blue8,blue8,blue9,blue9,blue_reverse,blue_reverse, blue_skip, blue_skip, blue_two, blue_two,wild,wild,wild,wild,wild_four,wild_four,wild_four,wild_four]
used = []
starter_card = False
wrapping = False