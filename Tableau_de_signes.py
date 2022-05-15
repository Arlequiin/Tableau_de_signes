import pandas as pd
import numpy as np
from pyparsing import line
from sympy import *
import re

x, y = symbols('x y')
a = input("Input first term (a in a/b) \n>>> ")
b = input("Input the second term (b in a/b) \n>>> ")
l = ['*','+','-','/']
try:
    result = re.search("(.*)x",a)
    resultat = result.group(1)[-1]
    foratest = int(resultat)
    a = a.replace(resultat+'x',resultat+"*"+'x')
except:
    pass
try:
    result = re.search("(.*)x",b)
    resultat = result.group(1)[-1]
    foratest = int(resultat)
    b = b.replace(resultat+'x',resultat+"*"+'x')
except:
    pass
first_term = eval(a)
second_term = eval(b)
first_soluce = solve(first_term,x)
second_soluce = solve(second_term,x)
line1 = ['-inf']
soluces = [*first_soluce,*second_soluce]
soluces.sort()
for i in range(len(soluces)):
    line1.append(soluces[i])
line1.append('+inf')
line2 = []
line3 = []
while len(line2) != len(line1):
    line2.append("")
    line3.append("")
lfs = line1.index(first_soluce[0])
print(f"Par convention, il est impossible de diviser par zéro, ainsi\n{b} est différent de 0 donc,\nx != {str(second_soluce).replace(',',';')}")
lss = line1.index(second_soluce[0])
line2[lfs] = 0
line3[lss] = 0
result = re.search("-(.*)x",a)
try:
    var = (result.group(1)+'x')
    fstx_sign = '-'
except:
    fstx_sign = '+'
result = re.search("-(.*)x",b)
try:
    var = (result.group(1)+'x')
    sndx_sign = '-'
except:
    sndx_sign = '+'
for i in range(len(line1)):
    try:
        if str(eval(a.replace('x',str(line1[i])))) == '0':
         line2[i] = str(eval(a.replace('x',str(line1[i]))))
    except:
        pass
for i in range(len(line1)):
    try:
        if str(eval(b.replace('x',str(line1[i])))) == '0':
         line3[i] = str(eval(b.replace('x',str(line1[i]))))
    except:
        pass
for i in range(len(line2)):
    if i < lfs and fstx_sign != '-':
        line2[i] = '-'
    if i > lfs and fstx_sign != '-':
        line2[i] = '+'
    elif fstx_sign == '-':
        if i < lfs:
            line2[i] = '+'
        if i > lfs:
            line2[i] = '-'
for i in range(len(line3)):
    if i < lss and sndx_sign != '-':
        line3[i] = '-'
    if i > lss and sndx_sign != '-':
        line3[i] = '+'
    elif sndx_sign == '-':
        if i < lss:
            line3[i] = '+'
        if i > lss:
            line3[i] = '-'
line4 = []
for i in range(len(line3)):
    line4.append('')
for i in range(len(line3)):
    string_to_evaluate = (line2[i]+line3[i]+'1')
    to_compare = (eval(string_to_evaluate.replace('0','')))
    if to_compare > 0:
     line4[i] = '+'
    else:
     line4[i] = '-'
tableau = (np.array([line1,line2,line3]))
#print(tableau)
line2[-1]=''
line3[-1]=''
line4[-1]=''
data = {x:  line1,
        first_term: line2,
        second_term:line3,
        'A(x)':line4,
        }

df = pd.DataFrame(data)

print(df.transpose())
print(f"\nS = {solve(first_term/second_term,x)}")