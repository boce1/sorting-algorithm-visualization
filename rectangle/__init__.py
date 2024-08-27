import pygame

class Rectangle:
    def __init__(self, val, arr_possition, rect_width, unit, window_height, color):
        self.val = val
        self.x = arr_possition * rect_width
        self.y = window_height - val * unit
        self.rect_width = rect_width
        self.unit = unit
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x + 1, self.y + 1, self.rect_width - 1, self.val * self.unit - 1))

    def update_cords(self, arr_possition, window_height):
        self.x = arr_possition * self.rect_width
        self.y = window_height - self.val * self.unit