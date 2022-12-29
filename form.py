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
            "wheel_z": [
                [self.center[0], self.center[1], self.center[2]-z/2],
                [self.center[0]+x/3, self.center[1], self.center[2]-z/2],
                [self.center[0]-x/3, self.center[1], self.center[2]-z/2],
                [self.center[0], self.center[1]+y/3, self.center[2]-z/2],
                [self.center[0], self.center[1]-y/3, self.center[2]-z/2],
            ],
            "wheel_x": [
                [self.center[0]-x/2, self.center[1], self.center[2]],
                [self.center[0]-x/2, self.center[1], self.center[2]+z/3],
                [self.center[0]-x/2, self.center[1], self.center[2]-z/3],
                [self.center[0]-x/2, self.center[1]+y/3, self.center[2]],
                [self.center[0]-x/2, self.center[1]-y/3, self.center[2]],
            ],
            "wheel_y": [
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
            "wheel_z": [
                [0, 1], [0, 2], [0, 3], [0, 4],
            ],
            "wheel_x": [
                [0, 1], [0, 2], [0, 3], [0, 4],
            ],
            "wheel_y": [
                [0, 1], [0, 2], [0, 3], [0, 4],
            ]
        }
        self.reaction = 20

    def angle_x(self):
        return -round(self.vertices["cube"][0][0] - self.vertices["cube"][6][0], 2) * 10

    def angle_z(self):
        return round(self.vertices["cube"][0][2] - self.vertices["cube"][6][2], 2) * 10

    def drawSqure(self):
        glBegin(GL_LINES)
        for element in self.lines:
            for vertex in self.lines[element]:
                if element == "wheel_z" or element == "wheel_y" or element == "wheel_x":
                    glColor(0, 255, 255)
                elif element == "crosshair":
                    glColor(255, 0, 255)
                else:
                    glColor(255, 255, 255)
                glVertex3fv(self.vertices[element][vertex[0]])
                glVertex3fv(self.vertices[element][vertex[1]])
        glEnd()

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

    def move_to_Z(self, distance):
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([vertex[0], vertex[1], vertex[2] + distance])
            self.vertices[element] = result

    def rotate_x(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([
                    vertex[0],
                    vertex[1] * matrix[0][0] - vertex[2] * matrix[0][1],
                    vertex[1] * matrix[1][0] + vertex[2] * matrix[1][1]
                ])
            self.vertices[element] = result

    def rotate_y(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([
                    vertex[0] * matrix[0][0] - vertex[2] * matrix[0][1],
                    vertex[1],
                    vertex[0] * matrix[1][0] + vertex[2] * matrix[1][1]
                ])
            self.vertices[element] = result

    def rotate_z(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        for element in self.vertices:
            result = []
            for vertex in self.vertices[element]:
                result.append([
                    vertex[0] * matrix[0][0] - vertex[1] * matrix[0][1],
                    vertex[0] * matrix[1][0] + vertex[1] * matrix[1][1],
                    vertex[2]
                ])
            self.vertices[element] = result

    # def rotate_x_axis_wheel(self, angle):
    #     matrix = [
    #         [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
    #         [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
    #     ]
    #     result = []
    #     for vertex in self.vertices["wheel_x"]:
    #         result.append([
    #             vertex[0],
    #             ((vertex[1] - self.vertices["wheel_x"][0][1]) * matrix[0][0] - (vertex[2] - self.vertices["wheel_x"][0][2]) * matrix[0][1]) + self.vertices["wheel_x"][0][1],
    #             ((vertex[1] - self.vertices["wheel_x"][0][1]) * matrix[1][0] + (vertex[2] - self.vertices["wheel_x"][0][2]) * matrix[1][1]) + self.vertices["wheel_x"][0][2]
    #         ])
    #     self.vertices["wheel_x"] = result
    #     self.rotate_x(-angle/self.reaction)

    # def rotate_y_axis_wheel(self, angle):
    #     matrix = [
    #         [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
    #         [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
    #     ]
    #     result = []
    #     for vertex in self.vertices["wheel_y"]:
    #         result.append([
    #             ((vertex[0] - self.vertices["wheel_y"][0][0]) * matrix[0][0] - (vertex[2] - self.vertices["wheel_y"][0][2]) * matrix[0][1]) + self.vertices["wheel_y"][0][0],
    #             vertex[1],
    #             ((vertex[0] - self.vertices["wheel_y"][0][0]) * matrix[1][0] + (vertex[2] - self.vertices["wheel_y"][0][2]) * matrix[1][1]) + self.vertices["wheel_y"][0][2]
    #         ])
    #     self.vertices["wheel_y"] = result
    #     self.rotate_y(-angle/self.reaction)

    # def rotate_z_axis_wheel(self, angle):
    #     matrix = [
    #         [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
    #         [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
    #     ]
    #     result = []
    #     for vertex in self.vertices["wheel_z"]:
    #         result.append([
    #             ((vertex[0] - self.vertices["wheel_z"][0][0]) * matrix[0][0] - (vertex[1] - self.vertices["wheel_z"][0][1]) * matrix[0][1]) + self.vertices["wheel_z"][0][0],
    #             ((vertex[0] - self.vertices["wheel_z"][0][0]) * matrix[1][0] + (vertex[1] - self.vertices["wheel_z"][0][1]) * matrix[1][1]) + self.vertices["wheel_z"][0][1],
    #             vertex[2]
    #         ])
    #     self.vertices["wheel_z"] = result
    #     self.rotate_z(-angle/self.reaction)

    def rotate_x_axis_wheel(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        result = []
        data = []
        for vertex in self.vertices["wheel_x"]:
            result.append([
                vertex[0],
                ((vertex[1] - self.vertices["wheel_x"][0][1]) * matrix[0][0] - (vertex[2] - self.vertices["wheel_x"][0][2]) * matrix[0][1]) + self.vertices["wheel_x"][0][1],
                ((vertex[1] - self.vertices["wheel_x"][0][1]) * matrix[1][0] + (vertex[2] - self.vertices["wheel_x"][0][2]) * matrix[1][1]) + self.vertices["wheel_x"][0][2]
            ])
            data.append([
                vertex[0],
                ((vertex[1] - self.vertices["wheel_x"][0][1]) * matrix[0][0] - (vertex[2] - self.vertices["wheel_x"][0][2]) * matrix[0][1]) + self.vertices["wheel_x"][0][1],
                ((vertex[1] - self.vertices["wheel_x"][0][1]) * matrix[1][0] + (vertex[2] - self.vertices["wheel_x"][0][2]) * matrix[1][1]) + self.vertices["wheel_x"][0][2]
            ])
            data.append([
                ((vertex[0] - self.vertices["wheel_y"][0][0]) * matrix[0][0] - (vertex[2] - self.vertices["wheel_y"][0][2]) * matrix[0][1]) + self.vertices["wheel_y"][0][0],
                vertex[1],
                ((vertex[0] - self.vertices["wheel_y"][0][0]) * matrix[1][0] + (vertex[2] - self.vertices["wheel_y"][0][2]) * matrix[1][1]) + self.vertices["wheel_y"][0][2]
            ])
            data.append([
                ((vertex[0] - self.vertices["wheel_z"][0][0]) * matrix[0][0] - (vertex[1] - self.vertices["wheel_z"][0][1]) * matrix[0][1]) + self.vertices["wheel_z"][0][0],
                ((vertex[0] - self.vertices["wheel_z"][0][0]) * matrix[1][0] + (vertex[1] - self.vertices["wheel_z"][0][1]) * matrix[1][1]) + self.vertices["wheel_z"][0][1],
                vertex[2]
            ])
        print(data)
        self.vertices["wheel_x"] = result
        self.rotate_x(-angle/self.reaction)

    def rotate_y_axis_wheel(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        result = []
        for vertex in self.vertices["wheel_y"]:
            result.append([
                ((vertex[0] - self.vertices["wheel_y"][0][0]) * matrix[0][0] - (vertex[2] - self.vertices["wheel_y"][0][2]) * matrix[0][1]) + self.vertices["wheel_y"][0][0],
                vertex[1],
                ((vertex[0] - self.vertices["wheel_y"][0][0]) * matrix[1][0] + (vertex[2] - self.vertices["wheel_y"][0][2]) * matrix[1][1]) + self.vertices["wheel_y"][0][2]
            ])
        self.vertices["wheel_y"] = result
        self.rotate_y(-angle/self.reaction)

    def rotate_z_axis_wheel(self, angle):
        matrix = [
            [math.cos(math.radians(angle)), math.sin(math.radians(angle))],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
        result = []
        for vertex in self.vertices["wheel_z"]:
            result.append([
                ((vertex[0] - self.vertices["wheel_z"][0][0]) * matrix[0][0] - (vertex[1] - self.vertices["wheel_z"][0][1]) * matrix[0][1]) + self.vertices["wheel_z"][0][0],
                ((vertex[0] - self.vertices["wheel_z"][0][0]) * matrix[1][0] + (vertex[1] - self.vertices["wheel_z"][0][1]) * matrix[1][1]) + self.vertices["wheel_z"][0][1],
                vertex[2]
            ])
        self.vertices["wheel_z"] = result
        self.rotate_z(-angle/self.reaction)
