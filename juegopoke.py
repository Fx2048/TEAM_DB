import csv
import pygame
from pygame.locals import *
import time
import math
import random
import sys
import os
from datetime import datetime
import requests
import io
from urllib.request import urlopen

pygame.init()

# create the game window
game_width = 500
game_height = 500
size = (game_width, game_height)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon')

# Fuentes
font = pygame.font.Font(None, 36)

# define colors
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)
background = pygame.image.load('fondo7.png')
background = pygame.transform.scale(background, (game_width, game_height))

# Variables para el Login
username = ""
is_logged_in = False
input_active = False

filename = 'usuarios.csv'

# base url of the API
base_url = 'https://pokeapi.co/api/v2'

def create_user_file(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["usuario"])  # Cabecera opcional

def create_log_file(log_filename):
    if not os.path.exists(log_filename):
        with open(log_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["fecha", "usuario"])

# Función para leer usuarios del CSV
def read_users_from_csv(filename):
    users = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        try:
            next(reader)  # Intentar saltar la cabecera si existe
        except StopIteration:
            return users  # Retorna la lista vacía si no hay filas

        for row in reader:
            users.append(row[0])
    return users

# Función para guardar un nuevo usuario en el CSV
def save_user_to_csv(username, filename):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp,username])  # Escribir el nuevo usuario
# Función para registrar cambios en el log
def log_change(username, action):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtener la fecha y hora actual
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, username, action])
# Función para mostrar la pantalla de login
def login_screen():
    global username, is_logged_in, input_active

    create_user_file(filename)  # Crear el archivo si no existe
    valid_users = read_users_from_csv(filename)  # Leer usuarios válidos
    create_log_file(filename)  # Crear el archivo de log si no existe

    while not is_logged_in:
        game.fill((255, 255, 255))  # Fondo blanco

        # Mostrar texto
        login_text = font.render("Login / Registro", True, (0, 0, 0))
        game.blit(login_text, (game_width // 2 - 100, 50))

        # Mostrar etiqueta "Usuario:"
        user_label = font.render("Usuario:", True, (0, 0, 0))
        game.blit(user_label, (game_width // 2 - 100, 150))  # Posición de la etiqueta

        # Rectángulo para el campo de entrada
        input_rect = pygame.Rect(game_width // 2 - 100, 200, 200, 40)
        pygame.draw.rect(game, (0, 0, 0), input_rect, 2)  # Contorno negro del rectángulo

        # Mostrar texto del usuario en el campo de entrada
        user_text = font.render(username, True, (0, 0, 0))
        game.blit(user_text, (input_rect.x + 5, input_rect.y + 5))  # Texto en el campo

        # Botón "Comienza"
        button_text = font.render("Empezar", True, (255, 255, 255))
        button_rect = pygame.Rect(game_width // 2 - 60, 300, 120, 50)
        pygame.draw.rect(game, (0, 0, 255), button_rect)  # Botón azul
        game.blit(button_text, (button_rect.x + 6, button_rect.y + 10))  # Texto en el botón

        pygame.display.flip()

        # Capturar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Presionar Enter
                    if username in valid_users:  # Validar credenciales
                        is_logged_in = True
                        log_change(username, "Inicio de sesión")  # Log de inicio de sesión
                    elif username:  # Si el usuario no existe, registrarlo
                        save_user_to_csv(username, filename)
                        log_change(username, "Registro")  # Log de registro
                        valid_users.append(username)  # Agregar a la lista local
                        is_logged_in = True  # Iniciar sesión después del registro
                elif event.key == pygame.K_BACKSPACE:  # Borrar el último carácter
                    username = username[:-1]

                # Agregar caracteres al nombre de usuario si el campo está activo
                if input_active and event.unicode.isprintable() and len(username) < 20:
                    username += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:  # Manejar clics del mouse
                if event.button == 1:  # Clic izquierdo
                    if input_rect.collidepoint(event.pos):  # Si el clic es en el campo de entrada
                        input_active = True  # Activar el campo de entrada
                    else:
                        input_active = False  # Desactivar el campo si se hace clic fuera

                    if button_rect.collidepoint(event.pos):  # Si el botón es clickeado
                        if username in valid_users:  # Validar credenciales
                            is_logged_in = True
                            log_change(username, "Inicio de sesión")  # Log de inicio de sesión
                        elif username:  # Si el usuario no existe, registrarlo
                            save_user_to_csv(username, filename)
                            log_change(username, "Registro")  # Log de registro
                            valid_users.append(username)  # Agregar a la lista local
                            is_logged_in = True  # Iniciar sesión después del registro



class Move():

    def __init__(self, url):
        # call the moves API endpoint
        req = requests.get(url)
        self.json = req.json()

        self.name = self.json['name']
        self.power = self.json['power']
        self.type = self.json['type']['name']


class Pokemon(pygame.sprite.Sprite):

    def __init__(self, name, level, x, y):

        pygame.sprite.Sprite.__init__(self)

        # call the pokemon API endpoint
        self.hp_x = None
        req = requests.get(f'{base_url}/pokemon/{name.lower()}')
        self.json = req.json()

        # set the pokemon's name and level
        self.name = name
        self.level = level

        # set the sprite position on the screen
        self.x = x
        self.y = y

        # number of potions left
        self.num_potions = 3

        # get the pokemon's stats from the API
        stats = self.json['stats']
        for stat in stats:
            if stat['stat']['name'] == 'hp':
                self.current_hp = stat['base_stat'] + self.level
                self.max_hp = stat['base_stat'] + self.level
            elif stat['stat']['name'] == 'attack':
                self.attack = stat['base_stat']
            elif stat['stat']['name'] == 'defense':
                self.defense = stat['base_stat']
            elif stat['stat']['name'] == 'speed':
                self.speed = stat['base_stat']

        # set the pokemon's types
        self.types = []
        for i in range(len(self.json['types'])):
            type = self.json['types'][i]
            self.types.append(type['type']['name'])

        # set the sprite's width
        self.size = 150

        # set the sprite to the front facing sprite
        self.set_sprite('front_default')

    def perform_attack(self, other, move):

        display_message(f'{self.name} used {move.name}')

        # pause for 2 seconds
        time.sleep(2)

        # calculate the damage
        damage = (2 * self.level + 10) / 250 * self.attack / other.defense * move.power

        # same type attack bonus (STAB)
        if move.type in self.types:
            damage *= 1.5

        # critical hit (6.25% chance)
        random_num = random.randint(1, 10000)
        if random_num <= 625:
            damage *= 1.5

        # round down the damage
        damage = math.floor(damage)

        other.take_damage(damage)

    def take_damage(self, damage):

        self.current_hp -= damage

        # hp should not go below 0
        if self.current_hp < 0:
            self.current_hp = 0

    def use_potion(self):

        # check if there are potions left
        if self.num_potions > 0:

            # add 30 hp (but don't go over the max hp)
            self.current_hp += 30
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp

            # decrease the number of potions left
            self.num_potions -= 1

    def set_sprite(self, side):

        # set the pokemon's sprite
        image = self.json['sprites'][side]
        image_stream = urlopen(image).read()
        image_file = io.BytesIO(image_stream)
        self.image = pygame.image.load(image_file).convert_alpha()

        # scale the image
        scale = self.size / self.image.get_width()
        new_width = self.image.get_width() * scale
        new_height = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def set_moves(self):

        self.moves = []

        # go through all moves from the api
        for i in range(len(self.json['moves'])):

            # get the move from different game versions
            versions = self.json['moves'][i]['version_group_details']
            for j in range(len(versions)):

                version = versions[j]

                # only get moves from red-blue version
                if version['version_group']['name'] != 'red-blue':
                    continue

                # only get moves that can be learned from leveling up (ie. exclude TM moves)
                learn_method = version['move_learn_method']['name']
                if learn_method != 'level-up':
                    continue

                # add move if pokemon level is high enough
                level_learned = version['level_learned_at']
                if self.level >= level_learned:
                    move = Move(self.json['moves'][i]['move']['url'])

                    # only include attack moves
                    if move.power is not None:
                        self.moves.append(move)

        # select up to 4 random moves
        if len(self.moves) > 4:
            self.moves = random.sample(self.moves, 4)

    def draw(self, alpha=255):

        sprite = self.image.copy()
        transparency = (255, 255, 255, alpha)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        game.blit(sprite, (self.x, self.y))

    def draw_hp(self):
        hp_background = pygame.image.load('barra2.png')  # Asegúrate de que esta ruta sea correcta
        hp_background = pygame.transform.scale(hp_background,
                                               (180, 60))  # Ajusta el tamaño de acuerdo a las barras de HP

        # Dibuja el fondo detrás de la barra de HP
        game.blit(hp_background, (self.hp_x - 10, self.hp_y - 10))  # Ajusta la posición según necesites

        # display the health bar
        bar_scale = 200 // self.max_hp
        for i in range(self.max_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(game, red, bar)

        for i in range(self.current_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(game, green, bar)

        # display "HP" text
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'HP: {self.current_hp} / {self.max_hp}', True, black)
        text_rect = text.get_rect()
        text_rect.x = self.hp_x
        text_rect.y = self.hp_y + 30
        game.blit(text, text_rect)

    def get_rect(self):

        return Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


def display_message(message):
    # draw a white box with black border
    pygame.draw.rect(game, white, (10, 350, 480, 140))
    pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

    # display the message
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(message, True, black)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410
    game.blit(text, text_rect)

    pygame.display.update()


def create_button(width, height, left, top, text_cx, text_cy, label):
    # position of the mouse cursor
    mouse_cursor = pygame.mouse.get_pos()

    button = Rect(left, top, width, height)

    # highlight the button if mouse is pointing to it
    if button.collidepoint(mouse_cursor):
        pygame.draw.rect(game, gold, button)
    else:
        pygame.draw.rect(game, white, button)

    # add the label to the button
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'{label}', True, black)
    text_rect = text.get_rect(center=(text_cx, text_cy))
    game.blit(text, text_rect)

    return button

button_width, button_height = 100, 50
yes_button_rect = pygame.Rect((100, 400), (button_width, button_height))  # Posición y tamaño del botón "Yes"
no_button_rect = pygame.Rect((300, 400), (button_width, button_height))   # Posición y tamaño del botón "No"


def draw_buttons():
    pygame.draw.rect(game, (0, 255, 0), yes_button_rect)  # Botón "Yes" en verde
    pygame.draw.rect(game, (255, 0, 0), no_button_rect)  # Botón "No" en rojo

    # Agregar texto a los botones
    font = pygame.font.Font(None, 36)
    yes_text = font.render("Yes", True, (255, 255, 255))
    no_text = font.render("No", True, (255, 255, 255))

    game.blit(yes_text, (yes_button_rect.x + 25, yes_button_rect.y + 10))
    game.blit(no_text, (no_button_rect.x + 25, no_button_rect.y + 10))

def draw_message():
    font = pygame.font.Font(None, 48)  # Fuente para el texto
    message = font.render("¿Quieres volver a jugar?", True, (255, 255, 255))  # Texto en blanco
    game.blit(message, (game_width//2 - message.get_width()//2, 300))  # Posiciona el texto en el centro horizontal

login_screen()
pygame.time.delay(6)
# create the starter pokemons
level = 30
bulbasaur = Pokemon('Bulbasaur', level, 25, 150)
charmander = Pokemon('Charmander', level, 175, 150)
squirtle = Pokemon('Squirtle', level, 325, 150)
pikachu = Pokemon('Pikachu', level, 25, 300)
jigglypuff = Pokemon('Jigglypuff', level, 175, 300)
rattata  = Pokemon('Rattata', level, 325, 300)
eevee = Pokemon('Eevee', level, 25, 450)
oddish = Pokemon('Oddish', level, 175, 450)
pidgey = Pokemon('Pidgey', level, 325, 450)
pokemons = [bulbasaur, charmander, squirtle, pikachu, jigglypuff, rattata, eevee, oddish, pidgey]

# the player's and rival's selected pokemon
player_pokemon = None
rival_pokemon = None

# game loop
game_status = 'select pokemon'



while game_status != 'quit':

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            game_status = 'quit'

        # detect keypress
        if event.type == KEYDOWN:

            # play again
            if event.key == K_y:
                # reset the pokemons
                bulbasaur = Pokemon('Bulbasaur', level, 25, 150)
                charmander = Pokemon('Charmander', level, 175, 150)
                squirtle = Pokemon('Squirtle', level, 325, 150)
                pikachu = Pokemon('Pikachu', level, 25, 300)
                jigglypuff = Pokemon('Jigglypuff', level, 175, 300)
                rattata = Pokemon('Rattata', level, 325, 300)
                eevee = Pokemon('Eevee', level, 25, 450)
                oddish = Pokemon('Oddish', level, 175, 450)
                pidgey = Pokemon('Pidgey', level, 325, 450)
                pokemons = [bulbasaur, charmander, squirtle, pikachu, jigglypuff, rattata, eevee, oddish, pidgey]
                game_status = 'select pokemon'

            # quit
            elif event.key == K_n:
                game_status = 'quit'

        # detect mouse click
        if event.type == MOUSEBUTTONDOWN:

            # coordinates of the mouse click
            mouse_click = event.pos
            with open('posiciones_clics.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([mouse_click[0], mouse_click[1]])  # Escribir las coordenadas X e Y
            # for selecting a pokemon
            if game_status == 'select pokemon':

                # check which pokemon was clicked on
                for i in range(len(pokemons)):

                    if pokemons[i].get_rect().collidepoint(mouse_click):
                        # assign the player's and rival's pokemon
                        player_pokemon = pokemons[i]
                        rival_pokemon = pokemons[(i + 1) % len(pokemons)]

                        # lower the rival pokemon's level to make the battle easier
                        rival_pokemon.level = int(rival_pokemon.level * .75)

                        # set the coordinates of the hp bars
                        player_pokemon.hp_x = 275
                        player_pokemon.hp_y = 250
                        rival_pokemon.hp_x = 50
                        rival_pokemon.hp_y = 50

                        game_status = 'prebattle'

            # for selecting fight or use potion
            elif game_status == 'player turn':

                # check if fight button was clicked
                if fight_button.collidepoint(mouse_click):
                    game_status = 'player move'

                # check if potion button was clicked
                if potion_button.collidepoint(mouse_click):

                    # force to attack if there are no more potions
                    if player_pokemon.num_potions == 0:
                        display_message('No more potions left')
                        time.sleep(4)
                        game_status = 'player move'
                    else:
                        player_pokemon.use_potion()
                        display_message(f'{player_pokemon.name} used potion')
                        time.sleep(4)
                        game_status = 'rival turn'

            # for selecting a move
            elif game_status == 'player move':

                # check which move button was clicked
                for i in range(len(move_buttons)):
                    button = move_buttons[i]

                    if button.collidepoint(mouse_click):
                        move = player_pokemon.moves[i]
                        player_pokemon.perform_attack(rival_pokemon, move)

                        # check if the rival's pokemon fainted
                        if rival_pokemon.current_hp == 0:
                            game_status = 'fainted'
                        else:
                            game_status = 'rival turn'

    # pokemon select screen
    if game_status == 'select pokemon':

        game.fill(white)
        # Dibuja los Pokémon en una cuadrícula (3 filas, 3 columnas)
        rows = 3
        cols = 3
        padding = 50
        pokemon_size = 100

        for index, pokemon in enumerate(pokemons):
            x = (index % cols) * (pokemon_size + padding)+20
            y = (index // cols) * (pokemon_size + padding)+15
            pokemon.x = x  # Actualiza la posición x del Pokémon
            pokemon.y = y  # Actualiza la posición y del Pokémon
            pokemon.size = pokemon_size  # Ajusta el tamaño del Pokémon
            pokemon.draw()

        # draw box around pokemon the mouse is pointing to
            mouse_cursor = pygame.mouse.get_pos()
            if pokemon.get_rect().collidepoint(mouse_cursor):
                pygame.draw.rect(game, black, pokemon.get_rect(), 2)

        pygame.display.update()

    # get moves from the API and reposition the pokemons
    if game_status == 'prebattle':
        # draw the selected pokemon
        game.fill(white)
        player_pokemon.draw()
        pygame.display.update()

        player_pokemon.set_moves()
        rival_pokemon.set_moves()

        # reposition the pokemons
        player_pokemon.x = -50
        player_pokemon.y = 100
        rival_pokemon.x = 250
        rival_pokemon.y = -50

        # resize the sprites
        player_pokemon.size = 300
        rival_pokemon.size = 300
        player_pokemon.set_sprite('back_default')
        rival_pokemon.set_sprite('front_default')

        game_status = 'start battle'

    # start battle animation
    if game_status == 'start battle':

        # rival sends out their pokemon
        alpha = 0
        while alpha < 255:
            game.blit(background, (0, 0))  # fondo
            rival_pokemon.draw(alpha)
            display_message(f'Rival sent out {rival_pokemon.name}!')
            alpha += .4

            pygame.display.update()

        # pause for 1 second
        time.sleep(2)

        # player sends out their pokemon
        alpha = 0
        while alpha < 255:
            game.blit(background, (0, 0))
            rival_pokemon.draw()
            player_pokemon.draw(alpha)
            display_message(f'Go {player_pokemon.name}!')
            alpha += .4

            pygame.display.update()

        # draw the hp bars
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

        # determine who goes first
        if rival_pokemon.speed > player_pokemon.speed:
            game_status = 'rival turn'
        else:
            game_status = 'player turn'

        pygame.display.update()

        # pause for 1 second
        time.sleep(1)

    # display the fight and use potion buttons
    if game_status == 'player turn':
        game.blit(background, (0, 0))
        player_pokemon.draw()
        rival_pokemon.draw()
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

        # create the fight and use potion buttons
        fight_button = create_button(240, 140, 10, 350, 130, 412, 'Fight')
        potion_button = create_button(240, 140, 250, 350, 370, 412, f'Use Potion ({player_pokemon.num_potions})')

        # draw the black border
        pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

        pygame.display.update()

    # display the move buttons
    if game_status == 'player move':

        game.blit(background, (0, 0))
        player_pokemon.draw()
        rival_pokemon.draw()
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

        # create a button for each move
        move_buttons = []
        for i in range(len(player_pokemon.moves)):
            move = player_pokemon.moves[i]
            button_width = 240
            button_height = 70
            left = 10 + i % 2 * button_width
            top = 350 + i // 2 * button_height
            text_center_x = left + 120
            text_center_y = top + 35
            button = create_button(button_width, button_height, left, top, text_center_x, text_center_y,
                                   move.name.capitalize())
            move_buttons.append(button)

        # draw the black border
        pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

        pygame.display.update()

    # rival selects a random move to attack with
    if game_status == 'rival turn':

        game.blit(background, (0, 0))
        player_pokemon.draw()
        rival_pokemon.draw()
        player_pokemon.draw_hp()
        rival_pokemon.draw_hp()

        # empty the display box and pause for 2 seconds before attacking
        display_message('')
        time.sleep(2)

        # select a random move
        move = random.choice(rival_pokemon.moves)
        rival_pokemon.perform_attack(player_pokemon, move)

        # check if the player's pokemon fainted
        if player_pokemon.current_hp == 0:

            game_status = 'fainted'
        else:
            
            game_status = 'player turn'

        pygame.display.update()

    # one of the pokemons fainted
    if game_status == 'fainted':
        alpha = 255
        while alpha > 0:
            # Limpiar la pantalla
            game.blit(background, (0, 0))
            player_pokemon.draw_hp()
            rival_pokemon.draw_hp()
            # Determinar qué Pokémon se desmayó
            if rival_pokemon.current_hp == 0:
                player_pokemon.draw()
                rival_pokemon.draw(alpha)
                display_message(f'{rival_pokemon.name} fainted!')
            else:
                player_pokemon.draw(alpha)
                rival_pokemon.draw()
                display_message(f'{player_pokemon.name} fainted!')
            alpha -= .4
            pygame.display.update()
            pygame.time.delay(10)  # Controlar la velocidad de la animación

        game_status = 'gameover'

        # Pantalla de gameover
    if game_status == 'gameover':
        game.fill((0, 0, 0))  # Fondo negro
        draw_buttons()
        draw_message()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Detectar clics de mouse
            elif event.type == MOUSEBUTTONDOWN:
                if yes_button_rect.collidepoint(event.pos):
                    # Reiniciar Pokémon
                    bulbasaur = Pokemon('Bulbasaur', level, 25, 150)
                    charmander = Pokemon('Charmander', level, 175, 150)
                    squirtle = Pokemon('Squirtle', level, 325, 150)
                    pikachu = Pokemon('Pikachu', level, 25, 300)
                    jigglypuff = Pokemon('Jigglypuff', level, 175, 300)
                    rattata = Pokemon('Rattata', level, 325, 300)
                    eevee = Pokemon('Eevee', level, 25, 450)
                    oddish = Pokemon('Oddish', level, 175, 450)
                    pidgey = Pokemon('Pidgey', level, 325, 450)

                    # Actualizar la lista de Pokémon
                    pokemons = [bulbasaur, charmander, squirtle, pikachu, jigglypuff, rattata, eevee, oddish, pidgey]
                    game_status = 'select pokemon'

                elif no_button_rect.collidepoint(event.pos):
                    # Si el botón "No" es clicado, salir del juego
                    game_status = 'quit'
                    running = False

        # Actualizar la pantalla al final del bucle
        pygame.display.flip()

pygame.quit()

