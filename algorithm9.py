def pyramid(n, list):
    for _ in range(n-len(list)):
        print(" "*(2*n-1))
    for l in reversed(list):
        m = str(l)*(2*l-1)
        m.center((2*n-1), " ")

stack = [[3,2,1],[],[]]
n = 3

A = stack[0]
B = stack[1]
C = stack[2]

if A != []:
    pyramid(n, A)
else:
    print(" "*(2*n-1)*n)

if B != []:
    pyramid(n, B)
else:
    print(" "*(2*n-1)*n)
if C != []:
    pyramid(n, C)
else:
    print(" "*(2*n-1)*n)