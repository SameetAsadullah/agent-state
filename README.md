# Classical AI Algorithms

A curated collection of foundational artificial-intelligence implementations covering state-space search, adversarial search, constraint satisfaction, local search, and evolutionary computation.

The implementations come from my original learning projects and remain intentionally close to their original form. This repository improves their organization, provenance, and reproducibility without replacing them with polished library implementations.

## Contents

| Area | Implementations |
|---|---|
| Maze search | [Breadth-first](search/maze/breadth-first-search), [depth-first](search/maze/depth-first-search), [greedy best-first](search/maze/greedy-best-first-search), and [A*](search/maze/a-star) |
| Graph search | [Depth-first search](search/graph/depth-first-search) and [A*](search/graph/a-star) |
| State-space search | [Eight puzzle](search/eight-puzzle) and [vacuum-world agent](agents/vacuum-world) |
| Adversarial search | Minimax for [tic-tac-toe](adversarial-search/tic-tac-toe) and [chess](adversarial-search/chess) |
| Constraint satisfaction | [Backtracking exam scheduling](constraint-satisfaction/exam-scheduling) |
| Local search | N-Queens with [hill climbing](local-search/n-queens-hill-climbing) and [simulated annealing](local-search/n-queens-simulated-annealing) |
| Evolutionary computation | [Genetic algorithm for knapsack](evolutionary-computation/knapsack-genetic-algorithm) |

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

## Getting started

The programs target Python 3 and use NumPy where array operations are needed.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run an exercise from its directory—for example:

```bash
python search/maze/a-star/src/main.py
```

Several programs are interactive and prompt for input in the terminal. Their original usage notes remain beside the source.

## Scope

These programs document my progression through classical AI techniques. They prioritize readable demonstrations of the underlying algorithms over framework abstractions or production performance.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for the source-repository mapping. Original per-project license files are retained where they existed. No blanket license is applied to exercises that previously had no declared license.
