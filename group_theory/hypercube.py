from sympy.combinatorics.perm_groups import PermutationGroup
from sympy.combinatorics import Permutation

a = Permutation([1,0,2,3,4,5])
b = Permutation([0,1,3,2,4,5])
c = Permutation([0,1,2,3,5,4])
G = PermutationGroup([a,b,c])

#Get the generators (permutations a, b, c)
print G.strong_gens
#I dont know
print G.base
#get the elements of the group
print G.order()

print G.asPresentation