#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


def root_s(x1, x2, t):

    tol_diff = 10.0
    tol_difff = 10.0

    f1 = f(x1)
    f2 = f(x2)
    mm = 0.0
    m = 0.0
    mm2 = 0.0
    xx1 = []
    yy1 = []
    xx2 = []
    yy2 = []
    c1 = x1
    c2 = x2

    if f1 == 0.0:

        xx1.append(float(x1))
        yy1.append(float(f(x1)))
        xx2.append(float(x2))
        yy2.append(float(f(x2)))
        print ('''Value is foundx = ''', x1)
        graph_print(xx1, yy1, xx2, yy2, x1)
        return x1
    elif f2 == 0.0:

        xx1.append(float(x1))
        yy1.append(float(f(x1)))
        xx2.append(float(x2))
        yy2.append(float(f(x2)))
        print ('''Value is foundx = ''', x2)
        graph_print(xx1, yy1, xx2, yy2, x2)
        return x2

    if f1 * f2 < 0:

        xx1.append(float(x1))
        yy1.append(float(f(x1)))
        xx2.append(float(x2))
        yy2.append(float(f(x2)))

        m = (x1 + x2) / 2.00
        mm = f(m)
        tol_diff = relative_diff(mm, mm2)

        if mm == 0.0:

            print ('x = ', m)
            graph_printf(xx1, yy1, xx2, yy2, m)

            return m
        elif f1 * mm < 0:

            x2 = m
        else:

            x1 = m
    elif f1 * f2 > 0:

        while tol_diff > t:

            mm2 = mm

            xx1.append(float(x1))
            yy1.append(float(f(x1)))

            m = (x1 + x2) / 2.00
            mm = f(m)

            tol_diff = relative_diff(mm, mm2)

            if mm == 0.0:

                print ('x = ', m)
                graph_printf(xx1, yy1, xx2, yy2, m)

                return m
            elif f1 * mm < 0:

                x2 = m
            else:

                x1 = m

        while tol_difff > t:

            mm2 = mm
            xx2.append(float(x2))
            yy2.append(float(f(x2)))

            m = (x1 + x2) / 2.00
            mm = f(m)

            tol_diff = relative_diff(mm, mm2)

            if mm == 0.0:

                print ('x = ', m)
                graph_printf(xx1, yy1, xx2, yy2, m)

                return m
            elif f2 * mm < 0:

                x1 = m
            else:

                x2 = m
    else:

        print ("Enter the right value b/w postive and negative")

        return 0

    tol_diff = 0.0

    print ("Tolerance limit reachedx = ", m)
    graph_printf(xx1, yy1, xx2, yy2, m)

    return m


def f(x):

    k = pow(x, 2) + 2.00 * x - 15.0
    return k


def relative_diff(a, b):

    a = abs(a)
    b = abs(b)

    return abs(a - b)


def graph_print(
    xx1,
    yy1,
    xx2,
    yy2,
    m,
    ):

    y = f(m)

    xf1 = xx1 + xx2
    xf2 = yy1 + yy2

    plt.plot(xf1, xf2)
    plt.scatter(m, y)

    plt.plot(m, y, '-o')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('f(x) = x^2 + 2 * x - 15')
    plt.annotate('  < - - y', (m, y))

    ax = plt.gca()
    ax.set_facecolor('xkcd:mint green')

    plt.grid()
    plt.show()


def graph_printf(
    xx1,
    yy1,
    xx2,
    yy2,
    m,
    ):

    y = f(m)

    plt.plot(xx1, yy1)
    plt.plot(xx2, yy2)
    plt.scatter(m, y)

    plt.plot(m, y, '-o')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('f(x) = x^2 + 2 * x - 15')
    plt.annotate('  < - - y', (m, y))

    ax = plt.gca()
    ax.set_facecolor('xkcd:mint green')

    plt.grid()
    plt.show()

x1 = float(input("\nEnter the value of x1\n"))

x2 = float(input("\nEnter the value of x2\n"))

t = float(input("\nEnter the tolerance value\n"))

root_s(x1,x2,t)