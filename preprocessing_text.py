text = "The cat is in the box. The cat likes the box. The box is over the cat"

from nltk.corpus import stopwords
tokens  = [w  for w in word_tokenize(text.lower())
            if w.isalpha()] 
no_stops = [t for t in tokens
             if t  not in stopwords.words('english')]
