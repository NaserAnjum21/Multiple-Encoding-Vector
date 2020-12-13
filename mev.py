import os
import sys
import numpy as np
import pandas as pd

import time
start_time = time.time()

R = ['A', 'G']
Y = ['C', 'T']

M = ['A', 'C']
K = ['G', 'T']

S = ['C', 'G']
W = ['A', 'T']


def get_encoding(group, seq):

    encoding = [1 if w in group or w == 'N' else 0 for w in seq]
    # encoding = [1 if x in group else 0 for x in seq] #alternate encoding where N denotes nothing
    return encoding


def get_feature(group, seq):
    encoding = get_encoding(group, seq)
    n = len(encoding)
    freq = sum(encoding)
    mean = sum( [ w*(i+1) for i, w in enumerate(encoding)] ) / freq
    variance = sum( [ w*((i+1 - mean)**2) for i, w in enumerate(encoding)] ) / (n * freq)
    return freq, mean, variance


def get_MEV(seq):

    fast_vector = []
    fast_vector.extend(get_feature(R,seq))
    fast_vector.extend(get_feature(Y,seq))
    fast_vector.extend(get_feature(M,seq))
    fast_vector.extend(get_feature(K,seq))
    fast_vector.extend(get_feature(S,seq))
    fast_vector.extend(get_feature(W,seq))

    assert len(fast_vector) == 18
    return fast_vector

def get_distance(vects):
    n = vects.shape[0]
    matrix = np.zeros((n,n))

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j] = matrix[j][i] = np.linalg.norm((vects[i,:] - vects[j,:]), ord=2)

    return matrix


def get_sequences(inFile):
    names = []
    seqs = []
    seq = ""
    with open(inFile) as f:
        for line in f:
            if line.startswith('>'):
                names.append(line.strip()[1:])
                if len(seq) > 0:
                    seqs.append(seq)
                seq = ""
            elif line[0].isalpha():
                seq += line.strip()
        seqs.append(seq)

    # print(seqs)
    # print(names)

    return names, seqs


if __name__ == "__main__":

    inFile = sys.argv[1]
    outFile = sys.argv[2]

    names, seqs = get_sequences(inFile)

    vects = []

    for seq in seqs:
        fast_vect = get_MEV(seq)
        vects.append(fast_vect)

    vects = np.array(vects)
    matrix = get_distance(vects)

    df = pd.DataFrame(matrix,index = names, columns=names)
    df.to_csv(outFile,index=True)
    #print(df)
    print("Done in  --- %s seconds ---" % (time.time() - start_time))
