PYTHON = python3
MAIN = a_maze_ing.py
CONFIG = config.txt
VENV = venv
VENV_PYTHON = ./$(VENV)/bin/python3
VENV_PIP = ./$(VENV)/bin/pip

#COLORS
GREEN = \033[0;32m
YELLOW = \033[0;33m
RED    = \033[0;31m
RESET = \033[0m

.PHONY: all install run debug clean lint

$(VENV):
	@echo "$(YELLOW)Venv not found. Creating it...$(RESET)"
	@$(PYTHON) -m venv $(VENV)
	@$(VENV_PIP) install -e . flake8 mypy
	
all: install

install:
	@echo "$(GREEN)Creating virtual environment and installing dependencies...$(RESET)"
	@$(PYTHON) -m venv $(VENV)
	@$(VENV_PIP) install --upgrade pip
	@$(VENV_PIP) install -e . flake8 mypy

run: $(VENV)
	@echo "$(GREEN)Launching A-Maze-Ing...$(RESET)"
	@$(VENV_PYTHON) $(MAIN) $(CONFIG)

debug:
	@echo "$(YELLOW)Debugging...$(RESET)"
	$(VENV_PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	@echo "$(RED)Cleaning build artifacts...$(RESET)"
	@rm -rf $(VENV) build/ dist/ *.egg-info
	@rm -rf __pycache__
	@rm -rf maze_gen/__pycache__
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@find . -maxdepth 1 -type f -name "*.txt" ! -name "config.txt" -delete

lint: $(VENV)
	@$(VENV_PYTHON) -m flake8 . --exclude=$(VENV),build,dist
	@$(VENV_PYTHON) -m mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .

lint-strict: $(VENV)
	@$(VENV_PYTHON) -m flake8 . --exclude=$(VENV),build,dist
	@$(VENV_PYTHON) -m mypy --strict .

package: $(VENV)
	@echo "$(GREEN)Building wheel package...$(RESET)"
	$(VENV_PIP) install build
	$(VENV_PYTHON) -m build .