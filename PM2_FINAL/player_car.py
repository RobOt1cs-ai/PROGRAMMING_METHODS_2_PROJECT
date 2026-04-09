import pygame

class PlayerCar:
    def __init__(self, image, left, right):
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.left, self.right = left, right
        self.x, self.y = 555, 480
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.base_speed, self.speed = 6, 6
        self.min_speed, self.max_speed = 2, 15

    def update(self, score):
        # Scale max speed with score (balanced)
        self.max_speed = 15 + (score ** 0.5) * 0.06

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed += 0.1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.speed -= 0.1

        self.speed = max(self.min_speed, min(self.speed, self.max_speed))

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > self.left:
            self.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x + self.width < self.right:
            self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))