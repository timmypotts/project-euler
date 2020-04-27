# I started with counting the number of nodes given an (n*n) grid.
# The number of nodes in an n*n grid is (n+1)^2
# The best way to find out the total number of paths from (0,0) to (n,n) on the grid was by finding the number of possible paths to (n,n) from points (n-1,n-1), (n-2, n-1), and so on.

# TERMINOLOGY:
# ==========================================================================
# Let's denote the number of possible paths to point (n,n) as NOP
# If the NOP from point (x,y) is 4, then that will be denoted as NOP(x,y)=4

# AXIOMS:
# ==========================================
# (1) NOP(0,n)=1, NOP(1,n)=1, ..., NOP(n-1,n)=1
# (2) NOP(n,0)=1, NOP(n,1)=1, ..., NOP(n,n-1)=1
# (3) NOP(a,b) = NOP(a+1,b) + NOP(a,b+1)

# EXAMPLES
# =====================================
# If we made a matrix of NOP(x,y) values for the n=2 example grid, it would appear as such:
#   6   3   1
#   3   2   1
#   1   1   0

# A n=3 grid:
#   20  10  4   1
#   10  6   3   1
#   4   3   2   1
#   1   1   1   0

# I start by initializing an n by n matrix, setting every element to -1 before I proceed.


import numpy as np


def lattice(n):
    grid = [[-1 for i in range(n+1)] for j in range(n+1)]
# From here, NOP(n,n)=0
    grid[n][n] = 0


# Follow axioms 1 & 2
    for i in range(0, n):
        grid[i][n] = 1
        grid[n][i] = 1

# Implement axiom 3 for the rest of the grid/matrix
    for k in range(1, n):
        for j in range(n-k, -1, -1):
            grid[n-k][j] = (grid[n-k][j+1] + grid[n-k+1][j])
            grid[j][n-k] = grid[n-k][j]

    nop = grid[1][0]+grid[0][1]
    grid[0][0] = nop

    print(np.matrix(grid))
    print("The number of unique paths is ", nop)


# Test our algorithm on n=20, as the problem asks.
lattice(20)

# We get an answer of 137846528820, which is correct
