'''
Starter Code
driver.py
'''
from generator import read_from_csv_list_all_links, write_to_csv_list_o_urls

'''
file will be all about calling functions that are
defined in other files, our driver dontchaknow
starts them processes
'''

def main():
  '''
  Params:
  Return:
  Describe:
  '''
  print('main myperson')

  list_all_links = read_from_csv_list_all_links()

  write_to_csv_list_o_urls(list_all_links)

  # make a csv with the first 100 links in the csv and the scraped content
  #  from these links

  # row ,


main()
