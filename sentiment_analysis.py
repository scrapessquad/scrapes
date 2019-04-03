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
'

'''
import nltk


def main():
    print('Great Success')

    example_string = 'this is an example string'

    tokens = nltk.word_tokenize(example_string)

    print('Tokenized version of', example_string, ':', tokens)

    list_index = []
    final_list

    for idx in range(len(tokens)):
        if tokens[idx].lower() == 'Northeastern'.lower() or
        tokens[idx].lower() == 'Administration'.lower() or
        tokens[idx].lower() == 'Aoun'.lower():
            list_index.append(idx)

    for index in list_index:
        if index not in 
            
        

    # so we give it a whole article. Then we tokenize the whole article.
    
    # Then we want to locate all the times in that article that 'Northeastern'
    # or 'Administration' or 'Aoun' appears. To store that data, we keep a
    # list of indexes of that string.
    # Then we pull out the 


main()
