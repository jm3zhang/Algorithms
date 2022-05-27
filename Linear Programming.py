#!/usr/bin/env python3
from scipy.optimize import linprog

def max_flow(cap, s, t):
    """
    Input: A matrix giving the capacity on each edge.
            If c[i,j] = 0, then the edge (i,j) is not in the graph
           A source s and sink node t,
    Output: A matrix giving the flow on each edge,
            A number giving the value of the max flow.
    """
    n = len(cap)
    # start with capacity bounds
    bounds = []
    for i in range(n):
        for j in range(n):
            lower_upper = (0, cap[i][j])
            bounds.append(lower_upper)

    # next do flow constaints.  Will have one row in Aeq for each flow constaint
    Aeq = []
    beq = []
    for i in range(n):
        if i != s and i != t:
            beq.append(0)
            row = []
            outflow = n * [0]
            outflow[i] = -1
            for j in range(n):
                if i == j:
                    row.extend(n * [1])
                else:
                    row.extend(outflow)
            Aeq.append(row)

    # finally, make c
    c = []
    n_negones =  n * [-1]
    for i in range(n):
        if i == s:
            c.extend(n * [-1])
        else:
            c.extend(n * [0])

    opt = linprog(c=c, A_eq=Aeq, b_eq=beq, bounds=bounds, method='revised simplex')
    print("\n example output: \n", opt)
    # extract the solution from opt
    flow = []
    count = 1
    row = []
    for i in range(len(opt.x)):
        if count < n:
            count += 1
            row.append(opt.x[i])
        else:
            row.append(opt.x[i])
            flow.append(row)
            row = []
            count = 1

    return flow, -opt.fun


def main():
    """
    Testing your LP.  The following is a single example.  Your alg
    should work for any input.
    """
    c = [[0, 3, 4, 0, 0],
         [0, 0, 1, 0, 2],
         [0, 0, 0, 5, 0],
         [0, 0, 0, 0, 6],
         [1, 1, 0, 0, 0]]
    s = 0
    t = 4
    print(max_flow(c, s, t))

    '''
    Optimal solution is the following output :

         con: array([0., 0., 0.])
         fun: -7.0
     message: 'Optimization terminated successfully.'
         nit: 6
       slack: array([], dtype=float64)
      status: 0
     success: True
           x: array([0., 3., 4., 0., 0., 0., 0., 1., 0., 2., 0., 0., 0., 5., 0., 0., 0., 0., 0., 5., 0., 0., 0., 0., 0.])

    The output should be interpreted as follows:
    1) the optimization has a value of 7.0.  Note, linprog solves minimization problems.
       To solve a maximization we solve:  min -c^T x. That is why fun = -7.0.

    2)  the array x contains the flow on each edge. the flow on edge (i,j) is contained in entry
         i * n + j.  For example, the flow on the edge (2,3), which has capacity 5 is the 13th
         entry in x, which is 5.0.  (Note Python uses zero indexing.)
    '''




if __name__ == '__main__':
    main()
