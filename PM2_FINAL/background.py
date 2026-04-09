class Background:
    def __init__(self, image, width):
        self.image = image
        self.x = (width / 10) - 25
        self.y1 = 0
        self.y2 = -self.image.get_height()
        self.speed = 6

    def update(self, height):
        self.y1 += self.speed
        self.y2 += self.speed
        if self.y1 >= height: self.y1 = self.y2 - self.image.get_height()
        if self.y2 >= height: self.y2 = self.y1 - self.image.get_height()

    def draw(self, screen, left, right, height):
        screen.blit(self.image, (self.x, self.y1))
        screen.blit(self.image, (self.x, self.y2))