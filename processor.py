import glob
import json
import os

import db_manager

keywords_to_track = ["AI", "Marketing", "Business", "social media"]


def main() -> None:
    db_manager.init_db()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    headline_files = glob.glob(os.path.join(script_dir, "headlines_*.json"))

    if not headline_files:
        print("No headlines_*.json files found.")
        return

    latest_file = max(headline_files, key=os.path.getctime)
    print(f"Processing: {os.path.basename(latest_file)}")

    with open(latest_file, encoding="utf-8") as f:
        headlines = json.load(f)

    inserted_count = 0
    for headline in headlines:
        title = headline["title"]
        if any(keyword.lower() in title.lower() for keyword in keywords_to_track):
            db_manager.insert_headline(title=title, source=headline["link"])
            inserted_count += 1

    print(f"Inserted {inserted_count} headline(s) into headlines.db")


if __name__ == "__main__":
    main()
