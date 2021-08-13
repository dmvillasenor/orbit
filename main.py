from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *

from object import Object

app = Ursina()
star = Object('sphere', color.blue, 1, (0.1, 0, 0), normals_shader)
star2 = Object('sphere', color.red, 2, (5, 0, 3), basic_lighting_shader)


def main():
    EditorCamera()
    app.run()


def update():
    star.accel_update()


def input(key):
    if key == 'q':
        quit(0)


if __name__ == '__main__':
    main()
