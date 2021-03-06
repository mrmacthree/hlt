from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from nltk.corpus.reader.util import *
from hlt import Essay
import re

class ICLECorpusReader(CategorizedPlaintextCorpusReader):

    def __init__(self, *args, **kwargs):
        if 'element_class' in kwargs:
            self.element_class = kwargs['element_class']
            del kwargs['element_class']
        else:
            self.element_class = Essay
        CategorizedPlaintextCorpusReader.__init__(self, *args, **kwargs)
        
    def _read_essay_block_wrapper(self, path):
        paras = [path]
        def _read_essay_block(stream):
            r = self._para_block_reader(stream)
            for para in r:
                paras.append(para)
                #paras.append([self._word_tokenizer.tokenize(sent) for sent in self._sent_tokenizer.tokenize(para)])

            if self._f2c is None:
                self._init()

            if paras[0] in self._f2c:
                paras.append(list(self._f2c[paras[0]])[0])
            else:
                paras.append('unknown')
            return [self.element_class(paras)]
        return _read_essay_block
    
    def essays(self, fileids=None, categories=None):
        files = self._resolve(fileids, categories)
        if self._sent_tokenizer is None:
            raise ValueError('No sentence tokenizer for this corpus')

        return concat([self.CorpusView(path, self._read_essay_block_wrapper(re.search(r".*(spaced|lemmatized)/(.*)",path.path).group(2)), encoding=enc)
                        for (path, enc, files) in self.abspaths(files, True, True)])

