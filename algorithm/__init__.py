import pygame

def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def buble_sort(arr, draw_scene, window, check_color, replace_color, regular_color):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            arr[j].color = check_color
            arr[j + 1].color = replace_color
            draw_scene(window)
            pygame.time.delay(10)
            if arr[j].val > arr[j + 1].val:
                swap_elements(arr, j, j + 1)
            arr[j].color = regular_color
            arr[j + 1].color = regular_color
            draw_scene(window)
            pygame.time.delay(10)
            yield
    
    for rect in arr:
        rect.color = regular_color

def insertion_sort(arr, draw_scene, window, check_color, replace_color, regular_color):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j].val < arr[j - 1].val and j > 0:
            arr[j].color = check_color
            arr[j - 1].color = replace_color
            draw_scene(window)
            pygame.time.delay(10) 

            arr[j].color = regular_color
            arr[j - 1].color = regular_color

            swap_elements(arr, j, j - 1)
            j -= 1
            yield
            

