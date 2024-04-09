from constraint import *

problem = Problem()

problem.addVariables(['a','b','c'], range(1,4))

problem.addConstraint(lambda a,b : a != b, ('a', 'b'))
problem.addConstraint(lambda b,c : b != c, ('b', 'c'))
problem.addConstraint(lambda a,c : a != c, ('a', 'c'))

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)