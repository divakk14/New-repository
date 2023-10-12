# from circle import Circle
# class Circle(Shape):
class Shape:    
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f'Circle at ({self.x}, {self.y}) with radius {self.size}'


class Base(Shape):
    pass

class Circle(Base):
    pass

def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())

if __name__ == '__main__':
    main()