import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

from form import Squre


def main():
    display = (800, 800)
    cube = Squre([0.5, -0.25, 1], 1, 1, 1)

    pygame.init()
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluPerspective(35, (display[0]/display[1]), 0.5, 100.0)
    glTranslatef(0.0, 0.0, -7)

    running = True
    isCTRL = False
    isSHIFT = False
    isSPACE = False
    while running:

        # 그리기
        cube.drawSqure()

        # pygame 환경변수
        pygame.time.Clock().tick(60)
        pygame.display.flip()

        # openGl 환경변수
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)

        # 종료
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.dict["key"] == pygame.K_LCTRL:
                    isCTRL = True
                if event.dict["key"] == pygame.K_LSHIFT:
                    isSHIFT = True
                if event.dict["key"] == pygame.K_SPACE:
                    isSPACE = True
            if event.type == pygame.KEYUP:
                if event.dict["key"] == pygame.K_LCTRL:
                    isCTRL = False
                if event.dict["key"] == pygame.K_LSHIFT:
                    isSHIFT = False
                if event.dict["key"] == pygame.K_SPACE:
                    isSPACE = False

        # 마우스
        for event in pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0] and isCTRL == False and isSHIFT == False and isSPACE == False:
                cube.rotate_by_z(4)
            if pygame.mouse.get_pressed()[2] and isCTRL == False and isSHIFT == False and isSPACE == False:
                cube.rotate_by_z(-4)
            if pygame.mouse.get_pressed()[0] and isSHIFT == False and isSPACE == False and isCTRL:
                cube.rotate_by_x(4)
            if pygame.mouse.get_pressed()[2] and isSHIFT == False and isSPACE == False and isCTRL:
                cube.rotate_by_x(-4)
            if pygame.mouse.get_pressed()[0] and isCTRL == False and isSPACE == False and isSHIFT:
                cube.rotate_by_y(1)
            if pygame.mouse.get_pressed()[2] and isCTRL == False and isSPACE == False and isSHIFT:
                cube.rotate_by_y(-1)
            if pygame.mouse.get_pressed()[0] and isCTRL == False and isSHIFT == False and isSPACE:
                cube.move_to_x(-0.01)
            if pygame.mouse.get_pressed()[2] and isCTRL == False and isSHIFT == False and isSPACE:
                cube.move_to_x(0.01)

        # if cube.angle_x() > 0:
        #     cube.rotate_by_z(cube.angle_x())
        # if cube.angle_x() < 0:
        #     cube.rotate_by_z(cube.angle_x())

        # if cube.angle_z() > 0:
        #     cube.rotate_by_x(cube.angle_z())
        # if cube.angle_z() < 0:
        #     cube.rotate_by_x(cube.angle_z())


if __name__ == '__main__':
    main()
