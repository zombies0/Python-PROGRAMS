import matplotlib.pyplot as plt

def root_s(x1, x2, t,xx,yy):

    tol_diff = 10.0

    f1 = f(x1)
    f2 = f(x2)
    mm = 0.0
    m = 0.0
    cm = 0.0
    xx1 = []
    yy1 = []
    xx2 = []
    yy2 = []
    c1 = x1
    c2 = x2
    i = 0

    if f(x1) == 0.0:

        xx1.append(float(x1))
        yy1.append(float(f(x1)))
        xx2.append(float(x2))
        yy2.append(float(f(x2)))
        print ('''
Value is found
x = ''', x1)
        graph_print(xx, yy, x1)
        return x1
    elif f(x2) == 0.0:

        xx1.append(float(x1))
        yy1.append(float(f(x1)))
        xx2.append(float(x2))
        yy2.append(float(f(x2)))
        print ('''
Value is found
x = ''', x2)
        graph_print(xx, yy, x2)
        return x2

    if f(x1) * f(x2) < 0:

        while tol_diff > t:
            mm2 = mm

            xx1.append(float(x1))
            yy1.append(float(f(x1)))
            xx2.append(float(x2))
            yy2.append(float(f(x2)))

            m = (x1 + x2) / 2.00
            mm = f(m)
            tol_diff = relative_diff(mm, mm2)

            if mm == 0.0:

                print ('x = ', m)
                graph_print(xx, yy, m)
                return m
            elif f(x1) * mm < 0:

                x2 = m
            else:
                x1 = m
    elif f1 * f2 > 0:

        while tol_diff > t:

            mm2 = mm

            xx2.append(float(x2))
            yy2.append(float(f(x2)))

            m = (x1 + x2) / 2.00
            mm = f(m)

            tol_diff = relative_diff(mm, mm2)

            if mm == 0.0:

                print ('x = ', m)
                graph_print(xx, yy, m)

                return m
            elif f(x1) * mm < 0:

                x2 = m
            else:

                x1 = m
            xx1.append(float(x1))
            yy1.append(float(f(x1)))

            i = i + 1
            print("\n i = ",i)
            print(" x1 = ",x1," x2 = ",x2 , " MID = ",m)
           
        i = 0
        tol_diff = 10
        print("\n\n")
        while tol_diff > t:

            mm2 = mm

            xx2.append(float(c2))
            yy2.append(float(f(c2)))

            cm = (c1 + c2) / 2.00
            mm = f(cm)

            tol_diff = relative_diff(mm, mm2)

            if mm == 0.0:

                print ('x = ', m)
                graph_print(xx, yy, cm)

                return cm
            elif f1 * mm < 0:

                c1 = cm
            else:

                c2 = cm

            xx1.append(float(c1))
            yy1.append(float(f(c1)))
            i = i + 1
            print("\n i = ",i)
            print("\n x1 = ",c1," x2 = ",c2 , " MID = ",cm)

        print ('''Tolerance limit reached x = ''', m)
        graph_printf(
            xx,
            yy,
            m,
            cm,
            )
        return
    else:

        print ('''Enter the right value b/w postive and negative''')
        return 0

    print ('''Tolerance limit reached x = ''', m)
    graph_print(xx, yy, m)

    return m

def f(x):

    #k = pow(x,3) + pow(x,2) + 2*x -30
    k = pow(x, 2) + 2.00 * x - 15.0
    return k

def relative_diff(a, b):

    a = abs(a)
    b = abs(b)

    return abs(a - b)

def graph_printf(
    xx1,
    yy1,
    m,
    cm
    ):

    y = f(m)
    cy = f(cm)

    plt.plot(xx1, yy1)
    plt.scatter(m, y)
    plt.scatter(cm, cy)

    plt.plot(m, y, '-o')
    plt.plot(cm, cy, '-o')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('f(x) = x^2 + 2 * x - 15')
    plt.annotate('  < - - y', (m, y))
    plt.annotate('  < - - y', (cm, cy))

    ax = plt.gca()
    ax.set_facecolor('xkcd:light green')

    plt.grid()
    plt.show()

def graph_print(
    xx1,
    yy1,
    m
    ):

    y = f(m)
    
    plt.plot(xx1, yy1)
    plt.scatter(m, y)
    
    plt.plot(m, y, '-o')
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('f(x) = x^2 + 2 * x - 15')
    plt.annotate('  < - - y', (m, y))
    

    ax = plt.gca()
    ax.set_facecolor('xkcd:light green')

    plt.grid()
    plt.show()

x1 = float(input("\nEnter x1\n"))

x2 = float(input("\nEnter x2\n"))

t = float(input("\nEnter tolerance\n"))

j1 = int(x1)
j2 = int(x2)

xx = []
yy = []
g = 0
s = 0
i  = 0
if j1<j2:
    g = j2
    s = j1
else:
    g = j1
    s = j2
b = 0.0
while s<=g:
    xx.append(float(s))
    yy.append(float(f(s)))
    xx.append(float(s + 0.5))
    yy.append(float(f(s + 0.5)))
    s = s + 1

root_s(x1, x2, t,xx,yy)