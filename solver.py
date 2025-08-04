# solver.py
from cube import Cube
import copy

class Solver:

    def _is_inverse_move(self, move1, move2):
        return (
            move1[0] == move2[0] and (
            move1 == move2 + "'" or move2 == move1 + "'" or
            (move1.endswith('2') and move2.endswith('2')) or
            (move1 == move2)
        )
    )


    def __init__(self, cube: Cube):
        self.initial_cube = cube
        self.moves = ['U', "U'", 'U2', 'D', "D'", 'D2', 'F', "F'", 'F2',
                      'B', "B'", 'B2', 'L', "L'", 'L2', 'R', "R'", 'R2']

    def is_solved(self, cube):
        for face in cube.faces:
            center = cube.faces[face][1][1]
            if not all(sticker == center for row in cube.faces[face] for sticker in row):
                return False
        return True

    def heuristic(self, cube):
        cost = 0
        for face in cube.faces:
            center = cube.faces[face][1][1]
            for row in cube.faces[face]:
                for sticker in row:
                    if sticker != center:
                        cost += 1
        return cost



    def apply_move(self, cube, move):
        cube_copy = copy.deepcopy(cube)
        cube_copy.move(move)
        return cube_copy

    def ida_star(self):
        threshold = self.heuristic(self.initial_cube)
        path = []
        print(f"Initial heuristic threshold: {threshold}")

        while True:
            temp = self._search(self.initial_cube, 0, threshold, path, set())
            if isinstance(temp, list):  # Found solution
                return temp
            if temp == float('inf'):   # No solution
                return None
            threshold = temp  # Increase threshold

    def _search(self, cube, g, threshold, path, visited):
        f = g + self.heuristic(cube)
        #print(f"Depth: {g}, f: {f}, threshold: {threshold}, path so far: {path}")
        if f > threshold:
            return f
        if self.is_solved(cube):
            return path

        min_cost = float('inf')
        if g > 20:
            return float('inf')  # optional safety cap for now

        for move in self.moves:
            if path and self._is_inverse_move(move, path[-1]):
                continue

            new_cube = self.apply_move(cube, move)
            cube_state = str(new_cube.faces)
            if cube_state in visited:
                continue

            visited.add(cube_state)
            result = self._search(new_cube, g + 1, threshold, path + [move], visited)
            visited.remove(cube_state)

            if isinstance(result, list):
                return result

            if result is not None and result < min_cost:
                min_cost = result

        return min_cost if min_cost != float('inf') else float('inf')
