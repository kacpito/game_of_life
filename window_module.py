import pygame
import button_module

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)


class MainWindow:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = None

        self.n_cells_x, self.n_cells_y = 40, 30
        self.cell_width = self.width // self.n_cells_x
        self.cell_height = self.height // self.n_cells_y

        self.button_Factory = None

    def Init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.button_Factory = button_module.ButtonFactory(self.screen)

    def DrawCells(self, game_state):
        for y in range(self.n_cells_y):
            for x in range(self.n_cells_x):
                cell = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                if game_state[x, y] == 1:
                    pygame.draw.rect(self.screen, black, cell)

    def DrawGrid(self):
        for y in range(0, self.width, self.cell_height):
            for x in range(0, self.width, self.cell_width):
                cell = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, gray, cell, 1)

    def DrawButtons(self):
        self.button_Factory.CreatePlayButton()
        self.button_Factory.CreatePauseButton()
        self.button_Factory.CreateSaveButton()
        self.button_Factory.CreateLoadButton()

    def Draw(self, game_state):
        self.screen.fill(white)
        self.DrawGrid()
        self.DrawCells(game_state)
        self.DrawButtons()

        pygame.display.flip()


