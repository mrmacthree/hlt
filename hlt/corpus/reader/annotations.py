from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from hlt import Annotation
import re

class PromptAgreementAnnotationsCorpusReader(CategorizedPlaintextCorpusReader):
    def __init__(self, *args, **kwargs):
        self.annotation_word_tokenizer = RegexpTokenizer(r'(Agree|Disagree) Strongly|(Agree|Disagree) Somewhat|Never Addressed|No Opinion|[AC]-\w+|\d+-\d+|\w+|[^\w\s]+')
        CategorizedPlaintextCorpusReader.__init__(self, *args, **kwargs)
    
    def _read_annotation_block_wrapper(self, path):
        paras = [path]
        def _read_annotation_block(stream):
            def lines(list):
                if len(list) > 0:
                    return list.split('\r\n')[:-1]
                return []
            
            raw_paras = self._para_block_reader(stream)
            paras.append(raw_paras[0])
            #paras.append([self._word_tokenizer.tokenize(sent) for sent in self._sent_tokenizer.tokenize(raw_paras[0])])
            for para in raw_paras[1:]:
                subann = lines(para)
                l = list()
                l.append(subann[0])
                for sent in subann[1:]:
                    l.append(self.annotation_word_tokenizer.tokenize(sent))
                paras.append(l)
            return [Annotation(paras)]
        return _read_annotation_block
    
    def annotations(self, fileids=None, categories=None):
        files = self._resolve(fileids, categories)
        if self._sent_tokenizer is None:
            raise ValueError('No sentence tokenizer for this corpus')
        
        return concat([self.CorpusView(path, self._read_annotation_block_wrapper(re.search(r".*AnnR/(.*)",path.path).group(1)), encoding=enc)
                        for (path, enc, files)
                        in self.abspaths(files, True, True)])