a = "SEND"
b = "MORE"
c = "MONEY"
import constraint
def solve_cryptarithmetic():
  problem = constraint.Problem()
  problem.addVariables("SM", range(1,10))
  problem.addVariables("ENDORY", range(10))
  problem.addConstraint(constraint.AllDifferentConstraint(), "SENDMORY")
  def cryptarithmetic_constraints(S, E, N, D, M, O, R, Y):
    send = S*1000 + E*100 + N*10 + D
    more = M*1000 + O*100 + R*10 + E
    money = M*10000 + O*1000 + N*100 + E*10 + Y
    return send + more == money
  problem.addConstraint(cryptarithmetic_constraints, "SENDMORY")
  solutions = problem.getSolutions()
  print(solutions)
solve_cryptarithmetic()
