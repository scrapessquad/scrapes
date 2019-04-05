'''
Starter Code
driver.py
'''
from generator import read_from_csv_list_all_links, write_to_csv_list_o_urls
from afinn import Afinn
import nltk
from sentiment_analysis import demonstrate_nltk, get_corpus, expandFromIndices
from scraping import scrape_hunt_news_article
# from wordcloud2_specific_author import *
import csv
'''
need to run
'pip install wordcloud'
to work properly
'''


'''
file will be all about calling functions that are
defined in other files, our driver dontchaknow
starts them processes
'''

def main():
  '''
  the function which specifies the things we want to run
  '''

  ''' This stuff: showing off the behavior of scrape_hunt_news_article when
    hits a 404 error (broken link)
    
  EXAMPLE_404_LINK = 'https://huntnewsnu.com/35970/lifestyle/event-calendar/35970/'
  string_to_print = scrape_hunt_news_article(EXAMPLE_404_LINK))
  print(string_to_print)
  '''

  ''' This Stuff: What I ran to construct the big CSV file from the
     may 6 scrape CSV file (with headline, byline, etc)

  list_all_links = read_from_csv_list_all_links()
  write_to_csv_list_o_urls(list_all_links)
  '''
  # print('Afinn stuff')
  afinn = Afinn()
  example_string = 'this is an example string'
  how_much_a_dollar_cost = """How much a dollar really cost?
The question is detrimental, paralyzin' my thoughts
Parasites in my stomach keep me with a gut feeling, y'all
Gotta see how I’m chillin' once I park this luxury car
Hopping out feeling big as Mutombo
20 on pump six dirty Marcellus called me Dumbo
20 years ago, can't forget
Now I can lend 'em a ear or two how to stack these residuals
Tenfold, the liberal concept of what men'll do
20 on 6, he didn't hear me
Indigenous African only spoke Zulu
My American tongue was slurry
Walked out the gas station
A homeless man with a silly tan complexion
Asked me for ten grand
Stressin' about dry land
Deep water, powder blue skies that crack open
A piece of crack that he wanted, I knew he was smokin'
He begged and pleaded
Asked me to feed him twice, I didn't believe it
Told him, "Beat it"
Contributin' money just for his pipe, I couldn't see it
He said, "My son, temptation is one thing that I've defeated
Listen to me, I want a single bill from you
Nothin' less, nothin' more
I told him I ain't have it and closed my door
Tell me how much a dollar cost
It's more to feed your mind
Water, sun and love, the one you love
All you need, the air you breathe
He's starin' at me in disbelief
My temper is buildin', he's starin' at me, I grab my key
He's starin' at me, I started the car and tried to leave
And somethin' told me to keep it in park until I could see
A reason why he was mad at a stranger like I was supposed to save him
Like I'm the reason he's homeless and askin' me for a favor
He's starin' at me, his eyes followed me with no laser
He's starin' at me, I notice that his stare is contagious
Cause now I'm starin' back at him, feelin' some type of disrespect
If I could throw a bat at him, it'd be aimin' at his neck
I never understood someone beggin' for goods
Askin' for handouts, takin' it if they could
And this particular person just had it down pat
Starin' at me for the longest until he finally asked
Have you ever opened to Exodus 14?
A humble man is all that we ever need
Tell me how much a dollar cost
It's more to feed your mind
Water, sun and love, the one you love
All you need, the air you breathe
Guilt trippin' and feelin' resentment
I never met a transient that demanded attention
They got me frustrated, indecisive and power trippin'
Sour emotions got me lookin' at the universe different
I should distance myself, I should keep it relentless
My selfishness is what got me here, who the fuck I'm kiddin'?
So I'ma tell you like I told the last bum, crumbs and pennies
I need all of mines, and I recognize this type of panhandlin' all the time
I got better judgement, I know when nigga's hustlin'
Keep in mind, when I was strugglin', I did compromise
Now I comprehend, I smell grandpa's old medicine
Reekin' from your skin, moonshine and gin
Nigga your babblin', your words ain't flatterin', I'm imaginin'
Denzel be lookin' at O'Neal
Cause now I'm in sad thrills, your gimmick is mediocre, the jig is up
I seen you from a mile away losin' focus
And I'm insensitive, and I lack empathy
You looked at me and said, "Your potential is bittersweet"
I looked at him and said, "Every nickel is mines to keep"
He looked at me and said, "Know the truth, it'll set you free
You're lookin' at the Messiah, the son of Jehova, the higher power
The choir that spoke the word, the Holy Spirit, the nerve
Of Nazareth, and I'll tell you just how much a dollar cost
The price of having a spot in Heaven, embrace your loss, I am God"
I wash my hands, I said my grace, what more do you want from me?
Tears of a clown, guess I'm not all what is meant to be
Shades of grey will never change if I condone
Turn this page, help me change, so right my wrongs"""

  # How does  afinn lexicon score the song how_much_a_dollar_cost?
  print(afinn.score(how_much_a_dollar_cost))

  # runs nltk functions on an example string
  demonstrate_nltk(example_string)

  # do get_corpus where we're searching for my from how_much_a_dollar_cost
  list_search_words = ['my']
  corpus_list = get_corpus(how_much_a_dollar_cost, list_search_words, 5)
  print('Words Pulled Out:', corpus_list)
##    corpus_string = corpus_list.join(" ")
  corpus_string = str.join(" ", corpus_list)

    # actually evaluate the corpus gathered for sentiment (negative is negative,
    # positive is positive
  print(afinn.score(corpus_string))

  print('OK So Let\'s do this to our actual data')


  # use the fn from other file
  before_corpus = multiple_lines(9025, 11881, 'scraped_articles_DATE.csv')
  after_corpus = multiple_lines(6939, 9024, 'scraped_articles_DATE.csv')

  search_words = ['Northeastern', 'Administration', 'Aoun']
  # get the words to score
  before_list = get_corpus(before_corpus, search_words, 5)
  after_list = get_corpus(after_corpus, search_words, 5)

  # print out the corpuses just to see
  print('The length of Before is:', len(before_list))
  print('The length of After is:', len(after_list))


  # turn these lists into strings with spaces in between each item
  before = " ".join(before_list)
  after = " ".join(after_list)

  # find the afinn positivity scores and print them out
  before_score = afinn.score(before)
  after_score = afinn.score(after)
  print('\nBefore Score:', before_score)
  print('\nAfter Score:', after_score)
  


#####
  #DUPLICATE CODE FROM ANOTHER FILE
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
  


main()
