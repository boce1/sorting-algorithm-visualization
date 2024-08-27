import pygame
from random import randint, shuffle
from rectangle import Rectangle
from algorithm import buble_sort, insertion_sort

pygame.init()

WIDTH = 600
HEIGHT = WIDTH
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
RECT_NUM = 20
RECT_UNIT = HEIGHT // RECT_NUM

rectangles = [Rectangle(i + 1, i, WIDTH // RECT_NUM, RECT_UNIT, HEIGHT, WHITE) for i in range(RECT_NUM)]
shuffle(rectangles)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visuallization for sorting algorithms")

def draw_scene(win):
    win.fill(BLACK)
    draw_rectangles(win)
    pygame.display.update()

def draw_rectangles(win):
    for i in range(len(rectangles)):
        rectangles[i].update_cords(i, HEIGHT)
        rectangles[i].draw(win) 

def toggle_sorting(event):
    global sorting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            sorting = True
        elif event.key == pygame.K_ESCAPE:
            sorting = False
    
def change_algorithm(event):
    global sort_generator_index, sorting, rectangles, sort_generator
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and sort_generator_index > 1:
            sort_generator_index -= 1
            sorting = False
            shuffle(rectangles)
            choose_algorithm(sort_generator_index)
        elif event.key == pygame.K_RIGHT and sort_generator_index < 2:
            sort_generator_index += 1
            sorting = False
            shuffle(rectangles)
            choose_algorithm(sort_generator_index)
        print(sort_generator_index)

def choose_algorithm(sort_generator_index):
    global sort_generator
    if sort_generator_index == 1:
        sort_generator = buble_sort(rectangles, draw_scene, window, GREEN, RED, WHITE)
    elif sort_generator_index == 2:
        sort_generator = insertion_sort(rectangles, draw_scene, window, GREEN, RED, WHITE)

clock = pygame.time.Clock()
running = True
sorting = False
sort_generator = None
sort_generator_index = 1

sort_generator = buble_sort(rectangles, draw_scene, window, GREEN, RED, WHITE) # default sort generation when starting

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        toggle_sorting(event)
        change_algorithm(event)


    if sorting:
        try:
            next(sort_generator)
        except StopIteration:
            sorting = False

    draw_scene(window)

pygame.quit()
