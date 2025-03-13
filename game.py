import pygame
from board import Board
import config  # Importar la configuración global
import time  # Para el temporizador

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # 🔥 Inicializar el módulo de sonido

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Juego de Memoria")
        self.board = Board()
        self.selected = []
        self.running = True
        self.matched_pairs = 0
        self.start_time = time.time()
        self.last_selection_time = 0
        self.time_limit = config.TIME_LIMIT  # Usar el tiempo límite de settings.py

        # 🔥 Definir sonidos correctamente
        self.flip_sound = pygame.mixer.Sound("assets/flip.mp3")
        self.match_sound = pygame.mixer.Sound("assets/match.mp3")
        self.win_sound = pygame.mixer.Sound("assets/win.mp3")

        # 🔥 Fuente para el temporizador
        self.font = pygame.font.Font(None, 36)

    def get_card(self, pos):
        x, y = pos
        col = x // 150
        row = y // 150
        if row < 4 and col < 4:
            return self.board.grid[row][col]
        return None

    def draw_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(self.time_limit - elapsed_time, 0)  # 🔥 Evita números negativos
        timer_text = self.font.render(f"Tiempo: {remaining_time}s", True, (255, 0, 0))
        self.screen.blit(timer_text, (10, 10))

        if remaining_time == 0:
            self.running = False  # 🔥 Terminar el juego cuando el tiempo se acabe

    def run(self):
        while self.running:
            self.screen.fill((255, 255, 255))
            self.board.draw(self.screen)
            self.draw_timer()  # 🔥 Mostrar temporizador siempre

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    card = self.get_card(pygame.mouse.get_pos())

                    if card and card.hidden and not card.matched and len(self.selected) < 2:
                        card.hidden = False
                        self.selected.append(card)
                        self.flip_sound.play()  # 🔥 Sonido al voltear carta
                        self.last_selection_time = time.time()

            # 🔥 Comprobar emparejamiento después de 1 segundo
            if len(self.selected) == 2 and time.time() - self.last_selection_time > 1:
                if self.selected[0].image_name == self.selected[1].image_name:
                    print("✅ ¡Pareja encontrada!")
                    self.selected[0].matched = True
                    self.selected[1].matched = True
                    self.matched_pairs += 1
                    self.match_sound.play()  # 🔥 Sonido al encontrar un par
                else:
                    print("❌ No coinciden, ocultando cartas")
                    self.selected[0].hidden = True
                    self.selected[1].hidden = True

                self.selected = []  # Reiniciar selección

            # 🔥 Verificar si el jugador ha ganado
            if self.matched_pairs == 8:
                self.show_game_over()

            pygame.display.flip()

        pygame.quit()

    def show_game_over(self):
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)
        print(f"🎉 ¡Juego completado en {total_time} segundos!")
        self.win_sound.play()  # 🔥 Sonido de victoria 🎵

        font = pygame.font.Font(None, 50)
        text = font.render(f"¡Ganaste en {total_time} segundos!", True, (0, 255, 0))
        self.screen.fill((0, 0, 0))
        self.screen.blit(text, (50, 250))
        pygame.display.flip()

        pygame.time.delay(3000)
        self.running = False
