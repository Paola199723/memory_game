import pygame

class Card:
    def __init__(self, image, image_name, row, col):
        self.image = pygame.transform.scale(image, (100, 100))
        self.image_name = image_name  # 🔥 Guardamos el nombre del archivo
        self.rect = pygame.Rect(col * 150 + 25, row * 150 + 25, 100, 100)
        self.hidden = True  # Si es True, la carta está boca abajo
        self.matched = False  # Si es True, la carta desaparecerá

    def draw(self, screen, back_image):
        if not self.matched:  # 🔥 Solo dibuja si no está emparejada
            if self.hidden:
                screen.blit(back_image, self.rect)  # Muestra el reverso
            else:
                screen.blit(self.image, self.rect)  # Muestra la imagen real
