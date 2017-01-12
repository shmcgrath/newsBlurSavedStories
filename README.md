# newsBlurSavedStories.py

## About

This python script will save all saved/favorite/starred stories from the users [NewsBlur](http://newsblur.com) account into a markdown document.

newsBlurSavedStories was originally written by Sarah H. McGrath (www.shmcgrath.com).

## How to Use newsBlurSavedStories.py

To use this script, a user needs to replace ‘USER’ and ‘PASS’ in the *newsblurLogin* funciton with the username and password to their NewsBlur account. These variables are marked with \#Your username here and \#Your password here.

The user needs to make sure that [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/#) is installed on their machine as the script depends on it. This install can be with pip:

```bash
	$ pip install requests
```

The documentation provides more detail on installing Requests.

## Future Plans

I am hoping to either add features to this or to roll this into a larger project for importing/exporting saved articles from various sites.