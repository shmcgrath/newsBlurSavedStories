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


## Copy of License

MIT License

Copyright (c) [2017] [Sarah H. McGrath]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.