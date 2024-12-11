import json
import argparse

# Executer le fichier
# ~ : python3 analyse_sentiment.py [you, monster]

# Recuperer l'argument pour determiner le show à analyser. 
parser = argparse.ArgumentParser(description='Program options')
parser.add_argument('show', type=str, help='The show to analyse : [monster,you]')
args = parser.parse_args()

if args.show not in ('monster', 'you'):
    parser.error("Please specify the show name [monster,you]")

# Le show à analyser
show = args.show

##################################################################
############## Load all data from JSON files #####################
##################################################################
from functions.dataLoader import getAllTexts

# Tous les commentaires dans un tableau
data = getAllTexts(show)

##################################################################
############## Text concatenation ################################
##################################################################
# Remove duplicates and concatenate review text 
# into a single large text (all_texts) for word common extraction
max_reviews_to_parse = 1000
all_ids = []
i = 0
unique_ids = 0;
all_unique_reviews = []
for review in data:
    if i < max_reviews_to_parse: # memory limit
        # Only add text to all_texts if we haven't already stored the id inside all_ids
        if(review['id'] not in all_ids):
            unique_ids += 1
            all_ids.append(review['id'])
            all_unique_reviews.append(review)
        i = i + 1

print(str(unique_ids) + ' unique reviews on ' + show)


from functions.sentiment import analyze_sentiment

allResponses = []

for unique_review in all_unique_reviews:
    response = analyze_sentiment(unique_review['id'], unique_review['text'], unique_review['starRating'])
    allResponses.append(response)

with open("data/sentiment-"+show+".json", "w") as file:
    file.write(json.dumps(allResponses, indent=4))
