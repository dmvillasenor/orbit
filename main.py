from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *

from object import Object

app = Ursina()
star = Object('sphere', color.blue, 1000000000000000, (10, 10, 10), (0, 0, 0), normals_shader, 0)
star2 = Object('sphere', color.red, 1, (10, 10, 10), (50, 0, 0), basic_lighting_shader, (0, 20, 20))


def main():
    EditorCamera()
    app.run()


def update():
    star2.update_position(time.dt)
    (radius, rel_pos) = star2.calc_radius((star.x, star.y, star.z))
    accel_vector = star2.calc_accel(radius, star.mass, rel_pos)
    star2.accel_velocity(accel_vector, time.dt)

    cube = Object('cube', color.blue, 1, (0.5, 0.5, 0.5), (star2.x, star2.y, star2.z), basic_lighting_shader, 0)


def input(key):
    if key == 'q':
        quit(0)


if __name__ == '__main__':
    main()
