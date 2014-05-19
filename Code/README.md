6.851 Advanced Data Structures Project

====================

Fermi Ma and Erik Waingarten

---------------------

## Dependencies

* [`PuLP 1.5.6`] (https://pypi.python.org/pypi/PuLP) python linear programming wrapper
* Any of the following LP/ILP solvers: [`GLPK`](http://www.gnu.org/software/glpk/), [`COIN CLP/CBC`](http://www.coin-or.org/projects/), [`CPLEX`](http://www-01.ibm.com/software/commerce/optimization/cplex-optimizer/), and [`GUROBI`](http://www.gurobi.com/)
* [`matplotlib`](http://matplotlib.org/) to plot the results

## Information on Organization and Usage

The file GenerateILP.py contains all the code to generate the vector form of the linear program. The function `generateILP(points)` outputs a pair `(optimization, contraints)` where optimization is the vector `c` of the linear program, and contraints is the pair `A,b` of the linear program. Where the linear program says maximize `cx` such that `Ax <= b`.

In the function `generateILP(points)` if the length of points is `n`, then it is implied that all points live in `{0, ..., n-1} x {0, ..., n-1}` and that there is a point in each column. Otherwise, the program will still work, but it will generate more variables and constraints that will just slow down the program.

The file SolveLP.py contains all the code to translate a linear program in matrix form, to one of the form that PuLP requires and solves it, the function of interests is `solve(points)` which solves the program and returns an `LpProblem` object.

The file RunTests.py runs several tests, to get the integrality gap. 

The file ViewResults.py contains a method to take the file output of what RunTests produce and visualize it with `matplotlib`.

## Contact

Please contact Erik Waingarten (eaw@mit.edu), for any more information or help with understanding/using the code.