import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

""" Initializing nltk downloads """
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

def basic_text_pipeline(user_input):
    """
    Implements the five steps of the basic text preprocessing pipeline:
    Tokenization, Normalization, Stop Word Removal, and Lemmatization.
    """

    # 1. Input Acquisition (The input is passed as 'user_input')
    print(f"Original Input: '{user_input}'")

    # 2. Tokenization: Split the string into individual words/tokens
    # Punctuation (like the comma) is separated as its own token here.
    tokens = word_tokenize(user_input)
    print(f"Tokens: {tokens}")

    # Initialize Lemmatizer and Stop Words Set for efficiency
    #lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    # List to hold tokens after normalization and filtering
    cleaned_tokens = []

    for token in tokens:
        # 3. Normalization: Convert all tokens to lowercase
        normalized_token = token.lower()

        # We only process tokens that are alphanumeric (removes most punctuation)
        if normalized_token.isalnum():

            # 4. Stop Word Removal: Filter out common, non-essential words
            if normalized_token not in stop_words:
                # 5. Lemmatization: Reduce word to its base or root form
                # Lemmatize after stop word removal to save time
                #lemma = lemmatizer.lemmatize(normalized_token)
                lemma = WordNetLemmatizer().lemmatize(normalized_token)

                cleaned_tokens.append(lemma)

    # print(f"Processed Tokens (Cleaned): {cleaned_tokens}")
    return cleaned_tokens



example_command = "Move the robot forward by ten centimeters, and turn slowly."

# Run the pipeline
processed_result = basic_text_pipeline(example_command)

print("\n--- Final Output ---")
print(f"Final Tokens for Command Parsing: {processed_result}")
print("\n The output is a list of root words ready for command interpretation")