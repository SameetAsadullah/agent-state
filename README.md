# Classical AI Algorithms

A curated collection of foundational artificial-intelligence implementations covering state-space search, adversarial search, constraint satisfaction, local search, and evolutionary computation.

The implementations come from my original learning projects and remain intentionally close to their original form. This repository improves their organization, provenance, and reproducibility without replacing them with polished library implementations.

## Contents

| Area | Implementations |
|---|---|
| Maze search | Breadth-first, depth-first, greedy best-first, and A* |
| Graph search | Depth-first search and A* |
| State-space search | Eight puzzle and vacuum-world agent |
| Adversarial search | Minimax for tic-tac-toe and chess |
| Constraint satisfaction | Backtracking exam scheduling |
| Local search | N-Queens with hill climbing and simulated annealing |
| Evolutionary computation | Genetic algorithm for knapsack |

## Repository layout

```text
agents/                    Agent-environment exercises
adversarial-search/        Minimax-based game agents
constraint-satisfaction/   Backtracking and CSP exercises
evolutionary-computation/  Population-based optimization
local-search/              Hill climbing and simulated annealing
search/                    Graph, maze, and puzzle search
```

Each exercise contains its original README and source files. Start with the README inside an exercise directory for its inputs and execution instructions.

## Scope

These programs document my progression through classical AI techniques. They prioritize readable demonstrations of the underlying algorithms over framework abstractions or production performance.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for the source-repository mapping. Original per-project license files are retained where they existed. No blanket license is applied to exercises that previously had no declared license.
