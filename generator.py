'''
Project Starter Code
generator.py

functions to scrape and generate intermediate csv's we're working with

rn can scrape links to all huntnews articles and put in csv

need to make fn to go through csv with all links and
'''
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
from scraping import scrape_hunt_news_article

'''
file will be all about how to generate csv files given lists
or dictionaries, abstract from the scraping part of the stuff
this is all about making something we can work with later and look at later
'''

def hn_all_articles_on_page(link):
    '''
    Params: link (string, the link with http specified)
    Return: a list of strings
    Describe: returns a list of strings, with all the articles on that page in that list
    '''
    # for each searchresult class, find the first a tag  (after the h2 tag with class searchheadline)
    #  and pull out the link (href in it), set that as variable, add to list
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req)

    soup = BeautifulSoup(webpage, 'html.parser')

    #searchpageresults = soup.find('div', attrs={'class': 'searchpageresults'})
    #thing = soup.find('div', attrs={'class', 'searchresult'})
    #thing = seachpageresults.find_all('a')
    search_results = soup.find_all('div', attrs={'class': 'searchresult'})

    # for every a tag in 'searchresult' class, append that link to an initially
    #  empty list
    list_o_links = list()
    for val in search_results:
        a = val.find('a')
        some_link = a['href']
        list_o_links.append(some_link)
    # return that populated list
    return list_o_links

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

def make_csv_urls_only(list_o_search_pages):
  with open('all_hunt_news_articles_DATE.csv', mode='w', newline='') as file:
    all_articles_writer = csv.writer(file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
    all_articles_writer.writerow(['URLs'])

    for page_url in list_o_search_pages:
      this_page_links = hn_all_articles_on_page(page_url)
      for url in this_page_links:
        all_articles_writer.writerow([url])

def make_list_urls_only(list_o_search_pages):
  all_huntnews_urls = list()
  for page_url in list_o_search_pages:
    this_page_links = hn_all_articles_on_page(page_url)
    all_huntnews_urls = all_huntnews_urls + this_page_links # IS THIS HOW YOU APPEND LISTS TO EACH OTHER?
  return all_huntnews_urls


def generate_list_all_links():
  '''
  Returns: a list of all the urls of articles from huntington news
  WARNING, THIS HITS THE HUNTNEWSNU.com WEBSITE WITH THOUSANDS OF REQUESTS
  TRY SEEING IF THERE IS A CSV FILE WITH ALL THE ARTICLE LINKS EXISTING AND
  READ FROM THAT INSTEAD
  '''
  START = 1
  END = find_huntnews_last_page()
  MIDDLE = 'https://huntnewsnu.com/page/'
  POST = '/?s'
  HN_SEARCH = 'https://huntnewsnu.com/page/1/?s'

  # assemble list of search pages to trawl for links
  list_o_search_pages = list()
  for num in range(1, END + 1):
    linky = MIDDLE + str(num) + POST
    list_o_search_pages.append(linky)
  all_urls = make_list_urls_only(list_o_search_pages)
  return all_urls

def read_from_csv_list_all_links():
    '''
    Returns: a list of all the urls of articles from huntington news,
    read from a preexisting csv file
    '''
    all_links = list()
    with open('all_hunt_news_articles_March_6_2019.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        # skip the headers
        next(csv_reader, None)
        for row in csv_reader:
            url = row[0]
            all_links.append(url)
    return all_links

def generate_csv_all_links():
  '''
  Params:
  Return:
  Describe:
  '''
  # so we want a list of all of the huntnews search pages
  #  (so we can assemble a list of links to all articles
  #  in order of publication)
  START = 1
  END = find_huntnews_last_page()
  MIDDLE = 'https://huntnewsnu.com/page/'
  POST = '/?s'
  HN_SEARCH = 'https://huntnewsnu.com/page/1/?s'
  # assemble list of search pages to trawl for links
  list_o_search_pages = list()
  for num in range(1, END + 1):
      linky = MIDDLE + str(num) + POST
      list_o_search_pages.append(linky)
  make_csv_urls_only(list_o_search_pages)

def write_to_csv_list_o_urls(list_links):
    with open('scraped_articles_DATE.csv', encoding='utf-8', mode='w', newline='') as file:
        all_articles_writer = csv.writer(file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
        all_articles_writer.writerow(['URL',
                                      'Headline',
                                      'Byline',
                                      'Date',
                                      'Content'])
        for url_yo in list_links:
            headline, byline, date, content = scrape_hunt_news_article(url_yo)
            all_articles_writer.writerow([url_yo,
                                          headline,
                                          byline,
                                          date,
                                          content])
