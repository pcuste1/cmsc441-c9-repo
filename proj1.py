from __future__ import print_function
import sys
import time
sys.setrecursionlimit(1500)

matches = {'H':'G', 'G':'H', 'W':'T','T':'W'}
r = []
line = []

def OPT(i,j):
    if not i < j-4:
        return 0
    
    if r[i][j] != '-':
        return r[i][j]

    q = -1
    for x in range(i, j-4):
        temp = OPT(i,x-1) + OPT(x+1, j-1)
        if matches[line[x]] == line[j]:
            q = max(temp + 1, q)
    #k = q
    q = max(q, OPT(i, j-1))
    #if k < q: optimal[j-1] = [j, q]
    r[i][j] = q
    return q

def main():
    global r
    global line
    n = 11
    
    r = [['-' for i in range(n+1)] for i in range(n+1)]
    
    infile = open('test.txt', 'r')
    
    for i in infile:
        line = list(i.strip())
        
    start_time = time.time()
    opt = OPT(0,n)
    
    deltaT = time.time() - start_time
    
    print(opt)


    print("  ", end="")
    for i in range(n+1):
        print(line[i], end= " ")
    print()
    
    for i in range(n+1):
        for j in range(n+1):
            if j == 0:
                print(line[i], end= " ")
            print(r[i][j], end = " ")
        print()
    
        
    print(str(n+1) + " & " + str(opt) + " & __ & " + str(deltaT) + "\\\\")
    print(opt)

main()