from Coordenada import *
from Borracho import *
from CampoBorracho import *
from bokeh.plotting import figure, show
from bokeh.palettes import magma 

def graficar(x,y):
    grafica = figure(title='Camino aleatorio',x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='Distancia Media')
    show(grafica)

def caminar(pasos,campo,borracho):
    inicio = campo.obtener_coordenada(borracho)
    for i in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))
def simular_caminata(pasos,num_int,tipo_borracho):
    borracho = tipo_borracho(name="Daniel")
    origen = Coordenada(0, 0)
    distancias = []
    for i in range(num_int):
        campo=Campo()
        campo.anadir_borrachos(borracho, origen)
        simulacion_caminata=caminar(pasos,campo,borracho)
        distancias.append(simulacion_caminata)
    return distancias
        
def main(distancias_de_caminata,num_int,tipo_borracho):
    distancias_media_por_caminata=[]
    dic=[]
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos,num_int,tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}') 
    graficar(distancias_de_caminata, distancias_media_por_caminata)
    for x in distancias_media_por_caminata:
        dic.append(x)
    return dic
if __name__ == '__main__':
    distancias_de_caminata = [10,100,1000,10000]
    num_int=100
    g3=[]
    g1=main(distancias_de_caminata,num_int,BorrachoIzq)
    g2=main(distancias_de_caminata,num_int,BorrachoTradicional)
    g3.append(g1)
    g3.append(g2)
    g2=([10,100,1000,10000],[10,100,1000,10000])
    graph = figure(title = "Comparacion borrachos",x_axis_label='pasos', y_axis_label='distancia')
    graph.multi_line(g2, g3)  
    show(graph) 
    
        