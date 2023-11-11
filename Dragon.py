# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.

# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту

# Экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:
# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;

# Из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая часть от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;

# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;

# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет

# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».

# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)
import math

class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color

    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}"
    
    def __repr__(self):
        return f"{self}({self.height}, {self.danger}, {self.color})"

    def __add__(self, other):
        if type(other) == Dragon:
            newcolor = min(self.color, other.color)
            newheight = math.floor((self.height + other.height)/2)
            newdanger = max(self.danger, other.danger)

            return f"New Dragon with height {newheight}, danger {newdanger}, color {newcolor} "
    
    def __sub__(self, other):
        if type(other) == int:
            subheight = self.height - (math.trunc(self.height / other))
            subdanger = self.danger + (self.danger % other)
            return f"After substraction Dragon with height {subheight}, danger {subdanger}, color {self.color}"
            
    def __call__(self, string):
        return f"{string * self.danger}"
         
    def change_color(self, color):
        self.color = color
        return self

                

dr = Dragon(69, 8, "brown")
dr1 = Dragon(78, 5, "gray")

print(dr)
print(dr1)
print(dr + dr1)
print(dr1-5)
print(dr1("whoah "))
print(dr.change_color("yellow"))
