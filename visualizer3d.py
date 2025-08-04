from vpython import box, vector, color, scene

face_colors = {
    'W': color.white,
    'Y': color.yellow,
    'G': color.green,
    'B': color.blue,
    'O': color.orange,
    'R': color.red
}

def draw_3d_cube(cube_faces):
    scene.title = "3D Rubik's Cube"
    scene.background = color.gray(0.2)
    scene.width = 800
    scene.height = 600

    face_positions = {
        'U': lambda i, j: vector(j - 1, 1, -(i - 1)),
        'D': lambda i, j: vector(j - 1, -1, i - 1),
        'F': lambda i, j: vector(j - 1, -(i - 1), 1),
        'B': lambda i, j: vector(-(j - 1), -(i - 1), -1),
        'L': lambda i, j: vector(-1, -(i - 1), -(j - 1)),
        'R': lambda i, j: vector(1, -(i - 1), j - 1)
    }

    for face in cube_faces:
        for i in range(3):
            for j in range(3):
                color_code = cube_faces[face][i][j]
                block_color = face_colors.get(color_code, color.gray(0.5))
                pos = face_positions[face](i, j)
                box(pos=pos, size=vector(0.95, 0.95, 0.1), color=block_color)

