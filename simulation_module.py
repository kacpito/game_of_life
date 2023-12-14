from abc import ABC, abstractmethod
from tkinter import filedialog

import tkinter as tk
import numpy as np
import pygame
import time

import game_state_module as gm


class ExecuteMethod(ABC):
    @abstractmethod
    def Execute(self):
        pass

class Play(ExecuteMethod):
    def Execute(self):
        return True

class Pause(ExecuteMethod):
    def Execute(self):
        return False

class Save(ExecuteMethod):
    def Execute(self):
        game_state = gm.GameState().game_state
        np.savetxt(open_file_dialog("Save"), game_state, fmt='%d', delimiter=',')

class Load(ExecuteMethod):
    def Execute(self):
         return np.loadtxt(open_file_dialog("Load"), delimiter=',')

class Simulation:
    def __init__(self, execute_method):
        self.execute_method = Play()
        self.running = self.execute_method.Execute()

    def RunSimulation(self, window, game_state):
        simulation_loop = True

        while simulation_loop:
            window.Draw(game_state.game_state)
            simulation_loop = self.CheckEvents(game_state, simulation_loop)

            if self.running:
                game_state.UpdateGameState()
                time.sleep(0.1)

        pygame.quit()

    def CheckEvents(self, game_state, simulation_loop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulation_loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 25 <= mouse_x <= 125 and 50 <= mouse_y <= 80:
                    self.execute_method = Play()
                    self.running = self.execute_method.Execute()
                elif 25 <= mouse_x <= 125 and 90 <= mouse_y <= 120:
                    self.execute_method = Pause()
                    self.running = self.execute_method.Execute()
                elif 675 <= mouse_x <= 775 and 50 <= mouse_y <= 80:
                    self.execute_method = Pause()
                    self.running = self.execute_method.Execute()
                    self.execute_method = Save()
                    self.execute_method.Execute()
                elif 675 <= mouse_x <= 775 and 90 <= mouse_y <= 120:
                    self.execute_method = Pause()
                    self.running = self.execute_method.Execute()
                    self.execute_method = Load()
                    game_state.LoadGameState(self.execute_method.Execute())


        return simulation_loop


def open_file_dialog(flag):
    root = tk.Tk()
    root.withdraw()

    if flag == "Load":
        file_path = filedialog.askopenfilename()
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    root.destroy()

    return file_path