# Agent State

Python implementations of state-space search, adversarial search, constraint satisfaction, local search, and evolutionary computation.

The algorithms are organized by method, with usage guidance, source attribution, and reproducible Python setup.

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
agents/                    Agent-environment implementations
adversarial-search/        Minimax-based game agents
constraint-satisfaction/   Backtracking and CSP solvers
evolutionary-computation/  Population-based optimization
local-search/              Hill climbing and simulated annealing
search/                    Graph, maze, and puzzle search
```

Each implementation contains its README and source files. Start with the README inside its directory for inputs and execution instructions.

## Getting started

The programs target Python 3 and use NumPy where array operations are needed.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run an implementation from its directory—for example:

```bash
python search/maze/a-star/src/main.py
```

Several programs prompt for input in the terminal. Usage notes are available beside the source.

## Scope

The source focuses on the underlying algorithms and their behavior.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for source history and licensing. Existing component licenses are retained; no blanket license is applied to programs that previously had no declared license.
