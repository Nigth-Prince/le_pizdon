al = 400
cr = 250
be = 350
iz = 100
class Biz():
    def __init__(self):
        self.al = al
        self.cr = cr
        self.be = be
        self.iz = iz
        self.send = 0
    def search(self):
        b = Biz()
        res =self.al > 0 and self.cr > 0 and self.be > 0 and self.iz > 0
        while res:
            b.a()

        print ()


    def a(self):
        # price = 120
        self.al -= 2
        self.cr -= 3
        self.be -= 5
        self.iz -= 2
        print (self.al)
        # self.send += price
    def b(self):
        # price = 100
        self.al -= 3
        self.cr -= 3
        self.be -= 5
        self.iz -= 2
        # self.send += price
    def c(self):
        # price = 150
        self.al -= 2
        self.cr -= 2
        self.be -= 1
        self.iz -= 3
        # self.send += price
b = Biz()
b.search()
