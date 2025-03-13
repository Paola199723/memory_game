import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.options = ["Jugar", "Instrucciones", "Ajustes", "Salir"]
        self.selected_option = 0
        self.running = True

    def draw(self):
        self.screen.fill((50, 50, 50))  # Fondo oscuro
        font = pygame.font.Font(None, 50)
        
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (180, 180, 180)
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(300, 200 + i * 60))
            self.screen.blit(text, text_rect)
        
        pygame.display.flip()

    def run(self):
        while self.running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        return self.options[self.selected_option]
        return "Salir"