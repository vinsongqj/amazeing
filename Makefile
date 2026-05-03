PYTHON = python3
MAIN = a_maze_ing.py
CONFIG = config.txt
VENV_PYTHON = ./venv/bin/python

#COLORS

GREEN = \033[0;32m
YELLOW = \033[0;33m
RED    = \033[0;31m
RESET = \033[0m

.PHONY: all install run debug clean lint

all: install

install:
	@echo "$(GREEN)Creating virtual environment and installing dependencies...$(RESET)"
	$(PYTHON) -m venv venv
	@./venv/bin/pip install . flake8 mypy

run:
	@echo "$(GREEN)Launching A-Maze-Ing...$(RESET)"
	$(VENV_PYTHON) $(MAIN) $(CONFIG)

debug:
	@echo "$(YELLOW)Debugging...$(RESET)"
	$(VENV_PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	@echo "$(RED)Cleaning build artifacts...$(RESET)"
	@rm -rf venv build/ dist/ *.egg-info
	@rm -rf __pycache__
	@rm -rf maze_gen/__pycache__
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@find . -maxdepth 1 -type f -name "*.txt" ! -name "config.txt" -delete

lint:
	flake8 .
	mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .

lint-strict:
	flake8 .
	mypy --strict .

package:
	@echo "$(GREEN)Building wheel package...$(RESET)"
	$(VENV_BIN) pip install build
	$(VENV_BIN) python3 -m build