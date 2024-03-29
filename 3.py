import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

text = "The quick brown foxes jumped over the lazy dogs."
tokens = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token, pos='v') for token in tokens]  # Specify 'v' for verb
print("Original Tokens:", tokens)
print("Lemmatized Tokens:", lemmatized_tokens)
