from itertools import permutations

def all_var(x):
    result = list(set(permutations(x)))
    return [list(permutation) for permutation in result]


if __name__=='__main__':
    print(all_var([1,2,3]))
    print(all_var([1,1,2]))
    print(all_var([0]))
