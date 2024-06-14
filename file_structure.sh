#!/bin/bash

# Set the project root directory
PROJECT_ROOT="sow_root"

# Create the main project directory
mkdir -p $PROJECT_ROOT

# Create source directory and subdirectories
mkdir -p $PROJECT_ROOT/src/utils
mkdir -p $PROJECT_ROOT/src/prompts
mkdir -p $PROJECT_ROOT/src/services
mkdir -p $PROJECT_ROOT/src/models
mkdir -p $PROJECT_ROOT/src/analysis

# Create tests directory
mkdir -p $PROJECT_ROOT/tests

# Create empty __init__.py files
touch $PROJECT_ROOT/src/__init__.py
touch $PROJECT_ROOT/src/utils/__init__.py
touch $PROJECT_ROOT/src/prompts/__init__.py
touch $PROJECT_ROOT/src/services/__init__.py
touch $PROJECT_ROOT/src/models/__init__.py
touch $PROJECT_ROOT/src/analysis/__init__.py
touch $PROJECT_ROOT/tests/__init__.py

# Create main Python files
touch $PROJECT_ROOT/src/config.py
touch $PROJECT_ROOT/src/main.py

# Create utility Python files
touch $PROJECT_ROOT/src/utils/logging.py
touch $PROJECT_ROOT/src/utils/requests.py

# Create prompts Python files
touch $PROJECT_ROOT/src/prompts/gpt_prompts.py

# Create service Python files
touch $PROJECT_ROOT/src/services/openai_service.py
touch $PROJECT_ROOT/src/services/embedding_service.py
touch $PROJECT_ROOT/src/services/bing_search.py

# Create model Python files
touch $PROJECT_ROOT/src/models/researcher.py

# Create analysis Python files
touch $PROJECT_ROOT/src/analysis/data_cleaning.py
touch $PROJECT_ROOT/src/analysis/embeddings.py
touch $PROJECT_ROOT/src/analysis/qdrant_management.py

# Create test Python files
touch $PROJECT_ROOT/tests/test_openai_service.py
touch $PROJECT_ROOT/tests/test_embedding_service.py
touch $PROJECT_ROOT/tests/test_main.py

# Create other project files
touch $PROJECT_ROOT/requirements.txt
touch $PROJECT_ROOT/.env
touch $PROJECT_ROOT/README.md
touch $PROJECT_ROOT/setup.py

echo "Project structure created successfully!"
