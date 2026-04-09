import random,pygame
from enemy_car import EnemyCar

class EnemyManager:
    def __init__(self, enemy_images, left, right, max_enemies=8, spawn_delay=100):
        lane_width = (right - left) // 3
        self.lanes = [left + lane_width // 2, left + lane_width + lane_width // 2, left + lane_width * 2 + lane_width // 2]
        self.enemy_images, self.max_enemies, self.spawn_delay = enemy_images, max_enemies, spawn_delay
        self.enemies, self.last_spawn_time = [], pygame.time.get_ticks()

    def spawn_enemy(self):
        enemy = EnemyCar(self.enemy_images, self.lanes)
        enemy.x = random.choice(self.lanes)
        self.enemies.append(enemy)

    def update(self, height):
        if len(self.enemies) < self.max_enemies and pygame.time.get_ticks() - self.last_spawn_time > self.spawn_delay:
            self.spawn_enemy()
            self.last_spawn_time = pygame.time.get_ticks()

        for enemy in self.enemies[:]:
            enemy.update()
            if enemy.y > height: self.enemies.remove(enemy)

    def draw(self, screen):
        for enemy in self.enemies: enemy.draw(screen)

    def check_collision(self, player):
        return any(enemy.collide(player) for enemy in self.enemies)