class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**0.5
        return diagonal

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            for i in range(self.height):
                picture += self.width * '*' + '\n'
            return picture
    
    def get_amount_inside(self, shape):
        width_counter = self.width // shape.width
        height_counter = self.height // shape.height
        return width_counter * height_counter

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side

    def __str__(self):
        return f'{self.__class__.__name__}(side={self.side})'

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

    def get_picture(self):
        picture = ''
        if self.side > 50:
            return 'Too big for picture.'
        else:
            for i in range(self.side):
                picture += self.side * '*' + '\n'
            return picture
