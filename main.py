from cube import Cube
from solver import Solver
from visualizer import animate_moves
from visualizer3d import draw_3d_cube

# Create cube and scramble it
cube = Cube()
scramble = "R U R'".split()
cube.do_moves(scramble)
print("Scramble:", scramble)
draw_3d_cube(cube.faces)
animate_moves(cube, scramble)

# Solve the cube
solver = Solver(cube)
solution = solver.ida_star()

if solution:
    print("Solution:", solution)

    # Animate solving moves
    animate_moves(cube, solution)

    # Final solved state in 3D
    draw_3d_cube(cube.faces)
    cube.print_cube()

else:
    print("No solution found.")
