import pygame

def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def buble_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            arr[j].color = check_color
            arr[j + 1].color = replace_color
            draw_scene(window)
            pygame.time.delay(delay)
            if arr[j].val > arr[j + 1].val:
                swap_elements(arr, j, j + 1)
            arr[j].color = regular_color
            arr[j + 1].color = regular_color
            yield

def insertion_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j].val < arr[j - 1].val and j > 0:
            arr[j].color = check_color
            arr[j - 1].color = replace_color
            draw_scene(window)
            pygame.time.delay(delay) 

            arr[j].color = regular_color
            arr[j - 1].color = regular_color

            swap_elements(arr, j, j - 1)
            j -= 1
            yield

def selection_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        arr[i].color = check_color
        for j in range(i + 1, n):
            arr[j].color = replace_color
            draw_scene(window)
            pygame.time.delay(delay)
            if arr[j].val < arr[min_index].val:
                min_index = j

            arr[j].color = regular_color
            yield
            
        arr[i].color = regular_color
        
        swap_elements(arr, min_index, i)     

def shell_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j].val < arr[j - gap].val:
                arr[j].color = check_color
                arr[j - gap].color = replace_color
                draw_scene(window)
                pygame.time.delay(delay)

                arr[j].color = regular_color
                arr[j - gap].color = regular_color

                swap_elements(arr, j, j - gap)
                j -= gap
                yield
        gap //= 2