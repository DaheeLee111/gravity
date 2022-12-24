import numpy as np
import pygame

from OpenGL.GL import *
from OpenGL.GLU import *


class Squre:
    def __init__(self, location, x, y, z):
        self.color = (255, 255, 255)

        self.center = location
        self.x = x
        self.y = y
        self.z = z

        self.vertices = (
            (location[0]-x/2, location[1]-y/2, location[2]-z/2),
            (location[0]+x/2, location[1]-y/2, location[2]-z/2),
            (location[0]+x/2, location[1]+y/2, location[2]-z/2),
            (location[0]-x/2, location[1]+y/2, location[2]-z/2),
            (location[0]-x/2, location[1]-y/2, location[2]+z/2),
            (location[0]+x/2, location[1]-y/2, location[2]+z/2),
            (location[0]+x/2, location[1]+y/2, location[2]+z/2),
            (location[0]-x/2, location[1]+y/2, location[2]+z/2),
        )

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

        # 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False

        glRotatef(1, 1, 1, 1)

        # 그리기
        object.draw()


main()
