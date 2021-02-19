class Campo:
    def __init__(self):
        self.coordenadas_de_borracho = {}
    def anadir_borrachos(self,borracho,coordenada):
        self.coordenadas_de_borracho[borracho] = coordenada
    def mover_borracho(self,borracho):
        delta_x, delta_y = borracho.moverse_profe()
        coordenada_actual = self.coordenadas_de_borracho[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        
        self.coordenadas_de_borracho[borracho] = nueva_coordenada
        
    def obtener_coordenada(self,borracho):
        return self.coordenadas_de_borracho[borracho]
    