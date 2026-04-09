import pygame
from pathlib import Path

class AssetManager:
    def __init__(self):
        self.path = Path(__file__).parent
        self.load()

    def load(self):
        img = self.path / "img"
        self.player = pygame.image.load(img / "PLAYER_CAR19.png")
        self.bg = pygame.image.load(img / "CAR_RACING_TRACK.png")
        self.icon = pygame.image.load(img / "icon.png")
        self.enemy_cars = [pygame.transform.flip(pygame.image.load(img / f"CARE{i}.png"), False, True) for i in range(1, 20)]