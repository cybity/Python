import random

class VagueList:
    def init(self, cont):
        self.cont = cont

    def getitem(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def len(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])