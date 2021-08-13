from ursina import Entity, Shader
import scipy.constants


class Object(Entity):
    def __init__(self, model, color, mass, position, shader):
        Entity.__init__(self, model=model, color=color, scale=mass, position=position, shader=shader)
        self.mass = mass

    def accel_update(self):
        G = scipy.constants.gravitational_constant
