import glob
import json
import os

import analyzer
import db_manager
import pandas as pd

keywords_to_track = ["AI", "Marketing", "Business", "social media"]


def main() -> None:
    db_manager.init_db() # Initialize the database

    script_dir = os.path.dirname(os.path.abspath(__file__))
    headline_files = glob.glob(os.path.join(script_dir, "headlines_*.json")) # Get the latest headlines file

    if not headline_files: # If no headlines files are found, print an error message and return
        print("No headlines_*.json files found.")
        return
    
    latest_file = max(headline_files, key=os.path.getctime) # Get the latest headlines file
    print(f"Processing: {os.path.basename(latest_file)}") # Print the latest headlines file

    with open(latest_file, encoding="utf-8") as f:
        headlines = json.load(f) # Load the headlines from the latest file

    inserted_count = 0
    df = pd.DataFrame(headlines) # Create a dataframe from the headlines
     
    # # Get the sentiment of the headlines
    titles_list = df['title'].tolist() # Convert the titles to a list
    df['sentiment'] = analyzer.get_sentiments(titles_list) # Get the sentiment of the headlines using the pipeline

    df = validate_data(df) # Validate the dataframe

    # Create a pattern string that looks for any of our keywords
    pattern = '|'.join(keywords_to_track)

    # Filter the DataFrame to only include rows that match the pattern
    filtered_df = df[df['title'].str.contains(pattern, case=False, na=False)]
    # Create a list of tuples from the filtered dataframe
    data_list=list(filtered_df[['title', 'link', 'sentiment']].itertuples(index=False, name=None))

    if data_list:
        db_manager.insert_many_headlines(data_list) # Insert the headlines into the database
        print(f"Inserted {len(data_list)} headline(s) into headlines.db") # Print the number of headlines inserted into the database
    else:
        print("No headlines to insert") # Print a message if no headlines are found

def validate_data(df):
    """Clean and validate the dataframe before database insertion."""
    
    # 1. Drop rows where essential info is missing
    df = df.dropna(subset=['title', 'sentiment'])
    
    # 2. Ensure sentiment is numeric and drop rows that couldn't be converted
    df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')
    df = df.dropna(subset=['sentiment'])
    
    # 3. Filter for logical sentiment range (-1.0 to 1.0)
    df = df[(df['sentiment'] >= -1.0) & (df['sentiment'] <= 1.0)]
    
    return df
 

if __name__ == "__main__":
    main()
