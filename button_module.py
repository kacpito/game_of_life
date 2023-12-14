import pygame


class Button:
    def __init__(self, x, y, width, height, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label

    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 25)
        text = font.render(self.label, True, (0,0,0))
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text, text_rect)

class PlayButton(Button):
    def __init__(self):
        super().__init__(25, 50, 100, 30, "Play")

class PauseButton(Button):
    def __init__(self):
        super().__init__(25, 90, 100, 30, "Pause")

class SaveButton(Button):
    def __init__(self):
        super().__init__(675, 50, 100, 30, "Save")

class LoadButton(Button):
    def __init__(self):
        super().__init__(675, 90, 100, 30, "Load")

class ButtonFactory:
    def __init__(self, screen):
        self.screen = screen

    def CreatePlayButton(self):
        PlayButton().draw(self.screen)

    def CreatePauseButton(self):
        PauseButton().draw(self.screen)

    def CreateSaveButton(self):
        SaveButton().draw(self.screen)

    def CreateLoadButton(self):
        LoadButton().draw(self.screen)