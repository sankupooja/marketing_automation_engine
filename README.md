 Pipeline Optimization & Architecture RefinementObjective: Enhance data throughput and system scalability by transitioning to vectorized processing and batch database operations.
 
 Key Achievements:
 Vectorized Data Processing: Refactored the core processor.py logic to replace iterative loops with Pandas vectorized filtering (str.contains). This significantly improves performance when scaling to larger headline datasets.
 High-Efficiency Batch Insertion: Replaced row-by-row database writes with cursor.executemany(). This reduction in database I/O transactions drastically decreases processing latency.
 Automated Metadata Management: Streamlined the data insertion process by offloading captured_at timestamp generation to the database layer using SQL's datetime('now'), ensuring perfect synchronization and cleaner code.
 Robust Data Validation Layer: Introduced a strict validate_data() function to the pipeline. This ensures that only high-quality data—validated for type correctness, missing values, and logical range constraints—reaches the database.
 
 Technical Highlights:
 Performance Engineering: Shifted from high-latency iterative tasks to high-performance batch operations.
 Database Best Practices: Employed transaction-based bulk commits to maintain ACID compliance while maximizing insertion speed.
 Data Integrity: Implemented a pre-insertion validation layer that enforces strict schema and data quality requirements.
 Git Lifecycle Management: Established a robust development workflow using branching and git stash to manage experimental performance optimizations without disrupting the production codebase.
 
 Summary of System 
 Evolution
 StageCapability
 Ingestion   Harvester reads raw JSON files.
 Validation  Data types cleaned, ranges verified, duplicates removed.
 Enrichment  Sentiment polarity calculated via NLP.
 Processing  Vectorized keyword filtering.
 StorageBatch insertion with server-side timestamping.
