# IAI SLE-2 – BFS vs DFS Profiling

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM026  
**Name:** Aditya Sanjay Patil  
**Division:** A  
**Date:** 22/09/2026

## Aim
Implement Breadth-First Search (BFS) and Depth-First Search (DFS) on a 1000-node graph and compare execution time and expanded nodes.

## Problem Setup
- Graph size: 1000 nodes
- Start node: 0
- Goal node: 999
- Timing: Python timeit
- Optional profiler: py-spy

## Files
- bfs.py – BFS implementation, node counting and timing
- dfs.py – DFS implementation, node counting and timing
- graph.svg – graph visualization
- CONTRIBUTION_LOG.md – development and AI contribution record

## Run
    python bfs.py
    python dfs.py

## py-spy Profiling
Install:
    pip install py-spy

Record sampling profiles:
    py-spy record --output bfs-profile.svg -- python bfs.py
    py-spy record --output dfs-profile.svg -- python dfs.py

Live terminal profiling:
    py-spy top -- python bfs.py
    py-spy top -- python dfs.py

## Results from the SLE-2 Report

| Case | Algorithm | Goal | Average Time (ms) | Nodes Expanded |
|---|---|---:|---:|---:|
| Best | BFS | 2 | 0.14260 | 3 |
| Best | DFS | 2 | 0.11840 | 3 |
| Average | BFS | 500 | 27.68430 | 501 |
| Average | DFS | 500 | 15.32780 | 335 |
| Worst | BFS | 999 | 52.41670 | 1000 |
| Worst | DFS | 999 | 31.84250 | 1000 |

These are the measurements documented in the submitted SLE-2 report, not universal performance values. The report notes that performance depends on graph structure and traversal order.

## Observation
For the selected test cases, DFS had lower measured execution time. BFS expanded fewer nodes in the reported average case, while both expanded all 1000 nodes in the selected worst case.

## AI Contribution
Gemini / ChatGPT helped prepare the BFS and DFS profiling code, timeit measurement, node counting, and documentation. The student studied the code, understood the profiling process, reviewed the results, and prepared the final report.
