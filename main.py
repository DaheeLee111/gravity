import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

import math


class Squre:
    def __init__(self, location, x, y, z):
        self.color = (255, 255, 255)

        self.center = location
        self.x = x
        self.y = y
        self.z = z

        self.vertices = [
            [location[0]-x/2, location[1]-y/2, location[2]-z/2],
            [location[0]+x/2, location[1]-y/2, location[2]-z/2],
            [location[0]+x/2, location[1]+y/2, location[2]-z/2],
            [location[0]-x/2, location[1]+y/2, location[2]-z/2],
            [location[0]-x/2, location[1]-y/2, location[2]+z/2],
            [location[0]+x/2, location[1]-y/2, location[2]+z/2],
            [location[0]+x/2, location[1]+y/2, location[2]+z/2],
            [location[0]-x/2, location[1]+y/2, location[2]+z/2]
        ]

        self.vertices = [
            [0, 0, 0],
            [x, 0, 0],
            [x, y, 0],
            [0, y, 0],
            [0, 0, z],
            [x, 0, z],
            [x, y, z],
            [0, y, z],
        ]

        self.edges = (
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7),
        )

    def begin_and_end(func):
        def wrapper(self):
            glBegin(GL_LINES)
            func(self)
            glEnd()

        return wrapper

    @begin_and_end
    def draw(self):
        for vertice in self.edges:
            glVertex3fv(self.vertices[vertice[0]])
            glVertex3fv(self.vertices[vertice[1]])

    def move_to_x(self, distance):
        result = []
        for vertex in self.vertices:
            result.append([vertex[0] + distance, vertex[1], vertex[2]])
        self.vertices = result

    def move_to_y(self, distance):
        result = []
        for vertex in self.vertices:
            result.append([vertex[0], vertex[1] + distance, vertex[2]])
        self.vertices = result

    def rotate_to_x(self, angle):
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

    def rotate_to_y(self, angle):
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


def main():
    display = (800, 800)
    object = Squre([0, 0, 0], 1, 1, 1)

    pygame.init()
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    gluPerspective(35, (display[0]/display[1]), 0.5, 100.0)
    glTranslatef(0.0, 0.0, -7)

    running = True
    while running:

        # pygame 환경변수
        pygame.time.Clock().tick(60)
        pygame.display.flip()

        # openGl 환경변수
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)

        for event in pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]:
                object.rotate_to_x(1)
            if pygame.mouse.get_pressed()[2]:
                object.rotate_to_x(-1)

        # 이벤트
        for event in pygame.event.get():
            # 종료
            if event.type == pygame.QUIT:
                running = False
            # 방향키
            if event.type == pygame.KEYDOWN:
                if event.dict["key"] == pygame.K_RIGHT:
                    object.move_to_x(0.1)
                if event.dict["key"] == pygame.K_LEFT:
                    object.move_to_x(-0.1)
                if event.dict["key"] == pygame.K_UP:
                    object.move_to_y(0.1)
                if event.dict["key"] == pygame.K_DOWN:
                    object.move_to_y(-0.1)

        # 그리기
        object.draw()


main()
