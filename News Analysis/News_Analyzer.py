import re
from nltk import word_tokenize
from collections import Counter
import gensim




News_script = "Vaccine distribution is ramping up in many countries, but with Covid-19 cases also climbing once again and the prospect of another surge of infections on the horizon, the world is in a race against time.Key to winning the race, experts say, is not only whether the vaccines will play a significant role in preventing serious illness from Covid-19, but also whether they can block people from spreading the virus.The ideal vaccine would have two performance features: One prevents you from going to the hospital, going to the ICU and losing your life,said Dr. Peter Hotez, co-director of the Center for Vaccine Development at Texas Children’s Hospital and dean of the National School of Tropical Medicine at Baylor College of Medicine.But if the vaccine also halts asymptomatic spread, then you could potentially vaccinate your way out of the epidemic.Early indications have been promising so far. The effect of vaccines on asymptomatic infection had been a big unknown, but scientists say it will be crucial to ending the pandemic.'s estimated that asymptomatic cases, which involve people who are infected with Covid-19 but have no symptoms, account for more than half of all transmissions of the virus, according to a recent study published in the journal JAMA Network Open by researchers at the Centers for Disease Control and Prevention. If vaccines can block asymptomatic infections, they could also significantly reduce overall transmission, offering hope that the virus may soon be contained.Vaccines can protect against transmission by reducing a person's viral load, or how much virus is present in the body, said Dr. Becky Smith, an associate professor of medicine at Duke University.Theoretically, by reducing your viral load, it should prevent your ability to transmit to others she said.And even if it doesn't fully prevent transmission, it should lower it significantly.The focus on vaccines and transmission comes at an important juncture in the pandemic. Although cases globally fell for several weeks, some European countries are now seeing rebounds. Parts of the U.S. are also reporting upticks, a worrisome development given that many states recently relaxed public health restrictionsConcerns about coronavirus variants, including strains that may be more contagious, also persist. The government's top infectious disease expert, Dr. Anthony Fauci, director of the National Institute of Allergy and Infectious Diseases, told NBC News' Richard Engel on Thursday that the U.S. needs to vaccinate as many people as possible to avoid further outbreaks.Part of that strategy hinges on the effect vaccine could have on reducing transmission."
News = word_tokenize(str(News_script))
News_model = gensim.models.Word2Vec(" ".join(News),size = 100 ,window =5,min_count = 1,workers = 2,sg = 1)
print(News_model)

News_vocab = list(News_model.wv.vocab.items())
print(News_vocab)
'''
News_most_similar = News_model.most_similar('19',topn = 20)
print(News_most_similar)
'''