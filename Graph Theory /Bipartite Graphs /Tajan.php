<?php

class Graph {
    private $vertices;
    private $adjacencyList;
    private $index;
    private $lowlink;
    private $onStack;
    private $stack;
    private $result;

    public function __construct($vertices) {
        $this->vertices = $vertices;
        $this->adjacencyList = array_fill(0, $vertices, array());
        $this->index = array_fill(0, $vertices, -1);
        $this->lowlink = array_fill(0, $vertices, -1);
        $this->onStack = array_fill(0, $vertices, false);
        $this->stack = [];
        $this->result = [];
    }

    public function addEdge($src, $dest) {
        $this->adjacencyList[$src][] = $dest;
    }

    public function tarjan() {
        for ($i = 0; $i < $this->vertices; ++$i) {
            if ($this->index[$i] == -1) {
                $this->strongConnect($i);
            }
        }

        return $this->result;
    }

    private function strongConnect($v) {
        $this->index[$v] = $this->lowlink[$v] = $this->index;
        $this->stack[] = $v;
        $this->onStack[$v] = true;

        foreach ($this->adjacencyList[$v] as $w) {
            if ($this->index[$w] == -1) {
                $this->strongConnect($w);
                $this->lowlink[$v] = min($this->lowlink[$v], $this->lowlink[$w]);
            } elseif ($this->onStack[$w]) {
                $this->lowlink[$v] = min($this->lowlink[$v], $this->index[$w]);
            }
        }

        if ($this->lowlink[$v] == $this->index[$v]) {
            $component = [];
            do {
                $w = array_pop($this->stack);
                $this->onStack[$w] = false;
                $component[] = $w;
            } while ($w != $v);
            $this->result[] = $component;
        }
    }
}

// Example usage:
$graph = new Graph(5);
$graph->addEdge(0, 1);
$graph->addEdge(1, 2);
$graph->addEdge(2, 0);
$graph->addEdge(1, 3);
$graph->addEdge(3, 4);

$result = $graph->tarjan();

echo "Strongly Connected Components:\n";
foreach ($result as $component) {
    echo implode(' ', $component) . "\n";
}
