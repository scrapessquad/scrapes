'''
Bradley Fargo
sentiment_analysis.py

installing nltk might be necessary (it doesn't come default with python yo)
Check these instructions to do that: https://www.nltk.org/install.html

Also, on their website they say
"
If you publish work that uses NLTK, please cite the NLTK book as follows:

Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing
with Python. O’Reilly Media Inc.
"

'
should run:
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
as needed

also make sure you ran 'pip install afinn' at some point in cmd line
'

'''
import nltk
from afinn import Afinn

def demonstrate_nltk(some_string):
    '''
    Params: some_string
    Return: nothing
    Describe: prints out a tokenization (ie string converted to list of
        substrings, elimating spaces, so it's just a list of words and
        punctuation marks)
    '''
    tokenized_corpus = nltk.word_tokenize(some_string)
    print('Tokenized version of \n "' + some_string + '"\nis:\n', tokenized_corpus)

def get_corpus(input_string, list_o_search_words, spread):
    '''
    Params: input_string (the input to retrieve a list of words from),
        list_o_search_words (the list of words to search for within that string),
        spread (an int, the amount of words to include from around a
            searched for word)
    Return: A list of strings (that represents the words searched for and the
        words surrounding in both directions in the amount specified by spread,
        words pulled from input_string)
    Describe: Searches input_string (via nltk tokenization) for specific words,
        returns the words searched for and the words surrounding them to the
        amount specified by spread
    '''

    # using nltk to make this string a list of strings with no spaces
    tokenized_corpus = nltk.word_tokenize(input_string)

    list_index = []
    final_list = []

    # for loop to populate list_index with indexes of searched words
    for idx in range(len(tokenized_corpus)):
        boolin = False
        for search_word in list_o_search_words:
            boolin = boolin or \
                     search_word.lower() == tokenized_corpus[idx].lower()
        if boolin:
            list_index.append(idx)


    final_list = expandFromIndices(list_index, spread)

    print('List_index', list_index)
    print('Final_list', final_list)

    # populate the list of (possibly repeating) words we will return
    word_list = []
    for idx in final_list:
        if idx < len(tokenized_corpus) and idx > -1:
            word_list.append(tokenized_corpus[idx])

    return word_list

def expandFromIndices(list_o_indices, amount_spread):
    '''
    Params: list_o_indices (the list representing the indices of the located
        search words)
        amount_spread (int, amount to spread in both directions (0 to large num)
    Returns: the list of new indices (a list of of the old indices, plus the new
        ones added according to the spread value, so that no indice occurs more
        than once
    Describe: this is the function that actually 'spreads' the view we have on
        the searched words to include the words next to the searched words
    '''
    set_indices = set(list_o_indices)
    print('Set_indices', set_indices)

    new_indices = set(set_indices)

    for indice in set_indices:
        things_to_add = range(indice - amount_spread, indice + amount_spread + 1)
        for i in things_to_add:
            new_indices.add(i)
            
    return list(new_indices)
