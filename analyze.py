import argparse

# Script pour récupérer les 100 mots les plus frequents dans une collection de textes

# Exécuter le fichier
# ~ : python3 analyse.py [you, monster]

# Récupérer l'argument pour determiner le show à analyser. 
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
# Enlever doublons et concaténer tous les textes dans un large texte (all_texts) 
# pour extraire les mots les plus récurrents
max_reviews_to_parse = 1000
all_ids = []
i = 0
unique_ids = 0;
all_texts = ''
for review in data:
    if i < max_reviews_to_parse: # memory limit
        # Uniquement ajouter les textes qui ne sont pas déjà dans all_ids
        if(review['id'] not in all_ids):
            unique_ids += 1
            all_ids.append(review['id'])
            all_texts +=  ' ' + review['text']
        i = i + 1

print(str(unique_ids) + ' unique reviews on ' + show)


##################################################################
############## SPACY NLP model config ############################
##################################################################
import spacy
# Load le pipeline NLP à utiliser.
# nlp = spacy.load("en_core_web_sm") # efficiency - faster
nlp = spacy.load("en_core_web_trf") #accuracy - slower

# Utiliser la pipeline NLP pour la lemmatisation,
# part-of-speech detection (pos_) et detection des stop_words
complete_text = nlp(all_texts)

# Garder les lemma
# Enlever les chiffres
print('Remove: NON ALPHA')
# Enlever les stop_words 
print('Remove: STOP_WORDS')
# Enlever la ponctuation
print('Remove: PUNCT')
# Enlever les verbes
print('Remove: VERB')

words = [
    token.lemma_
    for token in complete_text
    if token.is_alpha
    and not token.is_stop
    and not token.is_punct
    and token.pos_ != "VERB"
]


##################################################################
############## Counting words ####################################
##################################################################
# Récupérer les 100 mots les plus récurrents

from collections import Counter

print(Counter(words).most_common(100))
