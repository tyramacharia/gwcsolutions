import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def get_filtered_dictionary(tweet_blob): #this function will take a text blob and create a filtered dictionary of valid words
    words_to_filter = ["about", "https", "in", "the", "thing", "will", "could", "automation"]
    filtered_dictionary = dict()

    for word in tweet_blob.words:
        if len(word) < 2:
            continue
        if not word.isalpha():
            continue
        if word.lower() in words_to_filter:
            continue
        if len(word) < 5 and word.upper() != word:
            continue;

        filtered_dictionary[word.lower()] = tweet_blob.word_counts[word.lower()]

    return filtered_dictionary

#open, load, then close the json file
tweet_file = open("twitter_data.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

#create one large string of the texts of every tweet
combined_tweets = ""
for tweet in tweet_data:
	combined_tweets += tweet['text']

#save the combined tweets string as a textblob
tweet_blob = TextBlob(combined_tweets)

#create a new word cloud from filtered dictionary
word_cloud = WordCloud().generate_from_frequencies(get_filtered_dictionary(tweet_blob))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.figure(1)
plt.show()
