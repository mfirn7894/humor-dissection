# This program analyzes two sets of Reddit jokes (top and new) along multiple
# dimensions in order to determine what makes a joke popular on a social Internet
# platform. The user will run my main functions in the interactive shell, calling
# allInfo() to receive all results for a joke set, or customInfo() to see only
# a specific result.


# Allows importation of Reddit data
import praw

# Allows use of regular expressions
import re

# Initialize Reddit API
r = praw.Reddit(client_id= # user input,
                     client_secret= # user input,
                     password= # user input,
                     user_agent= # user input,
                     username= # user input)
subreddit = r.subreddit('jokes')

# Specify number of jokes to analyze
numJokes = 30
'''NOTE: may retrieve 404 error if jokes from deleted users appear'''

# For top jokes, creates a dictionary in which keys = jokes (unicode) and
# values = [upvotes, number of comments] (list of integers)
'INPUTS: none'
'OUTPUTS: dict'
topCommentsList = []
topKarmaList = []
topScoreDict = {}
topJokeList = []
for submission in subreddit.top('all',limit=numJokes):
    topJokeList = topJokeList + [submission.selftext]
    topCommentsList = topCommentsList + [submission.num_comments]
    topKarmaList = topKarmaList + [submission.score]
    topScoreDict = dict.fromkeys(topJokeList,'')
    for index in range(0,len(topJokeList)):
        topScoreDict[topJokeList[index]]=[topKarmaList[index],topCommentsList[index]]


# For new jokes, creates a dictionary in which keys = jokes (unicode) and
# values = [upvotes, number of comments] (list of integers)
'INPUTS: none'
'OUTPUTS: dict'
newCommentsList = []
newKarmaList = []
newScoreDict = {}
newJokeList = []
for submission in subreddit.new(limit=numJokes):
    newJokeList = newJokeList + [submission.selftext]
    newCommentsList = newCommentsList + [submission.num_comments]
    newKarmaList = newKarmaList + [submission.score]
    newScoreDict = dict.fromkeys(newJokeList,'')
    for index in range(0,len(newJokeList)):
        newScoreDict[newJokeList[index]]=[newKarmaList[index],newCommentsList[index]]

        
# For top jokes, creates a dictionary in which keys = jokes (unicode) and
# values = title (unicode)
'INPUTS: none'
'OUTPUTS: dict'
topTitleList = []
topTitleDict = {}
topJokeList = []
for submission in subreddit.top('all',limit=numJokes):
    topJokeList = topJokeList + [submission.selftext]
    topTitleList = topTitleList + [submission.title]
    topTitleDict = dict.fromkeys(topJokeList,'')
    for index in range(0,len(topJokeList)):
        topTitleDict[topJokeList[index]]=topTitleList[index]

# For new jokes, creates a dictionary in which keys = jokes (unicode) and
# values = title (unicode)
newTitleList = []
newTitleDict = {}
newJokeList = []
'INPUTS: none'
'OUTPUTS: dict'
for submission in subreddit.new(limit=numJokes):
    newJokeList = newJokeList + [submission.selftext]
    newTitleList = newTitleList + [submission.title]
    newTitleDict = dict.fromkeys(newJokeList,'')
    for index in range(0,len(newJokeList)):
        newTitleDict[newJokeList[index]]=newTitleList[index]

# For top jokes, creates a dictionary in which keys = jokes (unicode) and values
# = over18? tag (boolean)
'INPUTS: none'
'OUTPUTS: dict'
topOver18List = []
topOver18Dict = {}
topJokeList = []
for submission in subreddit.top('all',limit=numJokes):
    topJokeList = topJokeList + [submission.selftext]
    topOver18List = topOver18List + [submission.over_18]
    topOver18Dict = dict.fromkeys(topJokeList,'')
    for index in range(0,len(topJokeList)):
        topOver18Dict[topJokeList[index]]=topOver18List[index]

# For new jokes, creates a dictionary in which keys = jokes (unicode) and values
# = over18? tag (boolean)
'INPUTS: none'
'OUTPUTS: dict'
newOver18List = []
newOver18Dict = {}
newJokeList = []
for submission in subreddit.new(limit=numJokes):
    newJokeList = newJokeList + [submission.selftext]
    newOver18List = newOver18List + [submission.over_18]
    newOver18Dict = dict.fromkeys(newJokeList,'')
    for index in range(0,len(newJokeList)):
        newOver18Dict[newJokeList[index]]=newOver18List[index]                                              

# For top jokes, creates a dictionary in which keys = jokes (unicode) and
# values = total karma of the poster (integer)
'INPUTS: none'
'OUTPUTS: dict'
topUserKarma = []
topUserKarmaDict = {}
topJokeList = []
for submission in subreddit.top('all',limit=numJokes):
    topJokeList = topJokeList + [submission.selftext]
    topUserKarma = topUserKarma + [submission.author.link_karma + submission.author.comment_karma]
    topUserKarmaDict = dict.fromkeys(topJokeList,'')
    for index in range(0,len(topJokeList)):
         topUserKarmaDict[topJokeList[index]]=topUserKarma[index]
    
# For new jokes, creates a dictionary in which keys = jokes (unicode) and
# values = total karma of the poster (integer)
'INPUTS: none'
'OUTPUTS: dict'
newUserKarma = []
newUserKarmaDict = {}
newJokeList = []
for submission in subreddit.new(limit=numJokes):
    newJokeList = newJokeList + [submission.selftext]
    newUserKarma = newUserKarma + [submission.author.link_karma + submission.author.comment_karma]
    newUserKarmaDict = dict.fromkeys(newJokeList,'')
    for index in range(0,len(newJokeList)):
         newUserKarmaDict[newJokeList[index]]=newUserKarma[index]
    
def allInfo(jokeSet):
# Takes a jokeSet (string) -- either 'top' or 'new' -- and returns outputs from
# the textual analysis functions defined below. This, along with interactiveInfo,
# is one of my main functions, and will be called by the user in the interactive
# shell.
    'INPUTS: string'
    'OUTPUTS: string'
    # string --> string
    if jokeSet == 'top':
        print 'Averages for top ' + str(numJokes) + ' jokes of all time:\n'
        print 'Karma: ' + str(avgValue(topScoreDict)[0])
        print 'Number of comments: ' + str(avgValue(topScoreDict)[1])
        print "User's total karma: " + str(avgValue(topUserKarmaDict))
        print 'Number of words in title: ' + str(avgValue(topTitleDict))
        print 'Number of words per joke: ' + str(avgLength(topScoreDict))
        print 'Character length of word: ' + str(avgWordLength(topScoreDict))
        print 'Percent NSFW: ' + str(avgValue(topOver18Dict)*100) + '%'
        print 'Ratio of unique words to total words: ' + str(uniqueRatio(topScoreDict))
        print 'Number of swears per joke: ' + str(profanityCount(topScoreDict))
        print 'Ten most frequent words (>3 char.): ' + str(wordFreq(topScoreDict))
    elif jokeSet == 'new':
        print 'Averages for ' + str(numJokes) + ' newest jokes:\n'
        print 'Karma: ' + str(avgValue(newScoreDict)[0])
        print 'Number of comments: ' + str(avgValue(newScoreDict)[1])
        print "User's total karma: " + str(avgValue(newUserKarmaDict))
        print 'Number of words in title: ' + str(avgValue(newTitleDict))
        print 'Number of words per joke: ' + str(avgLength(newScoreDict))
        print 'Character length of word: ' + str(avgWordLength(newScoreDict))
        print 'Percent NSFW: ' + str(avgValue(newOver18Dict)*100) + '%'
        print 'Ratio of unique words to total words: ' + str(uniqueRatio(newScoreDict))
        print 'Number of swears per joke: ' + str(profanityCount(newScoreDict))
        print 'Ten most frequent words (>3 char.): ' + str(wordFreq(newScoreDict))
    else:
        print "Error! Please input either 'top' for top jokes or 'new' for new jokes"


def customInfo(jokeSet):
# Takes a jokeSet (string) -- either 'top' or 'new' -- and returns whichever
# output (string) is specified by user input (via raw_input)
    'INPUTS: string'
    'OUTPUTS: string'
    # string --> string
    if jokeSet == 'top':
        function = raw_input("Which info set are you looking for? \n\n Karma \n Number of comments \n Number of words in title \n Percent NSFW \n User karma \n Character length of word \n Ratio of unique words to total words \n Swear count \n Most frequent words \n\n >>> ")
        if cleanUp(function) == 'karma':
            print 'Average karma: ' + str(avgValue(topScoreDict)[0])
        elif cleanUp(function) == 'number of comments':
            print 'Average number of comments: ' + str(avgValue(topScoreDict)[1])
        elif cleanUp(function) == 'number of words in title':
            print 'Average number of words in title: ' + str(avgValue(topTitleDict))
        elif cleanUp(function) == 'percent nsfw':
            print 'Percent NSFW: ' + str(avgValue(topOver18Dict)*100) + '%'
        elif cleanUp(function) == "user karma":
            print "Average user's total karma: " + str(avgValue(topUserKarmaDict))
        elif cleanUp(function) == 'number of words per joke':
            print 'Average number of words per joke: ' + str(avgLength(topScoreDict))
        elif cleanUp(function) == 'character length of word':
            print 'Average character length of word: ' + str(avgWordLength(topScoreDict))
        elif cleanUp(function) == 'ratio of unique words to total words':
            print 'Average ratio of unique words to total words: ' + str(uniqueRatio(topScoreDict))
        elif cleanUp(function) == 'swear count':
            print 'Average number of swears per joke: ' + str(profanityCount(topScoreDict))
        elif cleanUp(function) == 'most frequent words':
            print 'Ten most frequent words (>3 char.): ' + str(wordFreq(topScoreDict))
        else:
            print 'Error! Please input an info set that matches the exact keys in the list of options below (case insensitive)\n'
            customInfo('top')
    elif jokeSet == 'new':
        function = raw_input("Which info set are you looking for? \n\n Karma \n Number of comments \n Number of words in title \n Percent NSFW \n User karma \n Character length of word \n Ratio of unique words to total words \n Swear count \n Most frequent words \n\n >>> ")
        if cleanUp(function) == 'karma':
            print 'Average karma: ' + str(avgValue(newScoreDict)[0])
        elif cleanUp(function) == 'number of comments':
            print 'Average number of comments: ' + str(avgValue(newScoreDict)[1])
        elif cleanUp(function) == 'number of words in title':
            print 'Average number of words in title: ' + str(avgValue(newTitleDict))
        elif cleanUp(function) == 'percent NSFW':
            print 'Percent NSFW: ' + str(avgValue(newOver18Dict)*100) + '%'
        elif cleanUp(function) == "user karma":
            print "Average user's total karma: " + str(avgValue(newUserKarmaDict))
        elif cleanUp(function) == 'number of words per joke':
            print 'Average number of words per joke: ' + str(avgLength(newScoreDict))
        elif cleanUp(function) == 'character length of word':
            print 'Average character length of word: ' + str(avgWordLength(newScoreDict))
        elif cleanUp(function) == 'ratio of unique words to total words':
            print 'Average ratio of unique words to total words: ' + str(uniqueRatio(newScoreDict))
        elif cleanUp(function) == 'number of swears per joke':
            print 'Average number of swears per joke: ' + str(profanityCount(newScoreDict))
        elif cleanUp(function) == 'most frequent words':
            print 'Ten most frequent words (>3 char.): ' + str(wordFreq(newScoreDict))
        else:
            print 'Error! Please input an info set that matches the exact keys in the list of options below (case insensitive)\n'
            customInfo('new')
    else:
        print "Error! Please input either 'top' for top jokes or 'new' for new jokes"


def cleanUp(myString):
# Removes capital letters and punctuation from a string
    'INPUTS: string'
    'OUTPUTS: string'
    # string --> string
    cleanString = ''
    for char in myString:
        if(char=='.' or char==',' or char=='!' or char=='?' or char=='/'
            or char=='"' or char=='(' or char==')' or char=='$' or char=='#'
            or char=='%' or char=='-' or char=='+' or char==':' or char==';'):
                cleanString += ' '
        else:
            cleanString += char
    cleanString = cleanString.lower()
    return cleanString


def avgValue(myDict):
# For any dictionary created above, returns average data (specifics depend on
# the type of values)
    'INPUTS: dict'
    'OUTPUTS: float'
    # dict --> float
    for index in range(0,len(myDict)):
        # If values are a list of integers (e.g [karma, comments]), return a
        # list of average values of both indices
        if type(myDict.values()[0]) == list:
            myList = myDict.values()
            karma = 0
            comments = 0
            for index in range (0,len(myList)):
                subList = myList[index]
                karma = karma + subList[0]
                avgKarma = karma/float(len(myList))
                comments = comments + subList[1]
                avgComments = comments/float(len(myList))
            return [round(avgKarma,2),round(avgComments,2)]
        # If values are unicode (e.g. titles), return average number of words
        # in the values
        if type(myDict.values()[0]) == unicode:
            myList = myDict.values()
            title = 0
            for index in range(0,len(myList)):
                titleIndex = myList[index]
                splitIndex = titleIndex.split()
                title += len(splitIndex)
            return round((title/float(len(myList))),2)
        # If values are integers (e.g. user karma), return average value
        if type(myDict.values()[0]) == int:
            myList = myDict.values()
            userKarma = 0
            for index in range(0,len(myList)):
                userKarma = userKarma + myList[index]
            return round((userKarma/float(len(myList))),2)
        # If values are booleans (e.g. over 18 flag), return % True
        if type(myDict.values()[0]) == bool:
            myList = myDict.values()
            over18 = 0
            for index in range(0,len(myList)):
                if myList[index] == True:
                    over18 = over18 + 1
            return round((over18/float(len(myList))),4)


def testAvgValue():
    if avgValue({0:[1,2],1:[3,4]}) == [2,3]:
        print'testAvgValue works for list values'
    else:
        print 'testAvgValue does not work for list values'
    if avgValue({0:unicode('hello sir'),1:unicode('how are you')}) == 2.5:
        print 'testAvgValue works for unicode values'
    else:
        print 'testAvgValue does not work for unicode values'
    if avgValue({0:1,1:2,2:3}) == 2:
        print 'testAvgValue works for integer values'
    else:
        print 'testAvgValue does not work for integer values'
    if avgValue({0:True,1:True,2:False}) == 0.6667:
        print 'testAvgValue works for boolean values'
    else:
        print 'testAvgValue does not work for boolean values'

testAvgValue()
# Test my avgValue function

def avgLength(myDict):
# Takes a dictionary whose keys are unicode (e.g. jokes) and computes the
# average number of words in the keys
    'INPUTS: dict'
    'OUTPUTS: float'
    # dict --> int
    myList = myDict.keys()
    word = 0
    for index in range (0,len(myList)):
        keyIndex = myList[index]
        splitIndex = keyIndex.split()
        word += len(splitIndex)
    return round((word/float(len(myList))),2)


def avgWordLength(myDict):
# Takes a dictionary whose keys are unicode (e.g. jokes) and computes the
# average length of a word in the keys
    'INPUTS: dict'
    'OUTPUTS: float'
    # dict --> int
    myList = myDict.keys()
    char = 0
    length = 0
    for index in range (0,len(myList)):
        myKey = cleanUp(myList[index])
        splitKey = myKey.split()
        length += len(splitKey)
        for index in range (0,len(splitKey)):
            char += len(splitKey[index])
    return round((char/float(length)),2)


def uniqueRatio(myDict):
# Takes a dictionary whose keys are unicode (e.g. jokes) and computes the ratio
# of unique words to total words for the keys
    'INPUTS: dict'
    'OUTPUTS: float'
    # dict --> int
# Do top jokes use relatively fewer unique words (and thus a more similar
# vocabulary) than new jokes?
    jokeList = myDict.keys()
    uniqueList = []
    jokeText = ''
    for index in range(0,len(jokeList)):
        jokeText = jokeText + ' ' + cleanUp(jokeList[index])
    jokeTextList = sorted(jokeText.split())
    uniqueList = [jokeTextList[0]]
    if len(jokeTextList[index]) != 0:
        for index in range(1, len(jokeTextList)):
            current = jokeTextList[index]
            previous = jokeTextList[index-1]
            if previous != current:
                uniqueList = uniqueList + [current]
    ratio = len(uniqueList)/float(len(jokeTextList))
    return round(ratio,2)


def profanityCount(myDict):
# Takes a dictionary whose keys are unicode (e.g. jokes) and returns the
# average number of swear words in each key
    'INPUTS: dict'
    'OUTPUTS: float'
    # dict --> float
    profanityCount = 0
    myList = myDict.keys()
    myString = ''
    for index in range(0,len(myList)):
        myString = myString + myList[index]
    matches = re.finditer('(fuck)|(shit)|(ass)|(bitch)',myString,re.IGNORECASE)
    for match in matches:
        profanityCount = profanityCount + 1
    return round((profanityCount/float(len(myList))),2)


def wordFreq(myDict):
# Takes a dictionary whose keys are unicode (e.g. jokes) and returns the most
# common ten words of length greater than 3 characters
    'INPUTS: dict'
    'OUTPUTS: list = [tuples]; tuple = (unicode,int)'
    # Dict --> list
    import collections
    myList = myDict.keys()
    words = []
    for index in range(0,len(myList)):
        myKey = cleanUp(myList[index])
        words = words + myKey.split()
        noShorts = []
        for word in words:
            if len(word) > 3:
                noShorts = noShorts + [word]
    counter = collections.Counter(noShorts)
    return counter.most_common()[0:10]

allInfo('top')
allInfo('new')
