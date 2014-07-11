class PromptAgreementDataset(object):
    def __init__(self, icle_corpus, lemmatized_corpus, prompt_agreement_annotations_corpus, prompt=None):
        self.icle = icle_corpus
        self.lemm = lemmatized_corpus
        if type(prompt_agreement_annotations_corpus) == PromptAgreementAnnotationsCorpusReader:
            self.ann = prompt_agreement_annotations_corpus
            self.ann_list = None
        else:
            self.ann = None
            self.ann_list = prompt_agreement_annotations_corpus
        self.prompt = prompt
        
        
        
    def __iter__(self):
        if self.ann_list is not None: 
            self.it = iter(self.ann_list)
        else:
            self.it = iter(self.ann.annotations(categories=self.prompt))
        return self
    
    def next(self):
        a = self.it.next()
        essayid = re.search(r'.*/(.*).promptagg', a.fileID).group(1)
        a.essay = self.icle.essays(fileids=[essayid+'.spaced'])
        a.essay.lemmatized = self.lemm.essays(fileids=[essayid+'.lemmatized'])
        return a
    
    def __getitem__(self, i):
        if isinstance(i, slice):
            if self.ann_list is not None:
                a = self.ann_list[i]
            else:
                a = self.ann.annotations(categories=self.prompt)[i]
            return PromptAgreementDataset(self.icle, self.lemm, a)
        else:
            if self.ann_list is not None:
                a = self.ann_list[i]
            else:
                a = self.ann.annotations(categories=self.prompt)[i]
            essayid = re.search(r'.*/(.*).promptagg', a.fileID).group(1)
            a.essay = self.icle.essays(fileids=[essayid+'.spaced'])
            a.essay.lemmatized = self.lemm.essays(fileids=[essayid+'.lemmatized'])
            return a
    
    def __len__(self):
        if self.ann_list is not None:
            return len(self.ann_list)
        else:
            return len(self.ann.annotations(categories=self.prompt))
    
    def __repr__(self):
        if self.ann_list is not None:
            return self.ann_list.__repr__()
        else:
            return self.ann.annotations(categories=self.prompt).__repr__()
        