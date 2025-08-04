class Cube:
    def __init__(self):
        self.faces = {
            'U': [['W'] * 3 for _ in range(3)],
            'D': [['Y'] * 3 for _ in range(3)],
            'F': [['G'] * 3 for _ in range(3)],
            'B': [['B'] * 3 for _ in range(3)],
            'L': [['O'] * 3 for _ in range(3)],
            'R': [['R'] * 3 for _ in range(3)],
        }

    def rotate_face_clockwise(self, face):
        self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]

    def rotate_face_counterclockwise(self, face):
        self.faces[face] = [list(row) for row in zip(*self.faces[face])][::-1]

    def move(self, notation):
        move_map = {
            'U': self.move_U,
            "U'": self.move_U_prime,
            'U2': lambda: (self.move_U(), self.move_U()),
            'D': self.move_D,
            "D'": self.move_D_prime,
            'D2': lambda: (self.move_D(), self.move_D()),
            'F': self.move_F,
            "F'": self.move_F_prime,
            'F2': lambda: (self.move_F(), self.move_F()),
            'B': self.move_B,
            "B'": self.move_B_prime,
            'B2': lambda: (self.move_B(), self.move_B()),
            'L': self.move_L,
            "L'": self.move_L_prime,
            'L2': lambda: (self.move_L(), self.move_L()),
            'R': self.move_R,
            "R'": self.move_R_prime,
            'R2': lambda: (self.move_R(), self.move_R()),
        }

        if notation in move_map:
            move_map[notation]()
        else:
            print(f"Invalid move: {notation}")

    def do_moves(self, moves):
        for move in moves:
            self.move(move)

    def get_face(self, face):
        return self.faces[face]

    def print_cube(self):
        for face in ['U', 'D', 'F', 'B', 'L', 'R']:
            print(f"{face} face:")
            for row in self.faces[face]:
                print(" ".join(row))
            print()

    def move_U(self):
        self.rotate_face_clockwise('U')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = F[0][:]
        F[0], R[0], B[0], L[0] = L[0], F[0], R[0], B[0]
        R[0] = temp

    def move_U_prime(self):
        self.rotate_face_counterclockwise('U')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = F[0][:]
        F[0], L[0], B[0], R[0] = R[0], F[0], L[0], B[0]
        L[0] = temp

    def move_D(self):
        self.rotate_face_clockwise('D')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = F[2][:]
        F[2], L[2], B[2], R[2] = R[2], F[2], L[2], B[2]
        L[2] = temp

    def move_D_prime(self):
        self.rotate_face_counterclockwise('D')
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        temp = F[2][:]
        F[2], R[2], B[2], L[2] = L[2], F[2], R[2], B[2]
        R[2] = temp

    def move_F(self):
        self.rotate_face_clockwise('F')
        U, D, L, R = self.faces['U'], self.faces['D'], self.faces['L'], self.faces['R']
        temp = U[2][:]
        U[2] = [L[i][2] for i in reversed(range(3))]
        for i in range(3):
            L[i][2] = D[0][i]
        D[0] = [R[i][0] for i in reversed(range(3))]
        for i in range(3):
            R[i][0] = temp[i]

    def move_F_prime(self):
        self.rotate_face_counterclockwise('F')
        U, D, L, R = self.faces['U'], self.faces['D'], self.faces['L'], self.faces['R']
        temp = U[2][:]
        U[2] = [R[i][0] for i in range(3)]
        for i in range(3):
            R[i][0] = D[0][2 - i]
        D[0] = [L[i][2] for i in range(3)]
        for i in range(3):
            L[i][2] = temp[2 - i]

    def move_B(self):
        self.rotate_face_clockwise('B')
        U, D, L, R = self.faces['U'], self.faces['D'], self.faces['L'], self.faces['R']
        temp = U[0][:]
        U[0] = [R[i][2] for i in range(3)]
        for i in range(3):
            R[i][2] = D[2][2 - i]
        D[2] = [L[i][0] for i in range(3)]
        for i in range(3):
            L[i][0] = temp[2 - i]

    def move_B_prime(self):
        self.rotate_face_counterclockwise('B')
        U, D, L, R = self.faces['U'], self.faces['D'], self.faces['L'], self.faces['R']
        temp = U[0][:]
        U[0] = [L[i][0] for i in reversed(range(3))]
        for i in range(3):
            L[i][0] = D[2][i]
        D[2] = [R[i][2] for i in reversed(range(3))]
        for i in range(3):
            R[i][2] = temp[i]

    def move_L(self):
        self.rotate_face_clockwise('L')
        U, D, F, B = self.faces['U'], self.faces['D'], self.faces['F'], self.faces['B']
        temp = [U[i][0] for i in range(3)]
        for i in range(3):
            U[i][0] = B[2 - i][2]
            B[2 - i][2] = D[i][0]
            D[i][0] = F[i][0]
            F[i][0] = temp[i]

    def move_L_prime(self):
        self.rotate_face_counterclockwise('L')
        U, D, F, B = self.faces['U'], self.faces['D'], self.faces['F'], self.faces['B']
        temp = [U[i][0] for i in range(3)]
        for i in range(3):
            U[i][0] = F[i][0]
            F[i][0] = D[i][0]
            D[i][0] = B[2 - i][2]
            B[2 - i][2] = temp[i]

    def move_R(self):
        self.rotate_face_clockwise('R')
        U, D, F, B = self.faces['U'], self.faces['D'], self.faces['F'], self.faces['B']
        temp = [U[i][2] for i in range(3)]
        for i in range(3):
            U[i][2] = F[i][2]
            F[i][2] = D[i][2]
            D[i][2] = B[2 - i][0]
            B[2 - i][0] = temp[i]

    def move_R_prime(self):
        self.rotate_face_counterclockwise('R')
        U, D, F, B = self.faces['U'], self.faces['D'], self.faces['F'], self.faces['B']
        temp = [U[i][2] for i in range(3)]
        for i in range(3):
            U[i][2] = B[2 - i][0]
            B[2 - i][0] = D[i][2]
            D[i][2] = F[i][2]
            F[i][2] = temp[i]
