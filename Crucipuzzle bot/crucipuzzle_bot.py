# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:08:32 2021

@author: paolo
"""
# Mio progetto universitario sviluppato durante il corso di python
import re

def es1(ftesto):
    parole = []
    matrice = []
    with open(ftesto, encoding='utf8') as f:
        line = f.readline()
        while line == '\n':                         # ignoro le linee vuote iniziali
            line = f.readline()
        while line != '\n':                         # tengo la matrice
            matrice.append(line.replace('\t', ''))  # e ne tolgo i tab
            line = f.readline()
        while line == '\n':                         # salto le linee vuote seguenti
            line = f.readline()
        while line != '\n':                         # e tengo solo le parole
            parole.append(line.strip())             # togliendo l'andare a capo e gli spazi iniziali
            line = f.readline()
                                                   
    parole_rev = list(map(lambda x: x[::-1], parole))   # costruisco le parole rovesciate
    biparole = parole + parole_rev                  # d'ora in poi cerco entrambe
    biparole.sort()
    contenute  = []
    contenenti = []
    for i in range(len(biparole)-1):
        prima, seconda = biparole[i:i+2]
        if prima in seconda:
            contenute.append(prima)
        

    biparole.sort(key=lambda x: (-len(x),x))
    matrice = ''.join(matrice)                      # lascio la matrice come una stringa
    # print(matrice, '\n\n', biparole)
    cerca = re.compile('('+('|'.join(biparole))+')')    # re. per cercare le parole
    marcate = [ [c] for c in matrice ]              # lista di caratteri che indicano quali lettere restano
    #print(''.join([c[0] for c in marcate]))
    process_dritta(cerca, matrice, marcate, biparole)         # cerco le parole nella matrice normale
    #print(''.join([c[0] for c in marcate]))
    process_trasposta(cerca, matrice, marcate, biparole)      # nella trasposta
    #print(''.join([c[0] for c in marcate]))
    process_d_principale(cerca, matrice, marcate, biparole)   # nelle diagonali principali
    #print(''.join([c[0] for c in marcate]))
    process_d_secondaria(cerca, matrice, marcate, biparole)   # nelle secondarie
    #print(''.join([c[0] for c in marcate]))
    return collect(marcate)                         # raccolgo le lettere rimaste

def cerca_parole(cerca, testo, marcate, tipo, parole):
    # print(''.join([c[0] for c in marcate]))
    match = cerca.search(testo)
    while match:
        #print(tipo, match[0])
        # assert match[0] in parole
        for i in range(*match.span()):
            marcate[i][0] = ' '
        match = cerca.search(testo, match.start()+1)

def process_dritta(cerca, matrice, marcate, parole):
    cerca_parole(cerca, matrice, marcate, 'dritta', parole)

def process_trasposta(cerca, matrice, marcate, parole):
    mat2 = matrice.split()
    w    = len(mat2[0])
    h    = len(mat2)
    matrice_t = [['\n']*(h+1) for _ in range(w)]
    marcate_t = ['\n']*((h+1)*w)
    # print(marcate)
    for y, riga in enumerate(mat2):
        for x, c in enumerate(riga):
            matrice_t[x][y] = c
            marcate_t[x*(h+1)+y] = marcate[y*(w+1)+x]
    # print('marcate_t pre', ''.join([c[0] for c in marcate_t]))
    matrice_t = ''.join([''.join(riga) for riga in matrice_t])
    # print('trasposta\n',matrice_t)
    cerca_parole(cerca, matrice_t, marcate_t, 'trasposta', parole)
    # print('marcate_post', ''.join([c[0] for c in marcate_t]))
    # print(matrice, matrice_t, marcate, marcate_t, sep='\n\n')

def process_d_principale(cerca, matrice, marcate, parole):
    mat2 = matrice.split()
    w = len(mat2[0])
    h = len(mat2)
    marc2 = [marcate[i:i+w] for i in range(0, len(marcate), w + 1)]
    diagonali      = [[] for _ in range (w + h - 1)]
    diagonali_marc = [[] for _ in range (w + h - 1)]
    for y in range(h):
        for x in range(w):
            diagonale = y+x
            diagonali[diagonale].append(mat2[y][w-x-1])
            diagonali_marc[diagonale].append(marc2[y][w-x-1])
    for d in diagonali_marc:
        d.append(['\n'])
    marc2 = [ el for d in diagonali_marc for el in d ]
    matrice_diag = '\n'.join([''.join(d) for d in diagonali])
    # print(matrice, matrice_diag, marc2, sep='\n\n')
    cerca_parole(cerca, matrice_diag, marc2, 'diag_princ', parole)

def process_d_secondaria(cerca, matrice, marcate, parole):
    mat2 = matrice.split()
    w = len(mat2[0])
    h = len(mat2)
    marc2 = [marcate[i:i + w + 1] for i in range(0, len(marcate), w + 1)]
    diagonali      = [[] for _ in range (w + h - 1)]
    diagonali_marc = [[] for _ in range (w + h - 1)]
    for y in range(h):
        for x in range(w):
            diagonale = y+x
            diagonali[diagonale].append(mat2[y][x])
            diagonali_marc[diagonale].append(marc2[y][x])
    for d in diagonali_marc:
        d.append(['\n'])
    marc2 = [ el for d in diagonali_marc for el in d ]
    matrice_diag = '\n'.join([''.join(d) for d in diagonali])
    # print(matrice, matrice_diag, sep='\n\n')
    cerca_parole(cerca, matrice_diag, marc2, 'diag_sec', parole)

def collect(marcate):
    return ''.join([ c[0] for c in marcate if c[0] not in ['\n',' ']])
        
        
soluzione = es1("cp6_Pensiero.txt")
print(soluzione)
