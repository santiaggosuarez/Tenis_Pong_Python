import pygame, sys
pygame.init()

#colores
black = (0,0,0)
white = (255,255,255)
background_color = (255,87,51)
background_score_color = (199, 0, 57)

#tamaños ventana
screen_width = 800
screen_height = 600
screen_size = (screen_width,screen_height)
#cargar imagen menu
menu_image = pygame.image.load("media/menu_con_texto_teclas.png")
menu_image_scale = pygame.transform.scale(menu_image, (screen_width, screen_height))
#cargar imagen ganador
winner_image = pygame.image.load("media/winner2.png")
winner_image_scale = pygame.transform.scale(winner_image, (screen_width, screen_height))
#tamaño marcador
background_score_height = screen_height*.1
#tamaño texto
text_size = round(background_score_height//2)
#cargar pelota
ball_image = pygame.image.load("media/ball_vector.png")

#icono y titulo ventana
pygame.display.set_caption("TENIS-PONG en PYTHON")
icon = pygame.image.load("media/ball_vector.png")
pygame.display.set_icon(icon)

#jugadores
player_width = 15
player_height = 90
player1_score = 0
player2_score = 0
player1_name = "Jugador 1"
player2_name = "Jugador 2"

#coordenadas y velocidad jugadores
player1_coor_x = 40
player1_coor_y = (screen_height+background_score_height)/2 - (player_height/2)
player1_speed_y = 0

player2_coor_x = 760 - player_width
player2_coor_y = (screen_height+background_score_height)/2 - (player_height/2)
player2_speed_y = 0

#coordenada y velocidad pelota
ball_x = screen_width/2
ball_y = (screen_height+background_score_height)/2
ball_speed_x = 5
ball_speed_y = 5
ball_width = 25
ball_height = 25
#pelota redimensionada
ball_image_scale = pygame.transform.scale(ball_image, (ball_width, ball_height))
#sonidos
ball_sound = pygame.mixer.Sound("media/ball_sound.mp3")
goal_sound = pygame.mixer.Sound("media/goal.mp3")
click_sound = pygame.mixer.Sound("media/click_sound.mp3")
winner_sound = pygame.mixer.Sound("media/winner.mp3")

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

exit = False
start = True

def menu_start(start,image,surface):
	surface.blit(image, (0,0))
	pygame.display.update()
	#rastreamos eventos
	for event in pygame.event.get():
		#para salir
		if event.type == pygame.QUIT:
			exit = True
			pygame.quit()
			sys.exit()
		#para empezar a jugar
		if event.type == pygame.KEYDOWN:
			click_sound.play()
			if event.key:
				return False
	#para que siga corriendo el juego
	return True

def pause(surface):
	paused = True
	while paused:
		#rastreamos eventos
		for event in pygame.event.get():
			#para salir
			if event.type == pygame.QUIT:
				exit = True
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				#para salir de pausa
				if event.key == pygame.K_SPACE:
					click_sound.play()
					paused = False
				#para salir por teclado
				elif event.key == pygame.K_ESCAPE:
					exit = True
					pygame.quit()
					sys.exit()
		#dibujo menu pausa
		text_pause1 = "JUEGO PAUSADO"
		text_pause2 = "Presiona 'ESPACIO' para reanudar"
		text_pause3 = "Presiona 'ESC' para salir"
		#draw_text(surface,text,size,color,x,y)
		draw_text(surface, text_pause1, text_size+20, white, (screen_width/2), (screen_height/4))
		pygame.display.update()
		draw_text(surface, text_pause2, text_size, white, (screen_width/2), (screen_height/1.5))
		pygame.display.update()
		draw_text(surface, text_pause3, text_size, white, (screen_width/2), (screen_height/1.4))
		pygame.display.update()

game_over = False
def winner(surface,player_win):
	game_over = True
	while game_over:
		#pelota y jugador vuelve al centro
		#coordenadas y velocidad jugadores
		player1_coor_x = 40
		player1_coor_y = (screen_height+background_score_height)/2 - (player_height/2)
		player1_speed_y = 0
		player2_coor_x = 760 - player_width
		player2_coor_y = (screen_height+background_score_height)/2 - (player_height/2)
		player2_speed_y = 0
		#coordenada y velocidad pelota
		ball_x = screen_width/2
		ball_y = (screen_height+background_score_height)/2
		ball_speed_x = 4
		ball_speed_y = 4
		player2_coor_x = 760 - player_width

		#rastreamos eventos
		for event in pygame.event.get():
			#para salir
			if event.type == pygame.QUIT:
				exit = True
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				#para reiniciar
				if event.key == pygame.K_SPACE:
					click_sound.play()
					game_over = False
				#para salir por teclado
				elif event.key == pygame.K_ESCAPE:
					exit = True
					pygame.quit()
					sys.exit()
		#dibujo ganador
		surface.blit(winner_image_scale,(0,0))
		text_winner1 = "GANADOR"
		text_winner2 = str(player_win)
		text_winner3 = "ESPACIO = Reanudar"
		text_winner4 = "    ESC = Salir   "
		#draw_text(surface,text,size,color,x,y)
		draw_text(surface, text_winner3, text_size, white, (screen_width/1.5), (screen_height/1.4))
		draw_text(surface, text_winner4, text_size, white, (screen_width/1.5), (screen_height/1.3))
		pygame.display.update()
		draw_text(surface, text_winner1, text_size+50, white, (screen_width/1.5), (screen_height/4))
		draw_text(surface, text_winner2, text_size+30, white, (screen_width/1.5), (screen_height/2.5))
		#utilice dos pygame.display.update() para que haya un efecto visual sobre "ganador"
		pygame.display.update()


def draw_text(surface,text,size,color,x,y):
	font = pygame.font.SysFont("consolas",size)
	text_surface = font.render(text,True,color)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surface.blit(text_surface, text_rect)

while not exit:
	#menu inicio
	while start:
		start = menu_start(start,menu_image_scale,screen)
	#rastrear eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
		#mover al presionar teclas
		if event.type == pygame.KEYDOWN:
			#jugador 1
			if event.key == pygame.K_w:
				player1_speed_y = -3
			if event.key == pygame.K_s:
				player1_speed_y = 3
			#jugador 2
			if event.key == pygame.K_UP:
				player2_speed_y = -3
			if event.key == pygame.K_DOWN:
				player2_speed_y = 3
			#pausar
			if event.key == pygame.K_SPACE:
				click_sound.play()
				pause(screen)

		# #no mover al soltar
		# if event.type == pygame.KEYUP:
		# 	#jugador 1
		# 	if event.key == pygame.K_w:
		# 		player1_speed_y = -0
		# 	if event.key == pygame.K_s:
		# 		player1_speed_y = 0
		# 	#jugador 2
		# 	if event.key == pygame.K_UP:
		# 		player2_speed_y = -0
		# 	if event.key == pygame.K_DOWN:
		# 		player2_speed_y = 0


	#---ZONA DE LOGICA
	#rebote de pelota contra los bordes superiores de la ventana
	if ball_y > (screen_height - ball_height) or ball_y < background_score_height:
		ball_speed_y *= -1
	#salida de la pelota (goles)
	if ball_x > screen_width:
		ball_x = screen_width/2
		ball_y = screen_height/2
		goal_sound.play()
		ball_speed_x *= -1
		ball_speed_y *= -1
		player1_score += 1
	if ball_x < (-1 * ball_width):
		ball_x = screen_width/2
		ball_y = screen_height/2
		goal_sound.play()
		ball_speed_x *= -1
		ball_speed_y *= -1
		player2_score += 1
	#rebota de los jugadores contra la ventana
	if player1_coor_y < background_score_height or player1_coor_y > (screen_height - player_height):
		player1_speed_y *= -1
	if player2_coor_y < background_score_height or player2_coor_y > (screen_height - player_height):
		player2_speed_y *= -1
	#dar movimiento a los jugadores y pelota
	player1_coor_y += player1_speed_y
	player2_coor_y += player2_speed_y

	ball_x += ball_speed_x
	ball_y += ball_speed_y
	#ganador jugador 1
	if player1_score == 10:
		winner(screen,player1_name)
		player1_score = 0
		player2_score = 0
	#ganador jugador 2
	if player2_score == 10:
		winner(screen,player2_name)
		player1_score = 0
		player2_score = 0
	#---ZONA DE LOGICA

	#background de la ventana
	screen.fill(background_color)
	#---zona de dibujo
	background_score = pygame.draw.rect(screen, background_score_color, pygame.Rect(0, 0, screen_width, background_score_height)) 

	player1 = pygame.draw.rect(screen, white, (player1_coor_x, player1_coor_y, player_width, player_height))
	player2 = pygame.draw.rect(screen, white, (player2_coor_x, player2_coor_y, player_width, player_height))
	center = pygame.draw.circle(screen, white, (screen_width/2, (screen_height+background_score_height)/2), 10)
	ball = screen.blit(ball_image_scale, [ball_x, ball_y])
	#---zona de dibujo

	#colisionoes
	if ball.colliderect(player1) or ball.colliderect(player2):
		ball_speed_x *= -1
		ball_speed_y *= -1
		ball_sound.play()

	#marcador
	text_score = player1_name + " (" + str(player1_score) + ")     |     (" + str(player2_score) + ") " + player2_name
	draw_text(screen, text_score, text_size, white, (screen_width/2), (background_score_height//3.5))
	#draw_text(surface,text,size,color,x,y)

	#actualiza ventana
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
sys.exit()