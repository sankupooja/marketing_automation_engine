Day 3: Intelligence Enrichment & Data Migration
Objective: Transform raw, unstructured text into actionable intelligence by integrating Sentiment Analysis and performing safe database migrations.

Key Achievements:

Sentiment Integration: Successfully integrated TextBlob to calculate sentiment polarity scores for all incoming news headlines, allowing the system to categorize content by emotional intent (Positive vs. Neutral/Negative).

Data Enrichment Strategy: Expanded the SQLite schema to include a sentiment column, effectively transforming raw text data into quantitative intelligence.

Engineering Best Practice (The Backfill): Instead of destructive data clearing, implemented a backfill_sentiment.py migration script. This ensured historical data was preserved and retroactively updated with sentiment scores, maintaining 100% data integrity.

Pipeline Optimization: Updated the core processor to compute and persist sentiment scores in real-time, completing the move from simple ingestion to an AI-enriched data pipeline.

Technical Highlights:

NLP: Applied natural language processing techniques to extract sentiment values from headlines.

SQL Migrations: Executed non-destructive schema updates to manage evolving data requirements.

System Reliability: Ensured pipeline idempotency and data consistency through robust script-based maintenance utilities.


Day 4:
Recent Updates: Dashboard & Pipeline Enhancements
1. Data Integrity Improvements
Duplicate Handling: Integrated drop_duplicates("title", inplace=True) into the data loading pipeline to ensure that identical headlines are removed, preventing biased sentiment results.

Data Validation: Ensured that the captured_at column is correctly cast to datetime objects for accurate time-series manipulation.

2. Analytical Visualization
Daily Sentiment Aggregation: Shifted from raw point plotting to a more meaningful daily trend analysis. The dashboard now uses groupby with date resampling to calculate and visualize the average daily sentiment using st.line_chart.

3. On-Demand Pipeline Refresh
Interactive Updates: Added a "Refresh Data" button to the Streamlit UI. This allows users to trigger the harvester and processor pipelines directly from the browser.

Modular Integration: Refactored the dashboard to interface with backend modules, ensuring the database is updated with the latest data before the dashboard refreshes its view.
