class Myclass:
    def getString(self):
        self.str = (str(input())).upper()
    def printString(self):
        print(self.str)
q = Myclass()
q.getString()
q.printString()


class Square:
    def __init__(self, len):
        self.len = len 
    
    def area(self):
        print(pow(self.len, 2))

class Shape(Square):
    def __init__(self, len = 0):
        Square.len = len 

p1 = Shape(5)
p1.area()




class Rectangle:
    def __init__(self, a, b):
        self.S = self.a * self.b
    
    def area(self):
        print(self.a * self.b)

class Shape(Rectangle):
    def __init__(self, a = 0, b = 0):
        Rectangle.a = a 
        Rectangle.b = b


p1 = Shape(5, 6)

p1.area()



class Point:
    def __init__(self, x_coord = 0, y_coord = 0):
        self.x = x_coord
        self.y = y_coord

    def show(self):
        print("X:", self.x," ",  "Y:", self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist_between_2(self, x1, y1, x2, y2):
        self.dist_between_2 = pow(pow(x1-x2, 2)+pow(y1-y2, 2), 0.5)

    def show_dist_between_2(self):
        print(self.dist_between_2)

    def dist(self, x, y):
        self.dist = pow(pow(x-self.x, 2) + pow(y-self.y, 2), 0.5)
        
    def show_dist(self):
        print(self.dist)



class Account:
    def __init__(p1, Name: str, Surname: str, Balance: int):
        p1.name_surname = Name + "_" +Surname
        p1.balance = Balance
    def deposit(self, money: int):
        self.balance += money 
    def balance_check(self):
        print("Balance:", self.balance, "tenge")
    def withdraw(self, How_much: int):
        if self.balance - How_much <= 0:
            print("No money in the deposit")
        else:
            self.balance -= How_much

user1 = Account("Aru", "Sat", 5000)
user1.deposit(10000)
user1.balance_check()
user1.withdraw(2000)
user1.balance_check()
user1.withdraw(100000)



class Myclass:
    def prime(self, num):
        if num == 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    def prime_1(self):
        self.x = lambda a : self.prime(a)
        list_1 = list(map(int, input().split()))
        list_1 = list(filter(self.x, list_1))
        print(list_1)

p1 = Myclass()
p1.prime_1()




