from __future__ import print_function
import sys
import time
import numpy as np
sys.setrecursionlimit(1500)

matches = {'H':'G', 'G':'H', 'W':'T','T':'W'}
r = []
line = []
b = []

def OPT(i,j):
    if not i < j-4:
        return 0
    
    if r[i][j] != '-':
        return int(r[i][j])

    q = -1
    for x in range(i, j-4):
        temp = max( OPT(i,x-1) + OPT(x+1, j-1) + 1, q)
        if matches[line[x]] == line[j]:
            q = max( temp, q)
    #k = q
    q = max(q, OPT(i, j-1))
    #if k < q: optimal[j-1] = [j, q]
    r[i][j] = q
    return q

def main(argv):
    global r
    global line
    global b
    n = int(argv[1])-1
    
    r = [['-' for i in range(n+1)] for i in range(n+1)]
    optimal = [[0,0] for i in range(n+1)]
    b = [0 for i in range(n+1)]
    
    filename = argv[0]
    infile = open(filename, 'r')
    
    for i in infile:
        line = list(i.strip())
    #r = np.array(r)
    line = np.array(line)
    start_time = time.time()
    opt = OPT(0,n)
    
    deltaT = time.time() - start_time
    
    print(opt)
    print(str(n+1) + " & " + str(opt) + " & __ & " + str(deltaT) + "\\\\")
    
    print("  ", end="")
    for i in range(n+1):
        print(" {}".format(line[i]), end = " ")
    print()
    
    for i in range(n+1):
        for j in range(n+1):
            if j == 0:
                print(line[i], end= " ")
            print("{:2}".format(r[i][j]), end = " ")
        print(line[i], end= " ")
        print()
    
        
    print("For n = " + str(n+1) + ", OPT(i,j) resulted in " + str(opt) + " with deltaT = " + str(deltaT) + " seconds.")
    print( opt )

    i, j = 0, n
    while(i < n and j > 0 and r[i][j] != '-' and r[i][j] != 0):
        if(r[i+1][j] != '-' and r[i+1][j] == r[i][j]):
            i += 1
        elif(r[i][j-1] != '-' and r[i][j-1] == r[i][j]):
            j -= 1
        else:
            print(line[i] + '-' + line[j] + ' [' + str(i) +',' + str(j) + ']')
            i += 1
            j -= 1
    
main(sys.argv[1:])