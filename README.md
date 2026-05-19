# Algerian Sentiment

NLP model and utilities for Algerian Arabic sentiment analysis using Transformers.

## Problem Statement
Sentiment analysis resources are scarce for dialectal Algerian Arabic. This repository provides a reproducible pipeline and model checkpoints to analyze sentiment in Algerian Arabic corpora.

## Features
- Dataset preprocessing scripts
- Transformer-based training and evaluation scripts
- Inference utilities and example notebooks

## Tech Stack
- Python
- Hugging Face Transformers
- PyTorch / TensorFlow (check scripts)

## Installation
1. Clone and checkout the improvements branch:

   git clone https://github.com/Mrrobot-rx/algerian-sentiment.git
   cd algerian-sentiment
   git checkout improvements/algerian-sentiment

2. Create virtual environment and install:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

## Usage
- Inspect `scripts/` and `notebooks/` for preprocessing and training examples.

## Roadmap
- Add Dockerfile for reproducible training environments
- Add CI checks for linting and minimal training smoke tests
- Publish model to Hugging Face Hub

---

See CONTRIBUTING.md for how to contribute.
