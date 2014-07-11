class Essay(object):
    def __init__(self, essay):
        self.fileID = essay[0]
        self.prompt = essay[1]
        self.essayID = essay[2]
        self.response = essay[3]
        self.promptID = essay[4]
        self.lemmatized = None
        
    def __repr__(self):
        if len(self.response) < 250:
            return self.response
        else:
            return self.response[:250].__repr__()[:-1] + "...'"
    
class LEssay(object):
    def __init__(self, essay):
        self.fileID = essay[0]
        self.prompt = essay[1]
        self.response = essay[2]
        self.promptID = essay[3]
        
    def __repr__(self):
        if len(self.response) < 250:
            return self.response
        else:
            return self.response[:250].__repr__()[:-1] + "...'"
        
