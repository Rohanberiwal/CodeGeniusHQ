#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

const int INF = 1e9;

int tsp(int mask, int pos, const std::vector<std::vector<int>>& graph, std::vector<std::vector<int>>& dp) {
    int n = graph.size();

    // If all cities have been visited
    if (mask == (1 << n) - 1) {
        return graph[pos][0];  // Return to the starting city
    }

    // If the subproblem has already been solved
    if (dp[mask][pos] != -1) {
        return dp[mask][pos];
    }

    int ans = INF;

    // Try visiting each unvisited city
    for (int next = 0; next < n; ++next) {
        if ((mask & (1 << next)) == 0) {  // If the next city is not visited
            int newMask = mask | (1 << next);
            ans = std::min(ans, graph[pos][next] + tsp(newMask, next, graph, dp));
        }
    }

    // Memoize the result
    return dp[mask][pos] = ans;
}

int main() {
    int n;  // Number of cities
    std::cout << "Enter the number of cities: ";
    std::cin >> n;

    // Initialize the graph with distances between cities
    std::vector<std::vector<int>> graph(n, std::vector<int>(n, 0));
    std::cout << "Enter the distance matrix (0 for same city, INF for unreachable):\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> graph[i][j];
        }
    }

    // Initialize memoization table
    std::vector<std::vector<int>> dp(1 << n, std::vector<int>(n, -1));

    // Start the TSP from the first city
    int minDistance = tsp(1, 0, graph, dp);  // '1' represents the starting city

    std::cout << "Minimum distance for the TSP: " << minDistance << "\n";

    return 0;
}
