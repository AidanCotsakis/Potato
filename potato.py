import pygame
import random
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
clock = pygame.time.Clock()

win_w = 1920
win_h = 1080
draw_w = 420
draw_h = 0

win = pygame.display.set_mode((win_w, win_h), pygame.FULLSCREEN)
pygame.display.set_caption("Potato")

_layout = pygame.image.load('layout.png')

_barrel4 = pygame.image.load('barrel1.png')
_barrel3 = pygame.image.load('barrel2.png')
_barrel2 = pygame.image.load('barrel3.png')
_barrel1 = pygame.image.load('barrel4.png')

_count1 = pygame.image.load('count1.png')
_count2 = pygame.image.load('count2.png')
_count3 = pygame.image.load('count3.png')
_count4 = pygame.image.load('count4.png')
_count5 = pygame.image.load('count5.png')
_count6 = pygame.image.load('count6.png')
_count7 = pygame.image.load('count7.png')
_count8 = pygame.image.load('count8.png')
_count9 = pygame.image.load('count9.png')
_count10 = pygame.image.load('count10.png')
_count11 = pygame.image.load('count11.png')
_count12 = pygame.image.load('count12.png')
_count13 = pygame.image.load('count13.png')
_count14 = pygame.image.load('count14.png')
_count15 = pygame.image.load('count15.png')
_count16 = pygame.image.load('count16.png')

_farm1 = pygame.image.load('farm1.png')
_farm2 = pygame.image.load('farm2.png')
_farm3 = pygame.image.load('farm3.png')
_farm4 = pygame.image.load('farm4.png')
_farm5 = pygame.image.load('farm5.png')
_farm6 = pygame.image.load('farm6.png')

_potato1 = pygame.image.load('potato1.png')
_potato2 = pygame.image.load('potato2.png')
_potato3 = pygame.image.load('potato3.png')

game = [
[50,50,50,50,50,50,50,50,50,50,50],
[50,0,10,0,10,0,20,0,20,0,50],
[50,10,10,0,10,0,20,0,20,20,50],
[50,0,0,0,10,0,20,0,0,0,50],
[50,11,12,0,10,0,20,0,22,21,50],
[50,0,13,0,10,0,20,0,23,0,50],
[50,11,12,0,10,0,20,0,22,21,50],
[50,0,0,0,10,0,20,0,0,0,50],
[50,10,10,0,10,0,20,0,20,20,50],
[50,0,10,0,10,0,20,0,20,0,50],
[50,50,50,50,50,50,50,50,50,50,50]
]

tilesize = 120
tick = 0
movmentdelay = 5
growdelay = 150
throwdelay = 2
potatos = []
potatoimpact = 3
offsetgap = 24

class player(object):
	def __init__(self, team, x, y,	direction):
		self.team = team
		self.x = x
		self.y = y
		self.direction = direction
		self.potato = 0
		self.offsetx = 0
		self.offsety = 0

	def moveup(self):
		self.direction = 0
		if game[self.y - 1][self.x] == 0:
			self.y -= 1

	def movedown(self):
		self.direction = 2
		if game[self.y + 1][self.x] == 0:
			self.y += 1

	def moveleft(self):
		self.direction = 1
		if game[self.y][self.x - 1] == 0:
			self.x -= 1

	def moveright(self):
		self.direction = 3
		if game[self.y][self.x + 1] == 0:
			self.x += 1

	def offsetup(self):
		self.direction = 0
		if game[self.y - 1][self.x] == 0:
			self.offsety -= offsetgap

	def offsetdown(self):
		self.direction = 2
		if game[self.y + 1][self.x] == 0:
			self.offsety += offsetgap

	def offsetleft(self):
		self.direction = 1
		if game[self.y][self.x - 1] == 0:
			self.offsetx -= offsetgap

	def offsetright(self):
		self.direction = 3
		if game[self.y][self.x + 1] == 0:
			self.offsetx += offsetgap

	def farm(self):
		if self.direction == 0:
			if (game[self.y - 1][self.x] == 10 or game[self.y - 1][self.x] == 20) and self.potato >= 1:
				if self.team == 0:
					game[self.y - 1][self.x] = 11
				if self.team == 1:
					game[self.y - 1][self.x] = 21
				self.potato -= 1

			if game[self.y - 1][self.x] == 13 or game[self.y - 1][self.x] == 23:
				if self.team == 0:
					game[self.y - 1][self.x] = 10
				if self.team == 1:
					game[self.y - 1][self.x] = 20
				self.potato += 2

		if self.direction == 2:
			if (game[self.y + 1][self.x] == 10 or game[self.y + 1][self.x] == 20) and self.potato >= 1:
				if self.team == 0:
					game[self.y + 1][self.x] = 11
				if self.team == 1:
					game[self.y + 1][self.x] = 21
				self.potato -= 1

			if game[self.y + 1][self.x] == 13 or game[self.y + 1][self.x] == 23:
				if self.team == 0:
					game[self.y + 1][self.x] = 10
				if self.team == 1:
					game[self.y + 1][self.x] = 20
				self.potato += 2

		if self.direction == 1:
			if (game[self.y][self.x - 1] == 10 or game[self.y][self.x - 1] == 20) and self.potato >= 1:
				if self.team == 0:
					game[self.y][self.x - 1] = 11
				if self.team == 1:
					game[self.y][self.x - 1] = 21
				self.potato -= 1

			if game[self.y][self.x - 1] == 13 or game[self.y][self.x - 1] == 23:
				if self.team == 0:
					game[self.y][self.x - 1] = 10
				if self.team == 1:
					game[self.y][self.x - 1] = 20
				self.potato += 2

		if self.direction == 3:
			if (game[self.y][self.x + 1] == 10 or game[self.y][self.x + 1] == 20) and self.potato >= 1:
				if self.team == 0:
					game[self.y][self.x + 1] = 11
				if self.team == 1:
					game[self.y][self.x + 1] = 21
				self.potato -= 1

			if game[self.y][self.x + 1] == 13 or game[self.y][self.x + 1] == 23:
				if self.team == 0:
					game[self.y][self.x + 1] = 10
				if self.team == 1:
					game[self.y][self.x + 1] = 20
				self.potato += 2

	def throw(self):
		if self.team == 0 and self.potato >= 1:
			potatos.append(potato(0,self.x,self.y))
			self.direction = 3
			self.potato	-= 1
		if self.team == 1 and self.potato >= 1:
			potatos.append(potato(1,self.x,self.y))
			self.direction = 1
			self.potato	-= 1

	def draw(self):
		if self.direction == 0:
			win.blit(_barrel2, (self.x * tilesize - tilesize + draw_w + self.offsetx,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.direction == 1:
			win.blit(_barrel3, (self.x * tilesize - tilesize + draw_w + self.offsetx,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.direction == 2:
			win.blit(_barrel4, (self.x * tilesize - tilesize + draw_w + self.offsetx,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.direction == 3:
			win.blit(_barrel1, (self.x * tilesize - tilesize + draw_w + self.offsetx,self.y * tilesize - tilesize + draw_h + self.offsety))

		if self.potato == 1:
			win.blit(_count1, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 2:
			win.blit(_count2, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 3:
			win.blit(_count3, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 4:
			win.blit(_count4, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 5:
			win.blit(_count5, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 6:
			win.blit(_count6, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 7:
			win.blit(_count7, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 8:
			win.blit(_count8, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 9:
			win.blit(_count9, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 10:
			win.blit(_count10, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 11:
			win.blit(_count11, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 12:
			win.blit(_count12, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 13:
			win.blit(_count13, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 14:
			win.blit(_count14, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato == 15:
			win.blit(_count15, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
		if self.potato >= 16:
			win.blit(_count16, (self.x * tilesize - tilesize + draw_w + self.offsetx ,self.y * tilesize - tilesize + draw_h + self.offsety))
player0 = player(0, 3, 5, 3)
player1 = player(1, 7, 5, 1)

class potato(object):
	def __init__(self, team, x, y):
	 	self.team = team
	 	self.x = x
	 	self.y = y

	def move(self):
		if self.team == 0:
			self.x += 1
			if player1.x == self.x and player1.y == self.y:
				player1.potato -= potatoimpact
				potatos.pop(potatos.index(self))
				if player1.potato < 0:
					player1.potato = 0
		if self.team == 1:
			self.x -= 1
			if player0.x == self.x and player0.y == self.y:
				player0.potato -= potatoimpact
				potatos.pop(potatos.index(self))
				if player0.potato < 0:
					player0.potato = 0
		if self.x == 0 or self.x == 10:
			potatos.pop(potatos.index(self))

	def draw(self):
		win.blit(_potato3, (self.x * tilesize - tilesize + draw_w,self.y * tilesize - tilesize + draw_h))


def draw():
	win.blit(_layout, (draw_w, draw_h))

	scanX = 0
	scanY = 0
	for row in game:
		for tile in row:
			if scanX >= 1 and scanX <= 11 and scanY >= 1 and scanY <= 11:
				if tile == 10 or tile == 20:
					win.blit(_farm1, (scanX * tilesize - tilesize + draw_w,scanY * tilesize - tilesize + draw_h))
				if tile == 11 or tile == 21:
					win.blit(_farm2, (scanX * tilesize - tilesize + draw_w,scanY * tilesize - tilesize + draw_h))
				if tile == 12 or tile == 22:
					win.blit(_farm3, (scanX * tilesize - tilesize + draw_w,scanY * tilesize - tilesize + draw_h))
				if tile == 13 or tile == 23:
					win.blit(_farm4, (scanX * tilesize - tilesize + draw_w,scanY * tilesize - tilesize + draw_h))
			scanX += 1
		scanY += 1
		scanX = 0
	
	player0.draw()
	player1.draw()

	for potatoT in potatos:
		potatoT.draw()

	pygame.display.update()


while True:
	clock.tick(30)
	tick += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_o:
				player1.throw()
			if event.key == pygame.K_e:
				player0.throw()
			if event.key == pygame.K_q:
				player0.farm()
			if event.key == pygame.K_u:
				player1.farm()

#player movement
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		player0.offsetleft()	
	if keys[pygame.K_d]:
		player0.offsetright()
	if keys[pygame.K_w]:
		player0.offsetup()
	if keys[pygame.K_s]:
		player0.offsetdown()

	if keys[pygame.K_l]:
		player1.offsetright()
	if keys[pygame.K_j]:
		player1.offsetleft()
	if keys[pygame.K_i]:
		player1.offsetup()
	if keys[pygame.K_k]:
		player1.offsetdown()

	if tick % movmentdelay == 0:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] or player0.offsetx < -60:
			player0.moveleft()
		if keys[pygame.K_d] or player0.offsetx > 60:
			player0.moveright()
		if keys[pygame.K_w] or player0.offsety < -60:
			player0.moveup()
		if keys[pygame.K_s] or player0.offsety > 60:
			player0.movedown()

		if keys[pygame.K_l] or player1.offsetx > 60:
			player1.moveright()
		if keys[pygame.K_j] or player1.offsetx < -60:
			player1.moveleft()
		if keys[pygame.K_i] or player1.offsety < -60:
			player1.moveup()
		if keys[pygame.K_k] or player1.offsety > 60:
			player1.movedown()

		player0.offsetx = 0
		player0.offsety = 0
		player1.offsetx = 0
		player1.offsety = 0

	if tick % growdelay == 0:
		scanX = 0
		scanY = 0
		for row in game:
			for tile in row:
				if (tile >= 11 and tile <= 12) or (tile >= 21 and tile <= 22):
					chance = random.randint(0, 6)
					if chance == 1:
						game[scanY][scanX] += 1
				scanX += 1
			scanY += 1
			scanX = 0

	if tick % throwdelay == 0:
		for potatoT in potatos:
			potatoT.move()
	
	draw()