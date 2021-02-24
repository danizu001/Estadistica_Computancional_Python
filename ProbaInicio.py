import random
def media(X):
    return(sum(X)/len(X))

def varianza(X):
    cont=0
    mu=media(X)
    for i in X:
        cont+=(i-mu)**2
    return (cont/len(X))

def desv_est(X):
    return (varianza(X))**(1/2)
    
if __name__ =='__main__':
    X=[random.randint(1,20) for i in range(20)]
    mu = media(X)
    Var=varianza(X)
    sigma=desv_est(X)
    print(f'Arreglo X:{X}')
    print(f'Media X:{mu}')
    print(f'Varianza X:{Var}')
    print(f'Desviacion estandar: X:{sigma}')    