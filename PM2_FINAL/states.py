import pygame
from player_car import PlayerCar
from background import Background
from enemy_manager import EnemyManager
from assets.audio_manager import AudioManager

class State:
    def __init__(self, game):
        self.game = game

    def handle(self): pass
    def update(self): pass
    def render(self): pass


class MenuState(State):
    def __init__(self, game):
        super().__init__(game)
        self.game.audio.play_lobby()

    def handle(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.game.running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.game.change_state("PLAY")

    def render(self):
        self.game.screen.fill((0, 0, 0))

        # Multi-line centered text
        lines = [
            "CAR RACING DODGE GAME",
            "PRESS SPACE TO START"
        ]

        y = self.game.HEIGHT // 2 - len(lines) * 20

        for line in lines:
            txt = self.game.font.render(line, True, (255, 255, 255))
            x = (self.game.WIDTH - txt.get_width()) // 2
            self.game.screen.blit(txt, (x, y))
            y += 60


class PlayState(State):
    def __init__(self, game):
        super().__init__(game)
        self.score, self.highscores = 0, self.load_scores()
        self.player = PlayerCar(game.assets.player, game.left, game.right)
        self.bg = Background(game.assets.bg, game.WIDTH)
        self.enemies = EnemyManager(game.assets.enemy_cars, game.left, game.right, max_enemies=8, spawn_delay=1500)

    def load_scores(self):
        try:
            with open("scores.txt", "r") as f:
                return sorted([int(x.strip()) for x in f.readlines()], reverse=True)[:5]
        except:
            return [0, 0, 0, 0, 0]

    def save_scores(self):
        self.highscores.append(self.score)
        with open("scores.txt", "w") as f:
            for s in sorted(self.highscores, reverse=True)[:5]:
                f.write(str(s) + "\n")

    def handle(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.game.running = False

    def update(self):
        self.player.update(self.score)
        self.bg.update(self.game.HEIGHT)
        self.enemies.update(self.game.HEIGHT)
        self.score += 1

        # Arcade-style scaling
        bg_speed = 6 + (self.score ** 0.5) * 0.08
        enemy_speed = 5 + (self.score ** 0.5) * 0.08

        self.bg.speed = min(15, bg_speed)

        for e in self.enemies.enemies:
            e.speed = min(14, enemy_speed)

        if self.enemies.check_collision(self.player):
            self.game.audio.play_crash()
            self.save_scores()
            self.game.change_state("GAMEOVER")

    def render(self):
        self.bg.draw(self.game.screen, self.game.left, self.game.right, self.game.HEIGHT)
        self.enemies.draw(self.game.screen)
        self.player.draw(self.game.screen)

        score_text = self.game.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.game.screen.blit(score_text, (120, 10))


class GameOverState(State):
    def handle(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.game.running = False
            if e.type == pygame.KEYDOWN:
                self.game.change_state("MENU")

    def render(self):
        self.game.screen.fill((0, 0, 0))

        crashed_txt = self.game.font.render("CRASHED!", True, (255, 0, 0))
        x, y = (self.game.WIDTH - crashed_txt.get_width()) // 2, 150
        self.game.screen.blit(crashed_txt, (x, y))

        header_txt = self.game.font.render("HIGH SCORES", True, (255, 255, 0))
        x_header = (self.game.WIDTH - header_txt.get_width()) // 2
        self.game.screen.blit(header_txt, (x_header, y + 80))

        for i, s in enumerate(self.game.states["PLAY"].highscores):
            score_txt = self.game.font.render(f"{i + 1}. {s}", True, (255, 255, 255))
            x_score = (self.game.WIDTH - score_txt.get_width()) // 2
            self.game.screen.blit(score_txt, (x_score, y + 140 + i * 50))

        last_score_y = y + 140 + (len(self.game.states["PLAY"].highscores) - 1) * 50

        instruction = self.game.font.render("PRESS ANY KEY TO RETURN TO MENU", True, (255, 255, 255))
        x_inst = (self.game.WIDTH - instruction.get_width()) // 2
        self.game.screen.blit(instruction, (x_inst, last_score_y + 80))
