''' Zettel metadata and content '''

class Zettel:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.date_time = None
        self.content = None
    
    def get_date(self):
        ''' Get date part of self.date_time as string '''
        if self.date_time == None:
            return None
        
        return self.date_time.split(" ")[0]

    def get_time(self):
        ''' Get time part of self.date_time as string '''
        if self.date_time == None:
            return None
        
        time = self.date_time.split(" ")
        if len(time) == 1:
            return None
        else:
            return time[1]