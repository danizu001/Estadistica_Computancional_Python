import random
class Borracho:
    def __init__(self, name):
        self.name=name
class BorrachoTradicional(Borracho):
    def __init__(self,name):
        super().__init__(name)
    def moverse(self):
        pasos = [(1,0),(0,1),(-1,0),(0,-1)]
        x=random.randint(0, 3)
        return pasos[x]
    def moverse_profe(self):
        return random.choice([(1,0),(0,1),(-1,0),(0,-1)])
class BorrachoIzq(Borracho):
    def __init__(self,name):
        super().__init__(name)
    def moverse_profe(self):
        return random.choice([(3,0),(0,1),(-1,0),(0,-1)])