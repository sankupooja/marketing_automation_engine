# AI-Powered Marketing Automation Engine

## Project Evolution Overview
The system has matured from a basic data collection script into a sophisticated, AI-driven intelligence pipeline featuring real-time sentiment analysis, robust data integrity controls, and an interactive analytical dashboard.

---

## Intelligence Enrichment & Data Migration (Day 3)
* **Sentiment Integration:** Integrated NLP capabilities to calculate sentiment polarity scores, enabling the system to categorize headlines by emotional intent (Positive vs. Neutral/Negative).
* **Data Enrichment Strategy:** Expanded the SQLite schema to include a `sentiment` column, successfully transforming raw text data into quantitative intelligence.
* **Engineering Best Practice (The Backfill):** Implemented a non-destructive `backfill_sentiment.py` migration script, ensuring historical data was preserved and retroactively updated with sentiment scores while maintaining 100% data integrity.
* **Pipeline Optimization:** Updated the core processor to compute and persist sentiment scores in real-time.

## Dashboard & Pipeline Enhancements (Day 4)
* **Data Integrity Improvements:**
    * **Duplicate Handling:** Integrated `drop_duplicates("title", inplace=True)` to prevent biased sentiment reporting caused by repetitive news.
    * **Validation:** Enforced accurate data casting for `captured_at` timestamps to enable reliable time-series analysis.
* **Analytical Visualization:** Shifted from raw data plotting to meaningful daily trend analysis. The dashboard now employs `groupby` and date resampling to visualize average daily sentiment trends.
* **On-Demand Pipeline Refresh:** Added a "Refresh Data" button to the Streamlit UI, enabling users to trigger the `harvester` and `processor` pipelines directly from the browser for immediate updates.
* **Modular Integration:** Refactored the dashboard to interface directly with backend modules, ensuring the database is synchronized before view refreshes.

---

## Technical Highlights
* **NLP & Intelligence:** Applied NLP techniques to extract sentiment values, providing context to raw headlines.
* **SQL Migrations:** Executed non-destructive schema updates to manage evolving data requirements without data loss.
* **System Reliability:** Ensured pipeline idempotency and data consistency through automated maintenance utilities.
* **Interactive UI:** Built a responsive Streamlit dashboard with real-time refresh capabilities and automated trend aggregation.

## System Architecture Evolution

| Stage | Capability |
| :--- | :--- |
| **Ingestion** | Harvester reads raw JSON data from diverse sources. |
| **Validation** | Duplicate removal and strict data type casting enforced. |
| **Enrichment** | Sentiment polarity calculated via NLP models. |
| **Processing** | Vectorized keyword filtering and daily trend aggregation. |
| **Storage** | Transactional batch insertion with historical backfill support. |
| **Presentation** | Interactive Streamlit dashboard with live pipeline triggering. |

---
*Built for scale, precision, and performance.*
