import Foundation

enum Color {
    case none, red, blue
}

func isBipartite(_ graph: [[Int]]) -> Bool {
    guard graph.count > 0 else {
        return true // An empty graph is trivially bipartite
    }

    let n = graph.count
    var colors = [Color](repeating: .none, count: n)

    for start in 0..<n {
        if colors[start] == .none {
            if !bfs(graph, start, &colors) {
                return false
            }
        }
    }

    return true
}

func bfs(_ graph: [[Int]], _ start: Int, _ colors: inout [Color]) -> Bool {
    var queue = [Int]()
    queue.append(start)
    colors[start] = .red

    while !queue.isEmpty {
        let current = queue.removeFirst()

        for neighbor in graph[current] {
            if colors[neighbor] == .none {
                colors[neighbor] = (colors[current] == .red) ? .blue : .red
                queue.append(neighbor)
            } else if colors[neighbor] == colors[current] {
                return false // Graph is not bipartite
            }
        }
    }

    return true
}

// Example usage:
let graph = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]

if isBipartite(graph) {
    print("The graph is bipartite.")
} else {
    print("The graph is not bipartite.")
}
