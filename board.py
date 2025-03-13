import pygame
import random
import os
from card import Card

# Configuración de pantalla
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4

class Board:
    def __init__(self):
        # Cargar imágenes
        image_paths = ["img1.png", "img2.png", "img3.png", "img4.png","img5.png", "img6.png", "img7.png", "img8.png"]
        images = [(pygame.image.load(os.path.join("assets", img)), img) for img in image_paths]

        if len(images) != 8:
            raise ValueError(f"Se esperaban 8 imágenes únicas, pero hay {len(images)}. Verifica tu carpeta 'assets/'")

        images *= 2  # Duplicar para hacer pares
        print("Total de cartas después de duplicar:", len(images))  # 🔥 Debe ser 16

        random.shuffle(images)  # Mezclar cartas
        
        # Cargar imagen trasera de las cartas
        self.back_image = pygame.image.load("assets/back.png")
        self.back_image = pygame.transform.scale(self.back_image, (100, 100))

        # Crear la grilla de cartas
        self.grid = []
        idx = 0
        for row in range(ROWS):
            row_cards = []
            for col in range(COLS):
                image, name = images[idx]  # 🔥 Obtener imagen y nombre
                row_cards.append(Card(image, name, row, col))
                idx += 1
            self.grid.append(row_cards)

    def draw(self, screen):
        screen.fill((255, 255, 255))  # Fondo blanco
        for row in self.grid:
            for card in row:
                if not card.matched:  # 🔥 Solo dibuja cartas NO emparejadas
                    card.draw(screen, self.back_image)
        pygame.display.flip()

    def shuffle_cards(self):
        print("🔀 Mezclando las cartas...")
        random.shuffle(self.grid)

