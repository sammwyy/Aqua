#!/bin/bash
python scripts/ast_transformer.py
python scripts/data_preprocessing.py
python scripts/model_training.py
python scripts/model_evaluation.py