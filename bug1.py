class base:
    def __init__(self, x, y, size): #initialize
        self.x = x
        self.y = y
        self.size = size
class Circle(base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
    def shape(self):
        return "This is a circle"
    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """
def main():
    c = Circle(1,2,3)
    print(c.shape())
    print(c.draw())
main()