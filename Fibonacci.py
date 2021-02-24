def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
def fibonacci_dinamico(n,var={}):
    if n==0 or n==1:
        return 1
    try:
        return var[n]
    except KeyError:
        var[n]=fibonacci_dinamico(n-1,var)+fibonacci_dinamico(n-2,var)
        return var[n]
if __name__ == '__main__':
    n=int(input("Escribe un entero: ") )
    res=fibonacci_dinamico(n)
    print(res)