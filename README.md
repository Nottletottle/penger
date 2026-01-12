# 3D Point Projection in Python (Tkinter)

This is a small educational project written in Python to explore how **3D objects can be projected onto a 2D screen** using basic math and perspective projection.

The goal of the project is not performance or visual fidelity, but understanding:
- 3D coordinate systems
- Rotation in 3D space
- Perspective projection
- Mapping normalized coordinates to screen space

Rendering is done using Python’s built-in `tkinter` library.

---

## Features

- Manual implementation of:
  - 3D → 2D perspective projection
  - Rotation around X and Y axes
- Frame-based animation using `tkinter.after`
- Wireframe rendering using edges between points
- Simple and minimal math-based pipeline

---

## How It Works

1. **3D Points**
   - The shape is defined as a list of 3D points (`POINTS`) and edges (`EDGES`).

2. **Rotation**
   - Each frame, points are rotated around the X and Y axes using rotation matrices.

3. **Perspective Projection**
   - 3D points are projected onto a 2D plane using:
     ```
     x' = x / z
     y' = y / z
     ```
   - This creates a depth illusion where distant points appear smaller.

4. **Screen Mapping**
   - Normalized 2D coordinates are converted into screen coordinates based on canvas size.

5. **Rendering**
   - Lines are drawn between projected points using the edge list to create a wireframe.

---

## Requirements

- Python 3.x
- No external dependencies

---

## Demo

![3D wireframe rotation demo](animation.gif)

### Model made by:
https://github.com/Max-Kawula

---

## Running the Project

```bash
python main.py
