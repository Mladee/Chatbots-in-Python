import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from poems import poems
from text_preprocessing import preprocess_text


processed_poems = [preprocess_text(poem) for poem in poems]

vectorizer = TfidfVectorizer(norm=None)
tfidf_scores = vectorizer.fit_transform(processed_poems)

corpus_index = [f"Poem {i+1}" for i in range(len(poems))]
feature_names = vectorizer.get_feature_names()
try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=corpus_index)
  print(df_tf_idf)
except:
  pass