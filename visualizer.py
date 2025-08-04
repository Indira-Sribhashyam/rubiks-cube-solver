#visualizer.py

import matplotlib.pyplot as plt
import time

def draw_cube(cube, ax):
    color_map = {
        'W': 'white', 'Y': 'yellow',
        'G': 'green', 'B': 'blue',
        'O': 'orange', 'R': 'red'
    }

    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')

    layout = {
        'U': (0, 3),
        'L': (3, 0),
        'F': (3, 3),
        'R': (3, 6),
        'B': (3, 9),
        'D': (6, 3),
    }

    for face, (row_offset, col_offset) in layout.items():
        for i in range(3):
            for j in range(3):
                color = color_map.get(cube[face][i][j], 'gray')
                rect = plt.Rectangle((col_offset + j, -row_offset - i), 1, 1,
                                     facecolor=color, edgecolor='black')
                ax.add_patch(rect)

    ax.set_xlim(0, 12)
    ax.set_ylim(-10, 1)
    plt.draw()
    plt.pause(0.5)

def animate_moves(cube_obj, moves):
    fig, ax = plt.subplots()
    draw_cube(cube_obj.faces, ax)
    time.sleep(1)

    for move in moves:
        cube_obj.move(move)
        draw_cube(cube_obj.faces, ax)
        time.sleep(0.5)
