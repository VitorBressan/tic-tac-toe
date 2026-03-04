# TicTacToe

A command-line Tic Tac Toe game built with clean architecture principles, strong separation of concerns, and 100% test coverage using pytest.

This project focuses on code quality, testability, and maintainability rather than complexity.

## Key Highlights

* Object-Oriented Design
* Clear separation between game logic and interface
* 100% test coverage
* Unit and Integration tests
* Parametrized testing with pytest
* Clean and scalable project structure
* No external runtime dependencies (pure Python implementation)

## Architecture Overview

The project is divided into two main layers:

### 1️: Game Engine

Responsible for:

* Managing board state
* Validating moves
* Switching players
* Detecting wins and draws
* Returning structured game status

The engine contains no input/output logic, making it fully deterministic and easy to test.

### 2️: CLI Interface

Responsible for:

* Handling user input
* Displaying the board
* Running the game loop

This separation ensures:

* High testability
* Single Responsibility Principle
* Clean boundaries between logic and presentation

## 🧪 Testing Strategy

The project includes two testing layers:

### Unit Tests

Test isolated behaviors such as:

* Win detection
* Draw detection
* Move validation
* Player switching

Unit tests ensure each component behaves correctly in isolation.

### Integration Tests

Simulate full game flows to verify that:

* Components interact correctly
* The game state transitions are consistent
* Win/draw conditions are correctly detected during real match scenarios

All tests are written using `pytest`, with extensive use of `@pytest.mark.parametrize` and `@pytest.fixture` to cover multiple scenarios cleanly.

Test Coverage: 100%

## 📂 Project Structure

tictactoe/ → core game logic  
tests/unit/ → isolated behavior tests  
tests/integration/ → full game flow tests  

## ▶ Running the Game

```bash
python -m tictactoe
```

## 🧪 Running Tests

Run all tests:
```bash
python -m pytest
```

Run only unit tests:
```bash
python -m pytest tests/unit
```

Run only integration tests:
```bash
python -m pytest tests/integration
```

Run with coverage:
```bash
python -m pytest --cov=tictactoe
```

## 📌 Purpose of This Project

This project was intentionally designed to focus on:

* Clean separation of concerns
* Deterministic and testable business logic
* Structured testing strategy (unit + integration)
* Professional project organization

Although the domain is simple, the goal was to apply production-oriented development practices to a small system.
