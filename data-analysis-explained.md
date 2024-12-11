# NLP ANALYSIS

USING model en_core_web_trf for accuracy

# nlp = spacy.load("en_core_web_sm") # efficiency
nlp = spacy.load("en_core_web_trf") #accuracy

(token, nb of ocurrences) 

## Only tokenization:

750 reviews on monster
557 unique reviews on monster
``` python
[
    ('the', 5747),
    ('.', 5323),
    (',', 4163),
    ('and', 3155),
    ('of', 2583),
    ('to', 2540),
    ('a', 2326),
    ('it', 2019),
    ('i', 1979),
    ('is', 1669),
    ('this', 1590),
    ('that', 1422),
    ('was', 1414),
    ('in', 1351),
    ("'s", 1111),
    ('dahmer', 1099),
    ('but', 889),
    ('his', 866),
    ('for', 836),
    ('he', 779)
]
```

750 reviews on you
653 unique reviews on you
``` python
[
    ('.', 4331),
    ('the', 3862),
    (',', 3020),
    ('and', 2458),
    ('a', 1988),
    ('to', 1935),
    ('i', 1923),
    ('it', 1661),
    ('is', 1565),
    ('of', 1526),
    ('in', 1030),
    ('that', 1022),
    ('season', 933),
    ('this', 926),
    ('was', 863),
    ("'s", 827),
    ('but', 813),
    ('you', 725),
    ('for', 663),
    ('with', 625)
 ]
```

## Token text vs lemmatization


### Token text (lowercased)
Token text for 20 most common words without stop words, only alpha and no punctuation
``` python
326 stop words 
750 reviews on you
653 unique reviews on you
[('season', 933), ('joe', 588), ('like', 413), ('series', 358), ('good', 311), ('love', 304), ('character', 262), ('characters', 221), ('watch', 214), ('story', 187), ('seasons', 174), ('beck', 174), ('people', 174), ('great', 171), ('way', 163), ('episode', 150), ('time', 147), ('watching', 146), ('think', 141), ('penn', 137)]

326 stop words 
750 reviews on monster
557 unique reviews on monster
[('dahmer', 1099), ('series', 737), ('story', 574), ('victims', 418), ('like', 382), ('peters', 352), ('evan', 324), ('people', 282), ('good', 274), ('jeffrey', 256), ('time', 253), ('watch', 252), ('episode', 239), ('serial', 235), ('way', 215), ('real', 210), ('families', 200), ('killer', 199), ('acting', 194), ('episodes', 193)]

```

### Token lemma_

Token lemma for 20 most common words without stop words, only alpha and no punctuation
``` python
326 stop words 
750 reviews on you
653 unique reviews on you
[('season', 1067), ('Joe', 549), ('character', 482), ('like', 472), ('watch', 444), ('good', 368), ('series', 345), ('love', 323), ('episode', 271), ('think', 229), ('go', 208), ('story', 195), ('get', 190), ('time', 186), ('great', 175), ('feel', 171), ('people', 170), ('end', 170), ('way', 169), ('Beck', 166)]

326 stop words 
750 reviews on monster
557 unique reviews on monster
[('Dahmer', 1048), ('series', 705), ('story', 579), ('watch', 517), ('victim', 513), ('episode', 430), ('like', 417), ('good', 365), ('time', 338), ('feel', 337), ('Peters', 328), ('Evan', 314), ('family', 288), ('know', 282), ('killer', 279), ('people', 272), ('Jeffrey', 249), ('life', 232), ('serial', 230), ('think', 229)]
```

## Remove verbs

100 most common tokens on Monster

``` python
326 stop words 
750 reviews on monster
557 unique reviews on monster
Remove VERB
[('Dahmer', 1048), ('series', 705), ('story', 579), ('victim', 513), ('episode', 430), ('good', 365), ('time', 338), ('Peters', 328), ('like', 321), ('Evan', 314), ('family', 288), ('killer', 279), ('people', 272), ('Jeffrey', 249), ('life', 232), ('serial', 230), ('way', 228), ('real', 210), ('thing', 209), ('crime', 196), ('great', 186), ('police', 185), ('acting', 182), ('character', 167), ('actor', 167), ('true', 166), ('Netflix', 153), ('performance', 147), ('scene', 144), ('man', 131), ('movie', 126), ('lot', 123), ('fact', 119), ('event', 113), ('job', 111), ('role', 111), ('bad', 105), ('amazing', 102), ('well', 102), ('point', 102), ('father', 100), ('year', 99), ('monster', 95), ('actually', 95), ('Murphy', 93), ('Jeff', 92), ('Glenda', 90), ('especially', 89), ('disturbing', 88), ('long', 84), ('away', 83), ('case', 82), ('Jenkins', 82), ('Ryan', 80), ('little', 78), ('detail', 78), ('person', 76), ('slow', 76), ('Richard', 75), ('neighbor', 75), ('horror', 72), ('interesting', 72), ('mind', 71), ('documentary', 71), ('kind', 71), ('white', 69), ('hard', 68), ('film', 68), ('Nash', 68), ('sure', 67), ('show', 66), ('cast', 65), ('right', 63), ('bit', 62), ('review', 61), ('different', 61), ('end', 60), ('murder', 60), ('black', 59), ('truly', 59), ('human', 58), ('overall', 58), ('tv', 58), ('racism', 58), ('day', 58), ('Story', 57), ('stuff', 56), ('far', 56), ('brilliant', 56), ('excellent', 55), ('Niecy', 55), ('parent', 54), ('work', 53), ('sick', 53), ('production', 53), ('horrible', 52), ('portrayal', 52), ('maybe', 52), ('evil', 50), ('entire', 50)]
```

100 most common tokens on You

``` python
326 stop words 
750 reviews on you
653 unique reviews on you
Remove VERB
[('season', 1067), ('Joe', 549), ('character', 482), ('good', 368), ('series', 345), ('like', 322), ('episode', 271), ('story', 195), ('time', 186), ('great', 175), ('people', 170), ('way', 169), ('Beck', 166), ('bad', 151), ('thing', 134), ('Penn', 134), ('plot', 125), ('book', 119), ('love', 116), ('main', 107), ('acting', 102), ('new', 102), ('well', 100), ('end', 89), ('girl', 89), ('writer', 88), ('Dexter', 87), ('Love', 86), ('interesting', 86), ('away', 81), ('guy', 79), ('second', 79), ('life', 75), ('show', 74), ('twist', 74), ('Netflix', 74), ('actor', 71), ('Badgley', 71), ('bit', 70), ('boring', 70), ('killer', 70), ('dark', 68), ('tv', 68), ('actually', 67), ('woman', 67), ('lot', 67), ('person', 66), ('point', 66), ('stalker', 63), ('writing', 63), ('little', 62), ('friend', 62), ('absolutely', 62), ('creepy', 60), ('far', 59), ('amazing', 58), ('pretty', 56), ('thriller', 55), ('definitely', 55), ('movie', 54), ('completely', 54), ('especially', 52), ('right', 52), ('day', 52), ('murder', 51), ('mind', 51), ('scene', 51), ('social', 50), ('kind', 50), ('annoying', 50), ('reason', 49), ('real', 49), ('review', 48), ('man', 47), ('different', 47), ('ending', 47), ('perfect', 46), ('viewer', 45), ('role', 44), ('maybe', 43), ('storyline', 43), ('sure', 42), ('psychopath', 42), ('relationship', 41), ('drama', 40), ('job', 40), ('long', 40), ('action', 39), ('not', 38), ('hard', 38), ('Season', 38), ('lead', 37), ('get', 37), ('audience', 37), ('worth', 36), ('joe', 35), ('idea', 35), ('overall', 35), ('sense', 35), ('big', 35)]
```

