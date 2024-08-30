import string
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import *
from csv import reader

# stemming tool from nltk
stemmer = PorterStemmer()
# a mapping dictionary that help remove punctuations
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
def text_to_unigrams(text):
  lowers = text.lower()
  no_punctuation = lowers.translate(remove_punctuation_map)
  tokens = nltk.word_tokenize(no_punctuation)
  filtered = [w for w in tokens if not w in stopwords.words('english')]
  stemmed = []
  for item in filtered:
    stemmed.append(stemmer.stem(item))
  return stemmed

if __name__ == "__main__":
  with open('24_train_2.csv', 'r', encoding='ISO-8859-1') as file:
    csv_reader = reader(file)
    
  with open('dictionary.txt', 'r') as file:
    word_set = set(word.strip() for word in file if word.strip())

  unigrams = {}
  for row in csv_reader:
    all_unigrams = text_to_unigrams(row[1])
    filtered_unigrams = [w for w in all_unigrams if w in word_set]
    
    # print(unigrams)