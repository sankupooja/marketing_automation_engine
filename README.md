# AI-Powered Marketing Automation Engine

## Overview
A high-performance data pipeline designed to ingest, validate, and analyze market news headlines in real-time. The system has evolved from simple rule-based heuristics to a sophisticated AI-driven architecture utilizing Transformer-based models for contextual sentiment analysis.

## Pipeline Optimization & Architecture Refinement

### Key Achievements
* **Transformer-Based Sentiment Intelligence:** Transitioned from basic polarity metrics to state-of-the-art contextual analysis using FinBERT.
* **Vectorized Batch Inference:** Implemented high-performance batch processing for reduced latency.
* **High-Efficiency Data Lifecycle:**
    * **Batch Database Operations:** Upgraded from row-by-row commits to `executemany()`.
    * **Automated Backfilling:** Added a robust utility to enrich historical records.
* **Robust Data Integrity:** Maintained a strict `validate_data()` layer.
* **Performance Engineering:** Managed model weight caching for local hardware optimization.

## System Architecture Evolution

| Stage | Capability |
| :--- | :--- |
| **Ingestion** | Harvester reads raw data from diverse sources. |
| **Validation** | Data types and null-checks enforced via `validate_data()`. |
| **Enrichment** | FinBERT Transformer model generates sentiment scores. |
| **Processing** | Vectorized batch inference for throughput. |
| **Storage** | Transactional bulk insertion into SQLite. |

## Technical Highlights
* **NLP Pipeline:** Integration of `transformers` for modular model management.
* **Database Design:** Normalized schema with support for batch updates.
* **Development Workflow:** Dedicated scripts for backfilling and data inspection.
* **Environment Optimization:** Managed dependencies for large model weight caching.

## Getting Started
1. **Run Harvest:** `python harvester.py`
2. **Process Data:** `python processor.py`
3. **Backfill History:** `python backfill_sentiment.py`
4. **Inspect Database:** `python view_data.py`
