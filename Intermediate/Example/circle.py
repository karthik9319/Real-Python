class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("radius must be positive")
        
    
    @property
    def area(self):
        return self.pi() * self.radius**2
    
    
    def cylinder_volume(self, height):
        return self.area * height
    
    
    @classmethod
    def unit_circle(cls):
        return cls(1)
    
    
    @staticmethod
    def pi():
        return 3.1415926535
    
c = Circle(5)
print(c.radius)
print(c.area)
print(c.cylinder_volume(height = 5))
print(c.pi())