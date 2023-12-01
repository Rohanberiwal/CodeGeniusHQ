#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Maximum number of vertices
#define MAX_VERTICES 1000

// Stack data structure
struct Stack {
    int top;
    int capacity;
    int* array;
};

// Function to initialize a stack
struct Stack* createStack(int capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

// Function to check if the stack is empty
bool isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

// Function to push an element onto the stack
void push(struct Stack* stack, int item) {
    stack->array[++stack->top] = item;
}

// Function to pop an element from the stack
int pop(struct Stack* stack) {
    if (isEmpty(stack))
        return -1; // Stack underflow
    return stack->array[stack->top--];
}

// Graph data structure
struct Graph {
    int vertices;
    int** adjacencyList;
};

// Function to create a graph
struct Graph* createGraph(int vertices) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->vertices = vertices;

    // Allocate memory for adjacency list
    graph->adjacencyList = (int**)malloc(vertices * sizeof(int*));
    for (int i = 0; i < vertices; ++i) {
        graph->adjacencyList[i] = (int*)malloc(vertices * sizeof(int));
    }

    return graph;
}

// Function to add an edge to the graph
void addEdge(struct Graph* graph, int src, int dest) {
    graph->adjacencyList[src][dest] = 1;
}

// Function to perform Depth First Search (DFS)
void DFS(struct Graph* graph, int vertex, bool* visited, struct Stack* stack) {
    visited[vertex] = true;

    for (int i = 0; i < graph->vertices; ++i) {
        if (!visited[i] && graph->adjacencyList[vertex][i] == 1) {
            DFS(graph, i, visited, stack);
        }
    }

    push(stack, vertex);
}

// Function to get the transpose of a graph
struct Graph* getTranspose(struct Graph* graph) {
    struct Graph* transposedGraph = createGraph(graph->vertices);

    for (int i = 0; i < graph->vertices; ++i) {
        for (int j = 0; j < graph->vertices; ++j) {
            transposedGraph->adjacencyList[i][j] = graph->adjacencyList[j][i];
        }
    }

    return transposedGraph;
}

// Function to print strongly connected components
void printSCC(struct Graph* graph) {
    bool* visited = (bool*)malloc(graph->vertices * sizeof(bool));
    struct Stack* stack = createStack(graph->vertices);

    for (int i = 0; i < graph->vertices; ++i) {
        visited[i] = false;
    }

    // Perform DFS and fill the stack
    for (int i = 0; i < graph->vertices; ++i) {
        if (!visited[i]) {
            DFS(graph, i, visited, stack);
        }
    }

    // Get the transposed graph
    struct Graph* transposedGraph = getTranspose(graph);

    // Reset visited array
    for (int i = 0; i < graph->vertices; ++i) {
        visited[i] = false;
    }

    // Process vertices in order defined by the stack
    while (!isEmpty(stack)) {
        int vertex = pop(stack);

        if (!visited[vertex]) {
            DFS(transposedGraph, vertex, visited, stack);
            printf("Strongly Connected Component: ");
            while (!isEmpty(stack)) {
                int componentVertex = pop(stack);
                printf("%d ", componentVertex);
                visited[componentVertex] = true;
            }
            printf("\n");
        }
    }

    free(visited);
    free(stack);
    free(transposedGraph);
}

int main() {
    // Example usage
    struct Graph* gr
