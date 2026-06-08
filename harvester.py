import datetime
import json
import os

import feedparser

FEED_URL = "https://news.ycombinator.com/rss"
MAX_HEADLINES = 5


def main() -> None:
    feed = feedparser.parse(FEED_URL)

    headlines_data = []
    for entry in feed.entries[:MAX_HEADLINES]:
        headlines_data.append({"title": entry.title, "link": entry.link})

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        f"headlines_{timestamp}.json",
    )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(headlines_data, f, indent=2)


if __name__ == "__main__":
    main()
