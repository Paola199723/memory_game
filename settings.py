import pygame
import config

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 40)
        self.running = True
        self.options = [30, 60, 90]  # Opciones de tiempo
        self.selected_index = self.options.index(config.TIME_LIMIT)  # Índice actual

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 50))

            # Texto de ajustes
            title = self.font.render("Ajustes:", True, (255, 255, 255))
            time_text = self.font.render(f"Tiempo límite: {self.options[self.selected_index]}s", True, (255, 255, 255))
            instructions = self.font.render("⬆️⬇️ para cambiar, ESC para volver", True, (255, 255, 255))

            self.screen.blit(title, (50, 100))
            self.screen.blit(time_text, (50, 200))
            self.screen.blit(instructions, (50, 300))

            pygame.display.flip()

            # Capturar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Volver al menú
                        self.running = False
                    elif event.key == pygame.K_UP:  # Aumentar tiempo
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:  # Disminuir tiempo
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    
                    # Guardar el nuevo tiempo límite
                    config.TIME_LIMIT = self.options[self.selected_index]

