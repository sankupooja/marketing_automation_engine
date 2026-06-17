import sqlite3
import db_manager
import analyzer

def run_backfill():
    conn = sqlite3.connect(db_manager.get_db_path())
    cursor = conn.cursor()
    
    # 1. Find all records with no sentiment
    cursor.execute("SELECT id, title FROM headlines WHERE sentiment IS NULL")
    missing_data = cursor.fetchall()
    
    print(f"Found {len(missing_data)} rows to backfill...")

    # 2. Extract IDs and Titles for batch processing
    ids = [row[0] for row in missing_data]
    titles = [row[1] for row in missing_data]
    
    # 3. Calculate batch sentiments using our new analyzer function
    sentiments = analyzer.get_sentiments(titles)
    
    # 4. Prepare data for bulk update
    # Create a list of tuples: (sentiment, id)
    update_data = list(zip(sentiments, ids))
    
    # 5. Execute batch update
    cursor.executemany(
        "UPDATE headlines SET sentiment = ? WHERE id = ?", 
        update_data
    )
    
        
    conn.commit()
    conn.close()
    print("Backfill complete!")

if __name__ == "__main__":
    run_backfill()