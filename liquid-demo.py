# Import math Library
import math 
ascii_elements = '·+*#%@░▒▓██'
wave_row = []
wave_matrix = []

i = 0 # counter
pi = math.pi # pi value
n = 100 # Iteration number.
for iterations in range(n):
    while i < pi*n and i <= pi:
        j = abs(round(math.sin(i),1))
        j = (j*10) 
        wave_row.append(ascii_elements[int(j)])
        i+=pi/n
wave_row = "".join(wave_row)
print(wave_row)