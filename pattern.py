# -*- coding: utf-8 -*-
import re, string
def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

#From http://daringfireball.net/2010/07/improved_regex_for_matching_urls
urls = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""

urlpattern = re.compile(urls)

#http://stackoverflow.com/questions/1986059/grubers-url-regular-expression-in-python?rq=1

#urlpattern = r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^%s\s]|/)))'
#urlpattern = urlpattern % re.sub(r'([-\\\]])', r'\\\1', string.punctuation)

#urlreg = re.compile(urlpattern)
