def glb_calc(x, y):
    return 2 * x + 3 * y


class Calc(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cls_calc(self, z):
        if type(z) is not int:
            raise ValueError("### z is not int")
        return self.x + self.y + z
