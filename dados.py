import random
def tirar_dado(num_veces):
    tiros1=[]
    tiros2=[]
    tiros=[]
    for i in range(num_veces):
        tiros1.append(random.randint(1, 6))
        tiros2.append(random.randint(1, 6))
    for x,y in zip(tiros1,tiros2):
        tiros.append(x+y)
    return tiros
def main(num_veces,num_inten):
    tiros=[]
    for i in range(num_inten):
        secuencia=tirar_dado(num_veces)
        tiros.append(secuencia)
        tiros_1=0
    for i in tiros:
        if 10 in i:
            cont=10
            tiros_1+=1
    probabilidad=tiros_1/num_inten
    return probabilidad
            
        
if __name__=='__main__':
    num_veces=int(input("Cuantos tiros del dado haras?"))
    num_inten=int(input("Cuantas veces correra la simulacion?"))
    print(main(num_veces,num_inten))