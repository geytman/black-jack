class Chips:  #  player Chips
    def __init__(self):
        self.total = 100

    def add(self, num):
        self.total = self.total + num

    def remove(self, num):
        self.total = self.total - num