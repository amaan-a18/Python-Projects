from constraint import *
problem = Problem()
problem.addVariables(range(0, 16), range(1, 16 + 1))
problem.addConstraint(AllDifferentConstraint(), range(0, 16))
problem.addConstraint(ExactSumConstraint(34), [0, 5, 10, 15])
problem.addConstraint(ExactSumConstraint(34), [3, 6, 9, 12])
for row in range(4):
    problem.addConstraint(ExactSumConstraint(34),[row * 4 + i for i in range(4)])
for col in range(4):
    problem.addConstraint(ExactSumConstraint(34),[col + 4 * i for i in range(4)])
print("Running… please wait")
solutions = problem.getSolutions()
print("Done:", solutions)
