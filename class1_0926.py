class Calculator:
    def __init__(self, name,price,hight,width,weight):
        self.name = name
        self.price = price
        self.h = hight
        self.w = width
        self.we = weight

        
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def mimus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        result = x * y
        print(result)
    def divide(self,x,y):
        result = x / y
        print(result)
