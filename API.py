# Copyright (c) Erik Campobadal <soc@erik.cat>

# Import the request library to perform HTTP requests.
import urllib.request as req

# Telegram class
class Telegram():
    base = 'https://api.telegram.org/bot'

    def __getattr__(self, name):
        def fun(p = {}):
            params = ''.join([str(i) + '=' + str(p[i]) + '&' for i in p])
            return req.urlopen(Telegram.base + self.token + '/' + name + '?' + params).read()
        return fun

    def __init__(self, token):
        self.token = token
