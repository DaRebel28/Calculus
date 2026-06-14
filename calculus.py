# John Burghardt
from fractions import Fraction
import os
import copy
userInput = None
while True :
    os.system('clear')
    print("Calculus Calculator")
    if userInput == None or userInput == "" :
        userInput = input("Enter f(x): ")
    fx = userInput
    fx = fx.replace(' ', "")
    fx = fx.replace('-', "+-")
    fx = fx.replace("x+", "x^1+")
    fx = fx.replace("+x", "+1x")
    fx = fx.replace("-x", "-1x")
    try :
        if fx.rfind('x') < fx.rfind('+') :
            fx += "x^0"
        if 'x' not in fx :
            fx += "x^0"
        if '^' not in fx and 'x' in fx :
            fx += "^1"
        if fx[len(fx) - 1] == 'x' :
            fx += "^1"
        if fx[0] == 'x' :
            fx = "+1" + fx
        if fx[0] != '+' :
            fx = '+' + fx
        if '+' in fx[fx.find('+') + 1:] :
            fn = int(fx[fx.find('^') + 1 : fx[fx.find('+') + 1:].find('+') + 1])
        else :
            fn = int(fx[fx.find('^') + 1 :])
        fa = [0] * (fn + 1)
        for i in range(fn, -1, -1) :
            if ('^' + str(i)) not in fx :
                continue
            else :
                fa[i] = int(fx[fx.find('+') + 1 : fx.find('x^' + str(i))])
                fx = fx[fx.find('^' + str(i)):]
    except :
        fx = None
        continue
    break
os.system('clear')
print("Calculus Calculator")
fx = ""
for i in range(len(fa) - 1, -1, -1) :
    if fa[i] == 0 and len(fa) > 1 :
        continue
    if fa[i] > 0 and i != len(fa) - 1 :
        fx += '+'
    if abs(fa[i]) != 1 and i > 0 :
        fx += str(fa[i]) + "x"
    elif abs(fa[i]) == 1 and i > 0 :
        fx += 'x'
    elif i == 0 :
        fx += str(fa[i])
    if i > 1 :
        fx += '^' + str(i)
print("f(x) = " + fx)
fpa = copy.deepcopy(fa)
fpa[0] = 0
for i in range(1, len(fpa)) :
	fpa[i] *= i
	fpa[i - 1] = fpa[i]
fpa[len(fpa) - 1] = 0
fpx = ""
for i in range(len(fpa) - 1, -1, -1) :
    if fpa[i] == 0 and len(fpa) > 1 :
        continue
    if fpa[i] > 0 and i != len(fpa) - 2 :
        fpx += '+'
    if abs(fpa[i]) != 1 and i > 0 :
        fpx += str(fpa[i]) + "x"
    elif abs(fpa[i]) == 1 and i > 0 :
        fpx += 'x'
    elif i == 0 :
        fpx += str(fpa[i])
    if i > 1 :
        fpx += '^' + str(i)
print("(d/dx)f(x) = " + fpx)
Fa = [0] * (len(fa) + 1)
Fa[0] = 'c'
for i in range(len(fa)) :
    Fa[i + 1] = Fraction(fa[i],(i + 1))
Fx = ""
for i in range(len(Fa) - 1, -1, -1) :
    if Fa[i] == 0 :
        continue
    if Fa[i] == 'c' :
        if len(Fx) > 0 :
            Fx += '+'
        Fx += 'c'
    else :
        if len(Fx) > 0 :
            Fx += '+'
        if Fa[i] != 1 or i == 0 :
            if Fa[i].denominator == 1 :
                Fx += str(Fa[i])
            else :
                Fx += '(' + str(Fa[i]) + ')'
        if i > 0 :
            Fx += 'x'
        if i > 1 :
            Fx += '^'
            Fx += str(i)
print("∫f(x)dx = " + Fx)