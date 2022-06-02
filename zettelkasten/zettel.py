'''
Zettel metadata and content
'''

class Zettel:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.date = None
        self.time = None
        self.content