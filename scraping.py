'''
Project Starter Code

scraping.py
'''
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

'''
what should be done ?

- collect (or define/pass in) list of urls to scrape
- for each url, perform an operation which visits that page and pulls out the useful materials, returns the stuff
    as variables
'''

'''
- tell python to get a certain thing from a specified link
- prepocess the content on that page (get rid of <p> tags)
- we want to end up with a list of words (so like spaces removed
['example', 'text', 'fun'] each word is individual string
- get rid of fluff words (using NLTK)
- put into wordcloud  -- piotr knows how
'''

def scrape_hunt_news_article(link):
    '''
    Params: link (a string starting with http or https that
        leads to a huntnews article), string
    Return: headline, byline, date, content (strings all)
    Describe: given a link, visits that link and attempts to scrape it
        assuming this is a hunt news article
    '''
    # if we just use urllib the website will be like
    #       'hold on there bot, get outta here, 403 error - Forbidden'
    # since we want to successfully make an http request, we make our own request
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    # query website to get html of that page, put it in our variable

    try:
        webpage = urlopen(req)
    except:
        print('Caught HTTPError')
        webpage = 'example'
        pass

    
    # we can use beautiful soup to work with this stuff
    # parse html using beaut soup, store in 'soup'
    soup = BeautifulSoup(webpage, 'html.parser')

    # take out the <div> of postarea and get it's value
    # this contains all the stuff we need, but it's a bit too much info
    post_area = soup.find('div', attrs={'class': 'postarea'})
    story_details = soup.find('div', attrs={'class': 'storydetails'})

    # so lets take out more specific elements
    story_date = soup.find('span', attrs={'class': 'storydate'})
    story_byline = soup.find('span', attrs={'class': 'storybyline'})
    story_content = soup.find('span', attrs={'class': 'storycontent'})
    story_headline = soup.find('h1', attrs={'class':'storyheadline'})
    ##permalinkphotobox = soup.find('div', attrs={'class':'permalinkphotobox'}) # this one isn't necessary, photo stuff
    # strip out unecessary stuff (span, p, a tags and the like)
    if story_date is None:
        date = ''
    else:
        date = story_date.text.strip()
    if story_byline is None:
        byline = ''
    else:
        byline = story_byline.text.strip()
    if story_content is None:
        content = ''
    else:
        content = story_content.text.strip()
    if story_headline is None:
        headline = ''
    else:
        headline = story_headline.text.strip()

    return headline, byline, date, content


def scrape_news_at_nu_article(link):
    '''
    Params: link (a string starting with http or https that
        leads to a huntnews article), string
    Return: headline, byline, date, content (strings all)
    Describe: given a link, visits that link and attempts to scrape it by
        as an article from news at northeastern
    '''
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    #
    webpage = urlopen(req)
    #
    soup = BeautifulSoup(webpage, 'html.parser')
    #
    article_topper = soup.find('section', attrs={'class': 'article-topper'})
    article_body = soup.find('div', attrs={'class': 'article-body'})

    print('Topper:\n', article_topper)
    print('Body:\n', article_body)
    return 'sup', 'sup', 'sup', 'sup'

def scrape_article(link):
    '''
    Params: link (a string starting with http or https that
        leads to a huntnews article), string
    Return: headline, byline, date, content (strings all)
    Describe: given a link, visits that link and attempts to scrape it by
        calling the appropriate helper function per publication
    '''
    if 'huntnewsnu.com' in link:
        return scrape_hunt_news_article(link)
    elif 'news.northeastern.edu' in link:
        return scrape_news_at_nu(link)

def hn_all_articles_on_page(link):
    '''
    Params: link (string, the link with http specified)
    Return: a list of strings
    Describe: returns a list of strings, with all the articles on that page in that list
    '''
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req)

    soup = BeautifulSoup(webpage, 'html.parser')

    #searchpageresults = soup.find('div', attrs={'class': 'searchpageresults'})
    #thing = soup.find('div', attrs={'class', 'searchresult'})
    #thing = seachpageresults.find_all('a')
    search_results = soup.find_all('div', attrs={'class': 'searchresult'})

    list_o_links = list()
    for val in search_results:
        a = val.find('a')
        some_link = a['href']
        list_o_links.append(some_link)

    return list_o_links
    # for each searchresult class, find the first a tag  (after the h2 tag with class searchheadline)
    #  and pull out the link (href in it), set that as variable, add to list


def find_huntnews_last_page():
    # this is just searching the pages of articles of hunt news with no actual
    # query, so it returns all articles in order of publication date
    link = 'https://huntnewsnu.com/page/1/?s'

    # tell the site we're using firefox
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    # open https request
    webpage = urlopen(req)
    # parse html we get back with beautiful soup
    soup = BeautifulSoup(webpage, 'html.parser')
    # pull out the nav bar at the bottom of the page (it shows the last page)
    nav = thing = soup.find('div', attrs={'class': 'navigation'})
    # pull out all list items in nav bar
    thing = nav.find_all('li')
    # remove the last element (preprocess data)
    thing = thing[:len(thing) - 1]
    # take the new last element (the number we're looking for get text)
    last_page = thing[len(thing) - 1].get_text()
    # that's the last page that exists, we return that number as an int
    return int(last_page)        

def main():
    # so we have a list of all of the huntnews search pages
    #  (so we can assemble a list of links to all articles
    #  in order of publication)
    START = 1
    END = find_huntnews_last_page()
    MIDDLE = 'https://huntnewsnu.com/page/'
    POST = '/?s'
    
    HN_SEARCH = 'https://huntnewsnu.com/page/1/?s'

    list_o_search_pages = list()
    
    for num in range(1, END + 1):
        linky = MIDDLE + str(num) + POST
        list_o_search_pages.append(linky)        
        

    with open('all_hunt_news_articles_March_6_2019.csv', mode='w', newline='') as file:
        all_articles_writer = csv.writer(file, delimiter=',', quotechar='"',
                                         quoting=csv.QUOTE_MINIMAL)
        all_articles_writer.writerow(['URLs'])

        for page_url in list_o_search_pages:
            this_page_links = hn_all_articles_on_page(page_url)
            for url in this_page_links:
                all_articles_writer.writerow([url])

    
        
    #print(list_o_search_pages)

    #list_o_links = hn_all_articles_on_page(HN_SEARCH)

    #for l in list_o_links:
    #    print(l)
    #print(thing.prettify())


def other():
    # what's the url?
    PROF_URL = 'https://huntnewsnu.com/58179/campus/columbia-professor-presents-the-blessings-of-multiple-causes-at-nu/'
    FRISKY_URL = 'https://huntnewsnu.com/58316/featured-content/frisky-husky-delivers-free-contraception-to-students/'
    
    # this next one is from news@northeastern
    SQUID_URL = 'https://news.northeastern.edu/2019/03/05/the-secret-of-squids-ability-to-change-colors-may-lie-in-an-unexpected-sparkle-on-its-skin/'
    
    input_link = ''
    while input_link == '':
        input_link = input('Please copy and paste a link to a specific hunt '
                           'news article (ie https://huntnewsnu.com/...../) '
                           'or enter 1 to select the prof one, and 2 to select '
                           'the frisky husky one.')
        if input_link == '1':
            input_link = PROF_URL
        if input_link == '2':
            input_link = FRISKY_URL
        if 'https://huntnewsnu.com/' not in input_link:
            input_link = ''
        
    headline, byline, date, content = scrape_article(input_link)
    
    print('INPUTTED STORY\n\n')
    print('Headline:\n', headline, '\n')
    print('Date:\n', date, '\n')
    print('Byline:\n', byline, '\n')
    print('Content:\n', content, '\n')  

# extra things that I didn't delete yet cause it might be convenient later

### now, we probably want some example data to work with (so we don't have to make
### an http request each time so I'm just gonna paste the data from the
### columbia professor presentation story into constants
##EX_HEADLINE = 'Columbia professor presents ‘The Blessings of Multiple Causes’ at NU'
##EX_DETAILS = 'February 27, 2019'
##EX_BYLINE = ' Nick Swindell, deputy campus editor '
##EX_CONTENT = ' Northeastern University’s Khoury College of Computer Sciences hosted David Blei, a professor of statistics and computer science at Columbia University, as a distinguished speaker Friday in a lecture titled “The Blessings of Multiple Causes.” Blei presented research done by himself and his Ph.D. student Yixin Wang on performing causal inference in multiple-cause scenarios using what he refers to as the “deconfounder.” Deconfounders are methods that determine the extent to which one thing is the cause of another using weaker assumptions than classical methods, and are relevant in fields like the social sciences where it is difficult to control for possible causes. Blei emphasized how complicated data is in the modern world.“We have people that connect to each other, that send messages to each other, they’re clicking on those messages et cetera et cetera, these are all ways data is [more] complicated than it was 20 years ago,” Blei said.Blei used data about movies to study causal effects of actors, like Meryl Streep affecting movie revenue. He showed that this question can take advantage of deconfounders because it is not a “classical causal problem” but one with multiple causes where an actor is only one possible factor.Blei said that his general field, probabilistic machine learning, builds methods that connect domain knowledge to data we collect about the world; that answers the question, “What does it mean to make sense of data?”“Traditionally in machine learning it means something about making a prediction about the future … most ambitiously we might want to do real science: confirm, elaborate or form causal theories,” Blei said. “Or put in plain English, I want to know how the world works based on this data. I want to ingest this data about Facebook and I want to understand something about how people connect and form relationships.”'
##
##print('Headline:\n', EX_HEADLINE, '\n')
##print('Details:\n', EX_DETAILS, '\n')
##print('Byline:\n', EX_BYLINE, '\n')
##print('Content:\n', EX_CONTENT, '\n')
