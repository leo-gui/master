class People(object):
    def show_power(self):
        print("i can walk")


class Singer(People):
    def show_power(self):
        super(Singer, self).show_power()
        print("i can sing")


class Actor(People):
    def show_power(self):
        super(Actor, self).show_power()
        print("i can play")


class Human(Singer, Actor):
    pass


if __name__ == "__main__":
    a = Human()
    a.show_power()
