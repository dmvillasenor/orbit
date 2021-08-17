from ursina import Entity, Shader
import scipy.constants
from numpy import sin, cos, arctan, sqrt, subtract, hypot


class Object(Entity):
    def __init__(self, model, color, mass, scale, position, shader, velocity):
        Entity.__init__(self, model=model, color=color, scale=scale, position=position, shader=shader)
        self.mass = mass
        self.velocity = velocity

    def calc_radius(self, parent_position):
        (temp_x, temp_y, temp_z) = tuple(subtract(self.position, parent_position))
        xy = hypot(temp_x, temp_y)
        radius = hypot(xy, temp_z)
        rel_pos = (temp_x, temp_y, temp_z)
        return radius, rel_pos

    def calc_accel(self, radius, parent_mass, rel_pos):
        temp_x, temp_y, temp_z = rel_pos
        xz_angle = arctan(temp_z / temp_x)

        xz = hypot(temp_x, temp_z)
        y_angle = arctan(temp_y / xz)

        if temp_x < 0:
            xz_angle += scipy.constants.pi

        G = scipy.constants.gravitational_constant
        Force = (G * parent_mass * self.mass) / (radius * radius)
        acceleration = Force / self.mass

        accel_y = acceleration * sin(y_angle)
        accel_xy = acceleration * cos(y_angle)
        accel_z = accel_xy * sin(xz_angle)
        accel_x = accel_xy * cos(xz_angle)

        accel_vector = (accel_x, accel_y, accel_z)
        return accel_vector

    def accel_velocity(self, accel_vector, time_pass):
        accel_vector = tuple([z * time_pass for z in accel_vector])
        self.velocity = tuple(subtract(self.velocity, accel_vector))

    def update_position(self, time):
        (x, y, z) = self.velocity
        self.x += (x * time)
        self.y += (y * time)
        self.z += (z * time)
