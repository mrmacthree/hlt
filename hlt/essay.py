from nltk.tokenize import TreebankWordTokenizer
import nltk

class Essay(object):
    def __init__(self, essay):
        self.fileID = essay[0]
        self.prompt = essay[1]
        self.essayID = essay[2]
        self.response = essay[3]
        self.promptID = essay[4]
        self.lemmatized = None
        self.annotation = None

    def sentences(self, lowercase=False, strip_punct=[], num_placeholder=None):
        word_tokenizer=TreebankWordTokenizer()
        sent_tokenizer=nltk.data.LazyLoader('tokenizers/punkt/english.pickle')
        token_sents = [word_tokenizer.tokenize(sent) for sent in sent_tokenizer.tokenize(self.response)]

        if lowercase:
            token_sents = [[token.lower() for token in sent] for sent in token_sents]

        if len(strip_punct) > 0:
            token_sents = [[token for token in sent if token not in strip_punct] for sent in token_sents]

        if num_placeholder is not None:
            def replace_num(token, placeholder):
                try:
                    float(token.replace(',',''))
                    return placeholder
                except ValueError:
                    return token
                
            token_sents = [[replace_num(token, num_placeholder) for token in sent] for sent in token_sents]
        return token_sents



        
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
        
