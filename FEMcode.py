import numpy as np
import matplotlib.pyplot as plt
import sys

f = lambda x: -1000*np.sin(np.pi*x)


x = np.array([-1,1])/np.sqrt(3)
def integrate(f,a,b):
    return sum((b-a)/2 * f((b-a)/2*xi +(b+a)/2) for xi in x)


def nodes(a,b,n):
    return np.linspace(a,b,n)

def base(x1,x2):
    phil = lambda x: (x2-x)/(x2-x1)
    phir = lambda x: (x-x1)/(x2-x1)
    philprim = lambda x: (-1)/(x2-x1)
    phirprim = lambda x: (1)/(x2-x1)
    return [phil,phir,philprim,phirprim]


def E(x):
    if 0<=x<=1:
        return 2
    return 6

def L(v,vprim,a,b):
    return integrate(lambda x: f(x)*v(x),a,b)


def B(vprim, wprim, a, b):
    return integrate(lambda x: E(x) * vprim(x) * wprim(x), a, b)


def sol(n):
    Nodes = nodes(0,2,n+1)
    A = np.zeros((n+1, n+1))
    b = np.zeros(n+1)
    for i,(x1,x2) in enumerate(zip(Nodes,Nodes[1:])):
        j=i+1
        phil,phir,philprim,phirprim = base(x1,x2)
        A[i, i] += B(philprim, philprim, x1, x2)
        A[i, j] += B(philprim, phirprim, x1, x2)
        A[j, i] += B(phirprim, philprim, x1, x2)
        A[j, j] += B(phirprim, phirprim, x1, x2)

        b[i] += L(phil,philprim,x1,x2)
        b[j] += L(phir,phirprim,x1,x2)
    A[0,0] -= 4
    b[0] -=8

    A[n, :] = 0
    A[n, n] = 1
    b[n] = 0
    ws = np.linalg.solve(A,b)

    return Nodes, ws+3

def main():
    n=100

    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except:
            print("VALUE ERROR")
    
    xs , ys = sol(n)
    print(f"____________")
    print(f"  x |u(x)")
    for x,y in zip(xs,ys):
        print(f"{x:.2f}|{y:.2f}")
    plt.plot(xs,ys)
    plt.show()
if __name__ == "__main__":
    main()