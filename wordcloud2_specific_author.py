
# importing the necessery modules 
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import csv

data_source = 'scraped_articles_DATE.csv'

COMMON_STOPWORDS = ["the", "and","but", "if", "to", "of", "at", "with",
                       "we", "it", "on", "in", "from", "for", "her", "him",
                       "up", "just", "had", "they", "that", "said", "got", "did",
                       "really", "their", "or", "who", "is", "its", "be", "am", "are"
                       "was", "about", "so", "also", "this", "you", "would", "she", 
                       "could", "can", "he", "has", "do"]


def get_content_at_line(line):
    '''
    Returns: a list of all the urls of articles from huntington news,
    read from a preexisting csv file
    '''
    text = ''
    with open('scraped_articles_DATE.csv', encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file)
        
        # skip the headers
        next(csv_reader, None)

        counter = 2
        for row in csv_reader:
            url = row[0]
            headline = row[1]
            byline = row[2]
            date = row[3]
            content = row[4]

            if counter == line:
                return content
            
            counter += 1
    return ''



def get_discography(author):
    '''
    Returns: a list of all the urls of articles from huntington news,
    read from a preexisting csv file
    '''
    text = ''
    with open('scraped_articles_DATE.csv', encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file)
        
        # skip the headers
        next(csv_reader, None)

        temporary = ''

        for row in csv_reader:
            url = row[0]
            headline = row[1]
            byline = row[2]
            date = row[3]
            content = row[4]

            if author.lower() in byline.lower():
                temporary += content

    return temporary




def multiple_lines(start, end, csv_name):
    '''
    Returns: a list of all the urls of articles from huntington news,
    read from a preexisting csv file
    '''
    text = ''
    with open(csv_name, encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file)
        
        # skip the headers
        next(csv_reader, None)

        temporary = ''
        counter = 2
        selected = False
        for row in csv_reader:
            url = row[0]
            headline = row[1]
            byline = row[2]
            date = row[3]
            content = row[4]

            if counter == start:
                selected = True
                print('counter', counter)

            if selected == True:
                temporary += content
                print('count', counter)

            if counter == end:
                selected = False


            counter += 1
                
    return temporary


def do_wordcloud(wordswordswords):
    wordcloud = WordCloud(width=480, height=480, 
            stopwords = COMMON_STOPWORDS).generate(wordswordswords)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    
    
#Uncomment the appropriate chunk of code as well as the plt function at the end in order to generate word-cloud
    
'''
line = int(input('Which line? '))
article = get_content_at_line(line)
wordcloud = WordCloud(width=480, height=480, 
            stopwords = COMMON_STOPWORDS).generate(article)
'''

'''
#author = input('Which author? ')
#one_author = get_discography(author).lower()
#wordcloud = WordCloud(width=480, height=480, 
            #stopwords = COMMON_STOPWORDS).generate(one_author)
'''

'''
start = int(input('Enter start: '))
end = int(input('Enter end: '))

section = multiple_lines(start, end, data_source).lower()

wordcloud = WordCloud(width=480, height=480, 
            stopwords = COMMON_STOPWORDS).generate(section)
'''

'''
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show()
'''
