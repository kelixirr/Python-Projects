import math

def nr_merge(src, result, start, inc):
    end1 = start + inc
    end2 = min(start + 2*inc, len(src))
    x, y, z = start, start + inc, start

    while x < end1 and y < end2:

        if src[x] < src[y]:
            result[z] = src[x]; x+= 1
        else:
            result[z] = src[y]; y+= 1

        z += 1

    if x < end1:
        result[z:end2] = src[x:end1]
    elif y < end2:
        result[z:end2] = src[y:end2]

def merge_sort(S):
    n = len(S)
    logn = math.ceil(math.log(n, 2))
    src, dest = S, [None] * n
    for i in (2**k fork in range(logn)):
        for j in range(0, n, 2*i):
            nr_merge(src, dest, j, i)
        src, dest = dest, src
    if S is not src:
        S[0:n] = src[0:n]
