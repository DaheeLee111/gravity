from OpenGL.GL import *
from OpenGL.GLU import *

import math


class Squre:
    def __init__(self, center, x, y, z):
        self.center = center
        self.x = x
        self.y = y
        self.z = z

        self.vertices = [
            [self.center[0]-x/2, self.center[1]-y/2, self.center[2]-z/2],
            [self.center[0]-x/2, self.center[1]+y/2, self.center[2]-z/2],
            [self.center[0]+x/2, self.center[1]+y/2, self.center[2]-z/2],
            [self.center[0]+x/2, self.center[1]-y/2, self.center[2]-z/2],
            [self.center[0]-x/2, self.center[1]-y/2, self.center[2]+z/2],
            [self.center[0]-x/2, self.center[1]+y/2, self.center[2]+z/2],
            [self.center[0]+x/2, self.center[1]+y/2, self.center[2]+z/2],
            [self.center[0]+x/2, self.center[1]-y/2, self.center[2]+z/2],
            [self.center[0] + x/5, self.center[1], self.center[2]],
            [self.center[0] - x/5, self.center[1], self.center[2]],
            [self.center[0], self.center[1] + y/5, self.center[2]],
            [self.center[0], self.center[1] - y/5, self.center[2]],
            [self.center[0], self.center[1], self.center[2] + z/5],
            [self.center[0], self.center[1], self.center[2] - z/5],
        ]

        self.edges = (
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7],
            [8, 9], [10, 11], [12, 13]
        )

    def begin_and_end(func):
        def wrapper(self):
            glBegin(GL_LINES)
            func(self)
            glEnd()

        return wrapper

    @begin_and_end
    def drawSqure(self):
        for vertice in self.edges:
            glVertex3fv(self.vertices[vertice[0]])
            glVertex3fv(self.vertices[vertice[1]])

    def move_by_x(self, distance):
        result = []
        for vertex in self.vertices:
            result.append([vertex[0] + distance, vertex[1], vertex[2]])
        self.vertices = result

    def move_by_y(self, distance):
        result = []
        for vertex in self.vertices:
            result.append([vertex[0], vertex[1] + distance, vertex[2]])
        self.vertices = result

    def rotate_by_z(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        result = []

        for vertex in self.vertices:
            rotated = [
                ((vertex[0] - self.vertices[0][0]) * matrix[0][0] -
                 (vertex[1] - self.vertices[0][1]) * matrix[0][1]) + self.vertices[0][0],
                ((vertex[0] - self.vertices[0][0]) * matrix[1][0] +
                 (vertex[1] - self.vertices[0][1]) * matrix[1][1]) + self.vertices[0][1],
                vertex[2]
            ]
            result.append(rotated)

        self.vertices = result

    def rotate_by_y(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        result = []

        for vertex in self.vertices:
            rotated = [
                ((vertex[0] - self.vertices[0][0]) * matrix[0][0] - (vertex[2] -
                 self.vertices[0][2]) * matrix[0][1]) + self.vertices[0][0],
                vertex[1],
                ((vertex[0] - self.vertices[0][0]) * matrix[1][0] + (vertex[2] -
                 self.vertices[0][2]) * matrix[1][1]) + self.vertices[0][2]
            ]
            result.append(rotated)

        self.vertices = result

    def rotate_by_x(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        result = []

        for vertex in self.vertices:
            rotated = [
                vertex[0],
                ((vertex[1] - self.vertices[0][1]) * matrix[0][0] -
                 (vertex[2] - self.vertices[0][2]) * matrix[0][1]) + self.vertices[0][1],
                ((vertex[1] - self.vertices[0][1]) * matrix[1][0] +
                 (vertex[2] - self.vertices[0][2]) * matrix[1][1]) + self.vertices[0][2]
            ]
            result.append(rotated)

        self.vertices = result

    def angle_x(self):
        return self.vertices[0][0] - self.vertices[6][0]

    def angle_z(self):
        return self.vertices[0][2] - self.vertices[6][2]
