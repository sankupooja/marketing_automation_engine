# from textblob import TextBlob


# def get_sentiment(text: str) -> float:
#     return TextBlob(text).sentiment.polarity

from transformers import pipeline

# Load the sentiment analysis pipeline
# This automatically downloads a pre-trained model fine-tuned for sentiment
analyzer = pipeline("sentiment-analysis",model="ProsusAI/finbert")

# analyzer.py
def get_sentiments(titles_list):

    #Safety check :if list is empty, return an empty list
    if not titles_list:
        return []
    # Pass the whole list to the pipeline for parallel processing
    results = analyzer(titles_list)
    print(f"DEBUG: Model raw output: {results[0]}")
    scores = []
    for res in results:
        #Finbert labels usualy are 'positive', 'negative', and 'neutral'
        label = res['label'].lower()
        score = res['score']
        
        if label == 'positive':
            scores.append(score)
        elif label == 'negative':
            scores.append(-score)
        else: # This handles 'neutral'
            scores.append(0.0)
    return scores