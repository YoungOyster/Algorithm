top = None
current = None

def nth_point(p, n):
    for _ in range(n):
        p = p[1]
    return p


def T(top, values):
    top = [values[0], top]
    print(top)

def B():
    print("b")

def A():
    print("b")

def C(top, value):
    print(nth_point(top, 1))

def P(top):
    print(nth_point(top, ))

def F():
    print("f")

def D():
    print("d")

def S():
    print("s")


Commands = {"t": T, "b": B, "a": A, "c": C, "p": P, "f": F, "d": D, "s": S}

while True:
    command, *values = input(">").split()
    
    Commands(command)

    if command == "q":
        print("終了します。")
        break