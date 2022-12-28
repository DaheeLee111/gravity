from OpenGL.GL import *
from OpenGL.GLU import *

import math


class Squre:
    def __init__(self, center, x, y, z):
        self.center = center
        self.x = x
        self.y = y
        self.z = z

        self.vertices = {
            "cube": [
                [self.center[0]-x/2, self.center[1]-y/2, self.center[2]-z/2],
                [self.center[0]-x/2, self.center[1]+y/2, self.center[2]-z/2],
                [self.center[0]+x/2, self.center[1]+y/2, self.center[2]-z/2],
                [self.center[0]+x/2, self.center[1]-y/2, self.center[2]-z/2],
                [self.center[0]-x/2, self.center[1]-y/2, self.center[2]+z/2],
                [self.center[0]-x/2, self.center[1]+y/2, self.center[2]+z/2],
                [self.center[0]+x/2, self.center[1]+y/2, self.center[2]+z/2],
                [self.center[0]+x/2, self.center[1]-y/2, self.center[2]+z/2],
            ],
            "crosshair": [
                [self.center[0], self.center[1], self.center[2]],
                [self.center[0], self.center[1], self.center[2]-z/2],
                [self.center[0]-x/2, self.center[1], self.center[2]],
                [self.center[0], self.center[1]-y/2, self.center[2]],
            ],
            "circle": [
                [self.center[0], self.center[1], self.center[2]-z/2],
                [self.center[0]+x/3, self.center[1], self.center[2]-z/2],
                [self.center[0]-x/3, self.center[1], self.center[2]-z/2],
                [self.center[0], self.center[1]+y/3, self.center[2]-z/2],
                [self.center[0], self.center[1]-y/3, self.center[2]-z/2],
                [self.center[0]-x/2, self.center[1], self.center[2]],
                [self.center[0]-x/2, self.center[1], self.center[2]+z/3],
                [self.center[0]-x/2, self.center[1], self.center[2]-z/3],
                [self.center[0]-x/2, self.center[1]+y/3, self.center[2]],
                [self.center[0]-x/2, self.center[1]-y/3, self.center[2]],
                [self.center[0], self.center[1]-y/2, self.center[2]],
                [self.center[0]+x/3, self.center[1]-y/2, self.center[2]],
                [self.center[0]-x/3, self.center[1]-y/2, self.center[2]],
                [self.center[0], self.center[1]-y/2, self.center[2]+z/3],
                [self.center[0], self.center[1]-y/2, self.center[2]-z/3],
            ]
        }

        self.lines = {
            "cube": [
                [0, 1], [1, 2], [2, 3], [3, 0],
                [4, 5], [5, 6], [6, 7], [7, 4],
                [0, 4], [1, 5], [2, 6], [3, 7],
            ],
            "crosshair": [
                [0, 1], [0, 2], [0, 3]
            ],
            "circle": [
                [0, 1], [0, 2], [0, 3], [0, 4],
                [5, 6], [5, 7], [5, 8], [5, 9],
                [10, 11], [10, 12], [10, 13], [10, 14]
            ]
        }

    def begin_and_end(func):
        def wrapper(self):
            glBegin(GL_LINES)
            func(self)
            glEnd()
        return wrapper

    @ begin_and_end
    def drawSqure(self):
        for element in self.lines:
            for vertex in self.lines[element]:
                if element == "circle":
                    glColor(0, 255, 255)
                else:
                    glColor(255, 255, 255)
                glVertex3fv(self.vertices[element][vertex[0]])
                glVertex3fv(self.vertices[element][vertex[1]])

    def move_to_x(self, distance):
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([vertex[0] + distance, vertex[1], vertex[2]])
            self.vertices[element] = result

    def move_to_y(self, distance):
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([vertex[0], vertex[1] + distance, vertex[2]])
            self.vertices[element] = result

    def rotate_by_z(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([
                    ((vertex[0] - self.vertices["cube"][0][0]) * matrix[0][0] - (vertex[1] - self.vertices["cube"][0][1]) * matrix[0][1]) + self.vertices["cube"][0][0],
                    ((vertex[0] - self.vertices["cube"][0][0]) * matrix[1][0] + (vertex[1] - self.vertices["cube"][0][1]) * matrix[1][1]) + self.vertices["cube"][0][1],
                    vertex[2]
                ])
            self.vertices[element] = result

    def rotate_by_y(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([
                    ((vertex[0] - self.vertices["cube"][0][0]) * matrix[0][0] - (vertex[2] - self.vertices["cube"][0][2]) * matrix[0][1]) + self.vertices["cube"][0][0],
                    vertex[1],
                    ((vertex[0] - self.vertices["cube"][0][0]) * matrix[1][0] + (vertex[2] - self.vertices["cube"][0][2]) * matrix[1][1]) + self.vertices["cube"][0][2]
                ])
            self.vertices[element] = result

    def rotate_by_x(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([
                    vertex[0],
                    ((vertex[1] - self.vertices["cube"][0][1]) * matrix[0][0] - (vertex[2] - self.vertices["cube"][0][2]) * matrix[0][1]) + self.vertices["cube"][0][1],
                    ((vertex[1] - self.vertices["cube"][0][1]) * matrix[1][0] + (vertex[2] - self.vertices["cube"][0][2]) * matrix[1][1]) + self.vertices["cube"][0][2]
                ])
            self.vertices[element] = result

    def angle_x(self):
        return -round(self.vertices["cube"][0][0] - self.vertices["cube"][6][0], 2) * 10

    def angle_z(self):
        return round(self.vertices["cube"][0][2] - self.vertices["cube"][6][2], 2) * 10
