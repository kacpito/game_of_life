import window_module as wm
import simulation_module as sm
import game_state_module as game

if __name__ == '__main__':
    main_window = wm.MainWindow()
    main_window.Init()

    game_of_life = game.GameState()

    simulation = sm.Simulation(sm.Play())
    simulation.RunSimulation(main_window, game_of_life)
