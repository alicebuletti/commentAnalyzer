# Comment Analyser

Ces scripts permettent de recuperer des commentaires depuis IMDB et de les analyser avec spacy et gcloud.

## Pour récupérer les commentaires avec NodeJS

Installer les dépendances du package.json
```
npm install
```

```
node index.js > data/you-newest-23-02-24.json
node index.js > data/you-oldest-23-02-24.json
node index.js > data/monster-oldest-23-02-24.json
node index.js > data/monster-newest-23-02-24.json
node index.js > data/you-featured-26-02-24.json
node index.js > data/monster-featured-26-02-24.json
```

## Pour analyser les commentaires et extraire les 100 mots les plus frequents avec Python

Installer spacy

```
pip3 install spacy
```

Telecharger le NLP pipeline

```
python3 -m spacy download en_core_web_trf
python3 -m spacy download en_core_web_sm
```

Lancer l'analyse des mots les plus frequents

```
python3 analyze.py monster
python3 analyze.py you
```

## Pour analyser les sentiments avec gcloud

Initialiser GCloud et s'authentifier
```
gcloud init
gcloud auth application-default login
```

```
python3 analyze_sentiment.py monster
python3 analyze_sentiment.py you
```
