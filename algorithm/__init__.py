import pygame

def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def buble_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    swap_count = 0
    access_count = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            access_count += 1
            arr[j].color = check_color
            arr[j + 1].color = replace_color
            draw_scene(window, swap_count, access_count)
            pygame.time.delay(delay)
            if arr[j].val > arr[j + 1].val:
                swap_elements(arr, j, j + 1)
                swap_count += 1
            arr[j].color = regular_color
            arr[j + 1].color = regular_color
            yield

def insertion_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    swap_count = 0
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j].val < arr[j - 1].val and j > 0:
            swap_count += 1
            arr[j].color = check_color
            arr[j - 1].color = replace_color
            draw_scene(window, swap_count, swap_count)
            pygame.time.delay(delay) 

            arr[j].color = regular_color
            arr[j - 1].color = regular_color

            swap_elements(arr, j, j - 1)
            j -= 1
            yield

def selection_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    swap_count = 0
    access_count = 0
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        arr[i].color = check_color
        for j in range(i + 1, n):
            access_count += 1
            arr[j].color = replace_color
            draw_scene(window, swap_count, access_count)
            pygame.time.delay(delay)
            if arr[j].val < arr[min_index].val:
                min_index = j

            arr[j].color = regular_color
            yield
            
        arr[i].color = regular_color
        
        swap_count += 1
        swap_elements(arr, min_index, i)     

def shell_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    swap_count = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j].val < arr[j - gap].val:
                swap_count += 1
                arr[j].color = check_color
                arr[j - gap].color = replace_color
                draw_scene(window, swap_count, swap_count)
                pygame.time.delay(delay)

                arr[j].color = regular_color
                arr[j - gap].color = regular_color

                swap_elements(arr, j, j - gap)
                j -= gap
                yield
        gap //= 2

def counting_sort(arr, exp, draw_scene, window, check_color, replace_color, regular_color, delay):
    swap_count = 0
    n = len(arr)
    count_arr = [0] * 10

    for i in range(n):
        digit = arr[i].val // exp % 10
        count_arr[digit] += 1

    for i in range(1, 10):
        count_arr[i] += count_arr[i - 1]

    out = [0] * n
    for i in range(n - 1, -1, -1):
        swap_count += 1
        arr[i].color = check_color
        arr[count_arr[digit] - 1].color = replace_color
        draw_scene(window, swap_count, swap_count)
        pygame.time.delay(delay) 

        arr[i].color = regular_color
        arr[count_arr[digit] - 1].color = regular_color

        digit = arr[i].val // exp % 10
        out[count_arr[digit] - 1] = arr[i]
        count_arr[digit] -= 1
        yield
    
    for i in range(n):
        arr[i] = out[i]
        arr[i].color = regular_color
        yield

def radix_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    m = max([rect.val for rect in arr])

    exp = 1
    while m // exp > 0:
        yield from counting_sort(arr, exp, draw_scene, window, check_color, replace_color, regular_color, delay)
        exp *= 10

def shaker_sort(arr, draw_scene, window, check_color, replace_color, regular_color, delay):
    swap_count = 0
    access_count = 0
    left = 0
    right = len(arr) - 1
    k = left
    last_swap = left

    while left < right:
        while k < right:
            access_count += 1
            arr[k].color = check_color
            arr[k + 1].color = replace_color
            draw_scene(window, swap_count, access_count)
            pygame.time.delay(delay) 

            if arr[k].val > arr[k + 1].val:
                swap_elements(arr, k, k + 1)
                last_swap = k
                swap_count += 1

            arr[k].color = regular_color
            arr[k + 1].color = regular_color

            k += 1
            yield

        right = last_swap
        k = right

        while k > left:
            access_count += 1
            arr[k].color = check_color
            arr[k - 1].color = replace_color
            draw_scene(window, swap_count, access_count)
            pygame.time.delay(delay) 
            if arr[k].val < arr[k - 1].val:
                swap_elements(arr, k, k - 1)
                last_swap = k
                swap_count += 1

            arr[k].color = regular_color
            arr[k - 1].color = regular_color

            k -= 1
            yield

        left = last_swap
        k = left