import pygame
import random

class EnemyCar:
    def __init__(self, images, lanes):
        self.image = pygame.transform.scale(random.choice(images), (60, 120))
        self.mask = pygame.mask.from_surface(self.image)
        self.lanes, self.speed, self.switch_speed = lanes, random.randint(5, 9), 5
        self.x, self.y = random.choice(self.lanes), -random.randint(100, 600)
        self.current_lane, self.target_lane = self.x, self.x

    def update(self):
        self.y += self.speed

        # Randomly decide to switch lanes
        if random.random() < 0.01:
            self.target_lane = random.choice(self.lanes)

        # Smooth movement toward target lane
        if self.x < self.target_lane:
            self.x += self.switch_speed
            if self.x > self.target_lane:
                self.x = self.target_lane
        elif self.x > self.target_lane:
            self.x -= self.switch_speed
            if self.x < self.target_lane:
                self.x = self.target_lane

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collide(self, player):
        return player.mask.overlap(self.mask, (int(self.x - player.x), int(self.y - player.y))) is not None
