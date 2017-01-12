''' 
newsBlurSavedStories.py


WRITTEN BY: Sarah H. McGrath (www.shmcgrath.com)
LAST MODIFICATIONS: 2017-01-12

This script will get favorited stories from NewsBlur and put them into 
a markdown document for the downloader's use. 
To use this script, put your NewsBlur username and password into 
nbUser and nbPass.

Helpful References that got me started (and finished):
- [D'Arcy Norman's post getting starred feed items from Newsblur via Python](https://darcynorman.net/2016/12/28/getting-starred-feed-items-from-newsblur-via-python/)
- [Requests: HTTP for Humans' Quickstart Documentation](http://docs.python-requests.org/en/master/user/quickstart/#more-complicated-post-requests)
- [John Morahan's newsblur-export in php](https://github.com/jmorahan/newsblur-export/blob/master/export.php)
- [NewsBlur API in YAML](https://github.com/samuelclay/NewsBlur/blob/master/templates/static/api.yml)
- [Raphael Jasjukaitis' instapaper2chrome.py](https://gist.github.com/raphaa/1327761)
- [Christoper Su's export-saved-reddit](https://github.com/csu/export-saved-reddit))

- I followed D'Arcy Norman's lead and chose readability over brevity. 
    This means long variable and function names.

- Finally, I tried to comment the code as extensively as possible 
so others understand my thought processes.

- I am not sure what kind of license to put on this, so feel free to use
it as needed. Any modifications or forks are fine as long as you link
back to the original on github. Feel free to submit a pull request.

- I am hoping to either add features to this or to roll this into a
larger project for importing/exporting saved articles from various sites.

Thanks, Sarah
'''

import requests
import json
import logging
import os
import sys
from collections import Mapping

# setting NewsBlur name and password
# TODO: use a config file
nbUser = 'USER' #Your username here
nbPass = 'PASS' #Your password here

#creating the creds string to easily pass the credentials
nbCreds = {'username': nbUser, 'password': nbPass}
nbURL = 'http://www.newsblur.com'

'''
newsBlurLogin logs the user in via the API and returns the session ID
to nbSessionId
'''
def newsBlurLogin():

    global nbSessionId
    loginURL = nbURL + '/api/login'

    login = requests.post(loginURL, data=nbCreds)
    print('==LOGIN INFORMATION==')
    print('Status Code: '+str(login.status_code))
    
    nbSessionId = login.cookies['newsblur_sessionid']
    print('nbSessionID Value:'+nbSessionId)
    print('')
    
    return nbSessionId

'''
newsBlurCookies gets the cookies that I need and returns it to a global
variable. I cannot get this to work still.
'''
def newsBlurCookies():

    global nbCookies

    nbCookies = dict(newsblur_sessionid=nbSessionId)
    #print('==COOKIE INFORMATION==')
    #print('nbCookies.text: '+nbCookies.text)
    #print('')

    return nbCookies
    

'''
getFeedInformation gets the starred count of the newsBlur feed that is
logged in. This is used to determine how long to run the 
newsBlurStarredStories function below.
'''
def getFeedInformation():
    #cannot get nbCookies global variable to work
    nbCookies = dict(newsblur_sessionid=str(nbSessionId))
    
    global countOfStarred

    feedParams = {'flat': 'true'} 
    feedURL = nbURL + '/reader/feeds'

    feedList = requests.get(feedURL, params=feedParams, cookies=nbCookies)
    feedListRaw = feedList.json()

    countOfStarred = feedListRaw['starred_count']

    return countOfStarred

#tagMerge combines folders and tags into a single list of tags.
#This was done with the intent of eventually uploading to Pinboard.in
def tagMerge(tags, folders):

    tagsIn = tags
    foldersIn = folders
    processList = tagsIn + foldersIn
    outList = []

    for tag in processList:
        tagNoSpaces = ''.join(tag.split())
        tagLowerCase = tagNoSpaces.lower()
        tagOut = tagLowerCase
        outList.append(tagOut)

    return outList

'''
tagListToString creates a string list of all tags with each tag
separated by a comma.
'''
def tagListToString(tags):
    tagsIn = tags
    tags = ','.join(map(str, tagsIn))

    return tags

'''
gatherStoryInfo grabs the story name, story permalink, story tags, and
the folder that the story was saved to. This will then return the
markdown line for printing. The encoded modifier came from an earlier
version that may have had me encoding the title and URL.
'''
def gatherStoryInfo(aStoryIn):
    aStory = aStoryIn

    title = aStory['story_title']
    url = aStory['story_permalink']
    tags = aStory['story_tags']
    folder = aStory['user_tags']

    encodedTitle = title
    encodedUrl = url
    encodedTagsList = tagMerge(tags, folder)
    encodedTags = tagListToString(encodedTagsList)

    mdLine = '[' + str(encodedTitle) + '](' + str(encodedUrl) + ') ' + encodedTags
    return mdLine

'''
newsBlurStarredStories gets all of the information about the starred
stories that are in the user's account. it also creates the markdown
document and loops through the starred stories.
'''
def newsBlurStarredStories():
    #cannot get nbCookies global variable to work
    nbCookies = dict(newsblur_sessionid=str(nbSessionId))

    #get new text document
    fileName = "newsBlurFavorites.md"
    nbFavoritesMD = open(fileName, 'w')

    i = 1
    page = 1

    y = countOfStarred
    x = countOfStarred // 10
    remainder = countOfStarred % 10

    if remainder != 0:
        x+=2
    
    if remainder == 0:
        x+=1

    starredURL = nbURL + '/reader/starred_stories'
    starredParams = {'page': page,}
    
    storyCount = 0
    page = 1

    while i < x:

        starredList = requests.get(starredURL, {'page': page,}, cookies=nbCookies)
        starredListRaw = starredList.json()
        userStarredStories = starredListRaw ['stories']

        print('Gathering Stories from Page '+str(i)+'...')
        for aStory in userStarredStories:
            
            mdLine = gatherStoryInfo(aStory)
            storyCount +=1

            nbFavoritesMD.write(mdLine)
            nbFavoritesMD.write("\n")
       
        i+=1
        page+=1        
        print('Running Story Count: '+str(storyCount))

    nbFavoritesMD.close()

#This code runs the script.

newsBlurLogin()
getFeedInformation()
userStarredStories = newsBlurStarredStories()