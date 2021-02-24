import random
import collections
PALOS=['espada','corazon','rombo','trebol']
VALORES=['AS','2','3','4','5','6','7','8','9','10','j','q','k']

def CrearBaraja(PALOS,VALORES):
    barajas=[]
    for i in PALOS:
        for j in VALORES:
            barajas.append((i,j))
    return barajas

def ObtenerMano(barajas,tam_man):
    mano=[]
    x=len(barajas)
    pos_cartas=[random.randint(1,x) for i in range(tam_man)]
    for i in pos_cartas:
        mano.append((barajas[i]))
        barajas.pop(i)
    return (mano,barajas)

def ObtenerManoProfe(barajas, tam_man):
    mano=random.sample(barajas,tam_man)
    return mano

def ProbabilidadPar(manos):
    pares=0
    for i in manos:
        valores=[]
        for j in i:
            valores.append(j[1])
        counter=dict(collections.Counter(valores))
        for i in counter.values():
            if i==2:
                pares+=1
                break
    return pares 
def ordenar(manos,orden):
    osort=[]    
    for i in orden:
        for j in manos:
            if i==j[1]:
                osort.append(j[1])
    return osort
        
def ProbCorridas(tam_man,manos):
    contCorr=0
    orden=['AS','2','3','4','5','6','7','8','9','10','j','q','k']
    for i in manos:
        osort=ordenar(i, orden)
        ver=0
        con=0
        for j in range(len(orden)):
            if (orden[j]==osort[0] and 0<j<len(orden)-tam_man):
                lim=j+tam_man
                for k in range(j,lim):
                    if orden[k]==osort[con]:
                        ver+=1
                    con+=1
            if ver==5:
                contCorr+=1
    return contCorr
            
def main(tam_man,intentos):
    barajas=CrearBaraja(PALOS, VALORES)
    manos=[]
    for i in range(intentos):
        mano=ObtenerManoProfe(barajas, tam_man)
        manos.append(mano)
    pares=ProbabilidadPar(manos)
    corridas=ProbCorridas(tam_man,manos)
    print(f'veces que salieron pares: {pares}')
    print(f'veces que salieron corridas: {corridas}')
    prob_par=pares/intentos
    print(f'probabilidad de salir par: {prob_par}')
    prob_corr=corridas/intentos
    print(f'probabilidad de salir corrida: {prob_corr}')
    
        
        
if __name__=='__main__':
    en_juego=[]
    tam_man=int(input("De qué tamaño es la mano"))
    intentos=int(input("Cuantos intentos para calcular una probabilidad?"))
    main(tam_man,intentos)