
# 🧊 Rubik's Cube Solver

A Python-based Rubik’s Cube Solver that uses the Iterative Deepening A\* (IDA\*) search algorithm and 2D visualization to find and display the solution to any scrambled 3x3 Rubik’s Cube.

## 🚀 Features

* Simulates a standard 3x3 Rubik’s Cube
* Custom scramble with move sequences
* Solver powered by the IDA\* search algorithm
* Visualizes the cube using matplotlib
* Modular and beginner-friendly codebase

## 📦 Requirements

* Python 3.8 or above
* matplotlib
* numpy

Install dependencies:

pip install matplotlib numpy

## 🔁 Usage

To scramble and solve the cube:

from cube import Cube
from solver import Solver

cube = Cube()
cube.do\_moves("R U R' U R U2 R'".split())  # Example scramble

solver = Solver(cube)
solution = solver.ida\_star()

if solution:
  print("Solution:", solution)
else:
  print("No solution found.")

To visualize the cube state:

from visualizer import draw\_cube
draw\_cube(cube)

## 🧠 Algorithm: IDA\*

This project uses the Iterative Deepening A\* (IDA\*) algorithm which combines the benefits of depth-first search and A\* by incrementally deepening the search while pruning states based on a heuristic estimate.

## 📸 Screenshots

(Add cube images or output screenshots here if available)

## ✨ Future Improvements

* Add animated GUI for solving steps
* Improve heuristics for faster solving
* Add support for other cube types (2x2, 4x4)
* Include step-by-step solving guide or logs

## 🤝 Contributing

Pull requests are welcome! For any feature suggestions or issues, feel free to open an issue.

## 📜 License

This project is licensed under the MIT License.

---

Let me know if you want to personalize the name or credits at the bottom.
