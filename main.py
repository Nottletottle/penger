import math
import tkinter as tk

from penger import EDGES, POINTS

BACKGROUND = "yellow"
FOREGROUND = "blue"
CANVAS_HEIGHT = 800
CANVAS_WIDTH = 800
FPS = 60

root = tk.Tk()
canvas = tk.Canvas(root, bg=BACKGROUND, height=800, width=800)

dz = 0.0
angle_x = 0.0
angle_y = 0.0
MAX_ZOOM = 1.2


class ScreenPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_screen(self, width, height):
        return ScreenPoint(
            (self.x + 1) * 0.5 * width,
            (1 - (self.y + 1) * 0.5) * height,
        )


class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def project(self):
        return Point2D(self.x / self.z, self.y / self.z)


def rotate_x(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return (x, y * cos_a - z * sin_a, y * sin_a + z * cos_a)


def rotate_y(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return (x * cos_a + z * sin_a, y, -x * sin_a + z * cos_a)


def draw_point(canvas, point: ScreenPoint, size=20):
    half = size / 2
    canvas.create_rectangle(
        point.x - half,
        point.y - half,
        point.x + size,
        point.y + size,
        fill=FOREGROUND,
        outline=FOREGROUND,
    )


def draw_line(canvas, p1, p2):
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="red")


def draw_shape(points):
    projected = []
    for point in points:
        rotated = rotate_x(rotate_y(point, angle_x), 6)
        x, y, z = rotated

        p3 = Point3D(x, y, z + 1.2)

        p2 = p3.project()
        screen_point = p2.to_screen(CANVAS_WIDTH, CANVAS_HEIGHT)
        projected.append(screen_point)

    for i, j in EDGES:
        draw_line(canvas, projected[i], projected[j])

    # for p in projected:
    # draw_point(canvas, p, size=3)


def animate():
    global angle_x, angle_y
    #
    # if dz < MAX_ZOOM:
    #     zoom_speed = 0.2
    #     dz += zoom_speed / FPS
    #     dz = min(dz, MAX_ZOOM)

    rotation_speed = 1.0
    angle_x += rotation_speed / FPS
    angle_y += rotation_speed / FPS

    canvas.delete("all")
    draw_shape(POINTS)
    root.after(1000 // FPS, animate)


animate()
canvas.pack()
root.mainloop()
