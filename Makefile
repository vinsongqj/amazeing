PYTHON = python3
PIP = pip 
MAIN = a_maze_ing.py
CONFIG = config.txt

#COLORS

GREEN = \033[0;32m
YELLOW = \033[0;33m
RED    = \033[0;31m
RESET = \033[0m

.PHONY: all install run debug clean lint

all: install

install:
	@echo "$(GREEN)Installing mazegen package...$(RESET)"
	$(PIP) install .

run:
	@echo "$(GREEN)Launching A-Maze-Ing...$(RESET)"
	$(PYTHON)	$(MAIN)	$(CONFIG)

debug:
	@echo "$(YELLOW)Debugging...$(RESET)"
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	@echo "$(RED)Cleaning build artifacts...$(RESET)"
	@rm -rf __pycache__
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache

lint:
	flake8 .
	mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .

lint-strict:
	flake8 .
	mypy --strict .