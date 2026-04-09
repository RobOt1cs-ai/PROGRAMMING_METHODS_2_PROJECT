import pygame
from pathlib import Path

class AudioManager:
    def __init__(self):
        path = Path(__file__).parent / "audio"
        self.lobby = path / "Car Racing Sounds-Lobby.mp3"
        self.crash = pygame.mixer.Sound(path / "Car Crash Sound Effect.mp3")

    def play_lobby(self):
        pygame.mixer.music.load(self.lobby)
        pygame.mixer.music.play(-1)

    def play_crash(self):
        self.crash.play()