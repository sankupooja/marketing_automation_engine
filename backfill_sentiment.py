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
    
    for row in missing_data:
        headline_id, title = row
        # 2. Calculate sentiment
        sentiment = analyzer.get_sentiment(title)
        
        # 3. Update the database
        cursor.execute(
            "UPDATE headlines SET sentiment = ? WHERE id = ?", 
            (sentiment, headline_id)
        )
        print(f"Updated ID {headline_id} with sentiment {sentiment}")
        
    conn.commit()
    conn.close()
    print("Backfill complete!")

if __name__ == "__main__":
    run_backfill()