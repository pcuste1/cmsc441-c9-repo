from __future__ import print_function
import sys
import time
sys.setrecursionlimit(1500)

matches = {'H':'G', 'G':'H', 'W':'T','T':'W'}
r = []
line = []

def OPT(n):
    for j in range(1, n+1):
        for i in range(0, j):
            for p in range(i,j-4):
                if matches[line[p]] == line[j]:
                    if i < j-4:
                        r[i][j] = max(r[i][j], r[i][p-1] + r[p+1][j-1] + 1)
            r[i][j] = max(r[i][j], r[i][j-1])
    return r[0][n]
            
def printBoard(n):
    print("  ", end="")
    for i in range(n+1):
        print(" {}".format(line[i]), end= " ")
    print()
    
    for i in range(n+1):
        for j in range(n+1):
            if j == 0:
                print("{}".format(line[i]), end= " ")
            print("{:2}".format(r[i][j]), end = " ")
        print()
    
            
def main():
    global r
    global line
    n = 69
    
    r = [[0 for i in range(n+1)] for i in range(n+1)]
    
    infile = open('test2.txt', 'r')
    
    for i in infile:
        line = list(i.strip())
        
    start_time = time.time()
    opt = OPT(n)
    
    deltaT = time.time() - start_time
    
    #print(r[len(l)][])

    if n < 69:
        printBoard(n)
    print(r[0][n])
    print(str(n+1) + " & " + str(opt) + " & __ & " + str(deltaT) + "\\\\")
    print(opt)

main()