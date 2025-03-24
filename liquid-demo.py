import math
import time
import numpy as np


ascii_elements = '·+*#%@░▒▓██'
global wave_row
global wave_matrix
global wave_values
size = 100

def init():
    global wave_row
    global wave_matrix
    wave_row = []
    wave_matrix = []
    for _ in range(size):
        wave_row.append(ascii_elements[0])
    for _ in range(size):
        wave_matrix.append(wave_row.copy())

def get_wave_values():
    global wave_values
    amplitude = .2
    frequency = 0
    x_cursor = 0
    sample_rate = math.pi/8
    wave_values = []
    for _ in range(size):
        wave_values.append(
            int(round(amplitude*(math.sin(x_cursor)),1)*10)
            )
        x_cursor += sample_rate

    
def draw():
    global wave_values
    global wave_matrix
    offset = size/2 # to start in the middle
    for _ in range(size):
        wave_matrix[int(wave_values[_] + offset)][_] = ascii_elements[2] 

def run():
    global wave_matrix
    init()
    get_wave_values()
    draw()
    for i in wave_matrix:
        print(' '.join(map(str, i)))

run()