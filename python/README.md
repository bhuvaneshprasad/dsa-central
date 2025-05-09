# 🐍 Python DSA Module

This folder contains Python implementations of core **Data Structures** and **Algorithms**, organized for clarity and reusability.

---

## 📁 Folder Structure

```test
python/
├── src/
│   ├── data_structures/   # Core data structures (e.g., Stack, Queue, Tree)
│   └── algorithms/        # Sorting, searching, recursion, etc.
├── tests/                 # Unit tests for all modules
└── pyproject.toml         # Project and dependency configuration
```

## 📦 Project and Dependency Configuration

The project uses [`uv`](https://github.com/astral-sh/uv) to manage dependencies via a `pyproject.toml` file. This file contains:

- Project metadata (name, version, description, etc.)
- Runtime and development dependencies (like `pytest`, `black`, etc.)
- Test configuration for tools like `pytest`

---

## 🚀 Getting Started

> This project uses [`uv`](https://github.com/astral-sh/uv) — a fast, modern Python package manager.

### 1. Install `uv` (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
