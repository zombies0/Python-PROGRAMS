import matplotlib.pyplot as plt

def root_s(x1 ,x2, t):

    tol_diff = 10.0

    f1 = f(x1);f2 = f(x2)
    mm = 0.0;m = 0.0
    xx1 = [];yy1 = []
     
    if f1 == 0.0:
            
        print("\nValue is found\nx = ",x1)
        graph_print(xx1,yy1,x1)
        return x1
                  
    elif f2 == 0.0 :
    
        print("\nValue is found\nx = ",x2)
        graph_print(xx1,yy1,x2)
        return x2

    if (f1*f2) <= 0:

        while tol_diff > t:  

            mm2 = mm
            m = (x1 + x2) / 2.00
            mm = f(m)
            xx1.append(float(m))
            yy1.append(float(mm))
             
            tol_diff = relative_diff(mm,mm2)

            if mm == 0.0:

                print("x = ", m)
                graph_print(xx1,yy1,m)

                return m
            
            elif (f1*mm) < 0: x2 = m               

            else: x1 = m                           

    else:

        print("\nEnter the right value b/w postive and negative\n")
        return 0
    
    print("\nTolerance limit reached\n x = ",m) 
    graph_print(xx1,yy1,m)

    return m

def f( x):

    k = pow(x,2)+ (2.0 * x )-15.0
    return k

def relative_diff(a, b):

    a = abs(a)
    b = abs(b)

    return abs(a-b)

def graph_print(xx1, yy1, m):

    y = f(m)
    
    plt.plot(xx1, yy1) 
    plt.scatter(m, y) 

    plt.plot(m, y, "-o")
  
    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 

    plt.title('f(x) = x^2 + 2 * x - 15') 
    plt.annotate("  < - - y", (m, y))

    ax = plt.gca()
    ax.set_facecolor('xkcd:mint green')
    
    plt.grid()
    plt.show() 

x1 = float(input("\nEnter the value of x1\n"))

x2 = float(input("\nEnter the value of x2\n"))

t = float(input("\nEnter the tolerance value\n"))

root_s(x1,x2,t)