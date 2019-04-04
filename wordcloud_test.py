from wordcloud2_specific_author import *

fake = 'fake_csv_wordcloud.csv'

test1 = multiple_lines(3, 4, fake)
print('expected appearances (most to least often): fish, cat/turtle, dog, kitten')
do_wordcloud(test1)

test2 = multiple_lines(3, 5, fake)
print('expected appearances (most to least often): fish, cat/dog, turtle, bunny/kitten')
do_wordcloud(test2)
