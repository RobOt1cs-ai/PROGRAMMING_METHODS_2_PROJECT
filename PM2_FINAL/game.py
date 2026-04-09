import pygame
from assets.asset_manager import AssetManager
from assets.audio_manager import AudioManager
from player_car import PlayerCar
from background import Background
from enemy_manager import EnemyManager
from states import MenuState, PlayState, GameOverState

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.WIDTH, self.HEIGHT = 1200, 800
        self.left, self.right = 360, 850
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Racing Simulator")

        self.clock, self.font = pygame.time.Clock(), pygame.font.SysFont("comicsansms", 40)
        self.assets, self.audio = AssetManager(), AudioManager()

        pygame.display.set_icon(self.assets.icon)
        self.running, self.states = True, {"MENU": MenuState(self), "PLAY": PlayState(self), "GAMEOVER": GameOverState(self)}
        self.state = self.states["MENU"]

    def change_state(self, name):
        self.state = self.states[name]
        if name == "PLAY": self.states["PLAY"] = PlayState(self)

    def run(self):
        while self.running:
            self.state.handle()
            self.state.update()
            self.state.render()
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()