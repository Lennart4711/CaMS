from buidling import Buidling
from mineral import Mineral

class Mine(Building):
    def __init__(self, pos):
        self.MINING_SPEED = 2000
        
        super(pos)
        self.minerals = []
        self.counter = 0

    def update(self):
        self.counter += 1
        if(self.counter == self.MINING_SPEED):
            self.minerals.append(Mineral(1))
            self.counter = 0
            print(f"This mine produced {self.minerals} minerals!")

    def transfer_minerals(self, receiver):
        receiver.append(self.mineral[-1])
        

