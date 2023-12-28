import pygame
import time
from important_variables import *

window = pygame.display.set_mode([screen_length, screen_height])
pygame.display.set_caption(title)


def call_every_cycle(function):
    """Calls the given function every cycle of the game loop"""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        function()


def draw_circle(left_edge, top_edge, length, height, color, outline_height):
    """Draws a circle on the screen"""

    pygame.draw.ellipse(window, color, [left_edge, top_edge, length, height], outline_height)


def draw_line(start_x_coordinate, end_x_coordinate, start_y_coordinate, end_y_coordinate, color, line_height):
    """Draws a line on the screen"""

    pygame.draw.line(window, color, [int(start_x_coordinate), int(start_y_coordinate - line_height)],
                     [int(end_x_coordinate), int(end_y_coordinate - line_height)], line_height)


def get_mouse_position():
    """
        Returns: 
            list[float]: [x, y] coordinates of the mouse
    """
    return pygame.mouse.get_pos()


def mouse_was_pressed():
    """
        Returns:
            bool: whether the mouse was pressed
    """

    return pygame.mouse.get_pressed()[0]


def update_display():
    """Updates the display, so the game is rerendered"""

    pygame.display.update()


def clear_screen():
    """Removes everything from the screen"""

    window.fill(background_color)


def pause_game(time_needed):
    """Pauses the game for the given amount of time"""

    time.sleep(time_needed)
