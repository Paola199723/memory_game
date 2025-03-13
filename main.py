import pygame
from menu import Menu
from game import Game
from settings import Settings
from instructions import Instructions

pygame.init()
screen = pygame.display.set_mode((600, 600))

running = True
while running:
    menu = Menu(screen)
    option = menu.run()

    if option == "Jugar":
        game = Game()
        game.run()
    elif option == "Instrucciones":
        instructions = Instructions(screen)
        instructions.run()
    elif option == "Ajustes":
        settings = Settings(screen)
        settings.run()
    elif option == "Salir":
        running = False

pygame.quit()
