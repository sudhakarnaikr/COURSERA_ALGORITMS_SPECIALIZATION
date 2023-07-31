# import math
# import numpy as np

# def tsp(cities):
#     nCities = len(cities)
#     mtrx = np.zeros((nCities, nCities))

#     for i in range(nCities):
#         for j in range(nCities):
#             a = cities[i][0] - cities[j][0]
#             b = cities[i][1] - cities[j][1]
#             mtrx[i][j] = math.sqrt(a * a + b * b)

#     # Initialize the DP table with infinity values
#     dp = np.full((nCities, 1 << nCities), float('inf'))
#     dp[0][1] = 0

#     # Precompute the minimum distances between two cities
#     min_distances = np.min(mtrx, axis=1)

#     # Iterate over all subsets of cities
#     for subset in range(1, 1 << nCities):
#         for city in range(1, nCities):
#             if (subset & (1 << city)) == 0:
#                 continue
#             prev_subset = subset ^ (1 << city)
#             for prev_city in range(nCities):
#                 if (prev_subset & (1 << prev_city)) == 0:
#                     continue
#                 dp[city][subset] = min(dp[city][subset], dp[prev_city][prev_subset] + mtrx[prev_city][city])

#     # Find the optimal solution
#     ans = float('inf')
#     final_subset = (1 << nCities) - 1
#     for city in range(1, nCities):
#         ans = min(ans, dp[city][final_subset] + mtrx[city][0])

#     return ans

# with open("tsp.txt") as f:
#     nCities = int(f.readline())
#     lines = f.readlines()

#     cities = []
#     for line in lines:
#         x, y = map(float, line.split())
#         cities.append([x, y])

#     result = tsp(cities)
#     print(result)
