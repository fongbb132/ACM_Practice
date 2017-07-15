def knapsack(W, wt, val):
    if len(wt) == 0 or W == 0 :
        return 0
    if wt[0]>W:
        return knapsack(W, wt[1:], val[1:])
    else:
        return max(knapsack(W, wt[1:], val[1:]), (val[0] + knapsack(W-wt[0], wt[1:], val[1:])))

print knapsack(50, [10, 20, 30], [60, 100, 120])