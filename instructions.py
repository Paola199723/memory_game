import pygame

class Instructions:
    def __init__(self, screen):
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.Font(None, 28)  # Usa una fuente predeterminada

        # Texto de instrucciones
        self.instructions = [
            "1) Selecciona en el menú principal",
            "la opción JUGAR para iniciar el juego.",
            "",
            "2) Selecciona las cartas con el mouse",
            " para encontrar las parejas.",
            "",
            "3) Tienes un tiempo límite por defecto",
            " de 60 segundos para encontrar todas las parejas.",
            "",
            "4) En el menú principal en la sección",
            " de ajustes puedes modificar el tiempo límite.",
            "",
            "Presiona ESC para volver al menú principal."
        ]

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Fondo negro

            y_offset = 80  # Posición inicial en Y
            for line in self.instructions:
                text_surface = self.font.render(line, True, (255, 255, 255))  # Texto blanco
                self.screen.blit(text_surface, (50, y_offset))  # Dibujar en la pantalla
                y_offset += 30  # Espaciado entre líneas

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
