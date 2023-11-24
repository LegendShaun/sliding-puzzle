from random import *
from math import *

#global constant
g_patternList =[9,16]
g_steps = 0

def position(x):
    for i in range(maxcolumn):
        try:
            n = list3[i].index(x)
            m = i
        except:
            continue
    return  m,n

def newGraph():
    tempGraph =[]
    location =position(pattern)
    x=location[0]
    y=location[1]
    temp = list3[x][y]
    if key == '%s'%a:
        if  0<x+1<maxrow:
            list3[x][y]=list3[x+1][y]
            list3[x+1][y]=temp
    if key == '%s'%c:
        if  0<=x-1<=maxrow:
            list3[x][y]=list3[x-1][y]
            list3[x-1][y]=temp
    if key == '%s'%b:
        if  0<=y+1<maxcolumn:
            list3[x][y]=list3[x][y+1]
            list3[x][y+1]=temp
    if key == '%s'%d:
        if  0<=y-1<=maxcolumn:
            list3[x][y]=list3[x][y-1]
            list3[x][y-1]=temp
    for i in range(1,maxcolumn+1):
        for j in range(1,maxrow+1):
            if j % maxcolumn ==0:
                if list3[i-1][j-1] != pattern:
                    tempGraph.append('%s\t\n'%list3[i-1][j-1])
                else:
                    tempGraph.append(' \t\n')
            else:
                if list3[i-1][j-1] !=pattern:
                    tempGraph.append('%s\t'%list3[i-1][j-1])
                else:
                    tempGraph.append(' \t')
    return tempGraph

def getFinalGraph():
    finalGraph = []
    for i in range(1,maxcolumn+1):
        for j in range(1,maxrow+1):
            if j % maxcolumn ==0:
                if list3[i-1][j-1] != pattern:
                    finalGraph.append('%s\t\n'%list3[i-1][j-1])
                else:
                    finalGraph.append(' \t\n')
            else:
                if list3[i-1][j-1] !=pattern:
                    finalGraph.append('%s\t'%list3[i-1][j-1])
                else:
                    finalGraph.append(' \t')
    return finalGraph

def enterKey():
    if position(pattern)[0] ==0:
        if position(pattern)[1]==0:
            key = input('enter your move, %s-up,%s-left:' %(c,a))
        elif position(pattern)[1] ==maxcolumn-1:
            key = input('enter your move, %s-up,%s-right:' %(c,b))
        else:
            key = input('enter your move, %s-up,%s-left,%s-right:'%(c,a,b))
    elif position(pattern)[0] ==maxrow-1:
        if position(pattern)[1]==0:
            key = input('enter your move, %s-down,%s-left:'%(d,a))
        elif position(pattern)[1] ==maxcolumn-1:
            key = input('enter your move, %s-down,%s-right:'%(d,b))
        else:
            key = input('enter your move, %s-down,%s-left,%s-right:'%(d,a,b))
    else:
        if position(pattern)[1]==0:
            key = input('enter your move, %s-up,%s-down,%s-left:'%(c,d,a))
        elif position(pattern)[1] ==maxcolumn-1:
            key = input('enter your move,%s-up, %s-down,%s-right:'%(c,d,b))
        else:
            key = input('enter your move,%s-up, %s-down,%s-left,%s-right:'%(c,d,a,b))
    return key

def data():
    while True:
        try:
            n = eval(input('please enter 0 or 1 for different puzzles:'))
            if n == 0 or n== 1:
                break
        except:
            continue
    
    global pattern,maxcolumn,maxrow,final,list3  
    list3 = []
    pattern = g_patternList[n]
    maxrow = maxcolumn = int(sqrt(pattern))
    for i in range(maxrow):
        list3.append([])
        for j in range(maxcolumn):
            list3[i].append(i*maxcolumn +j+1)
    final = getFinalGraph()
    return pattern,maxrow,maxcolumn,final,list3

def initialGraph():
    for i in range(500):
            j = randint(0,3)
            global key
            key = randomMove[j]
            temp = newGraph()
            initial_graph = ''.join(temp)
    print(initial_graph)
    return temp

print('''welcome to linyuxiao\'s sliding puzzle!
In this game you can choose two types puzzle.
And you will move the tiles using any 4 letters of your own choice
For example, you can choose w,a,s,d for up,left,down and right''')

while True:
    try:
        l = a,b,c,d = input('please enter four letters you want:')
        list1=list(set(l))
        list2=[a,b,c,d]
        if list1.sort()==list2.sort():
            break
    except:
        continue

randomMove= [a,b,c,d]

while True:
    data()
    temp = initialGraph()
    while temp !=final:
        key = enterKey()
        temp = newGraph()
        temp_graph = ''.join(temp)
        print(temp_graph)
        g_steps+=1
        
    print('finished!move %s.'%g_steps)
    m = input('You can choose c for another game,or q for quit:')
    if m =='q':
        break
    
# this is  a update 



