from wordcloud2_specific_author import *

data_source = 'scraped_articles_DATE.csv'
'''

line_number = int(input('Enter line number of article you want to see content of: '))
specified_article = get_content_at_line(line_number)
print(specified_article)


start_line = int(input('Enter start line number of articles we want the content for: '))
end_line = int(input('Enter end line number of articles we want the content for (inclusive): '))
all_those_lines_contents = multiple_lines(start_line, end_line, data_source)


author_name = input('Which author')
article_by_author = get_discography(author_name, data_source)
'''

fake_string = """How much a dollar really cost?
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
               
do_wordcloud(fake_string)
