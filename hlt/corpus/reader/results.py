class ResultCorpusReader(CategorizedPlaintextCorpusReader):
    def __init__(self, *args, **kwargs):        
        CategorizedPlaintextCorpusReader.__init__(self, *args, **kwargs)

    def _read_result_block_wrapper(self, path):
        paras = [path]
        def _read_result_block(stream):
            r = self._para_block_reader(stream)
            for para in r:
                paras.append(para)
                #paras.append([self._word_tokenizer.tokenize(sent) for sent in self._sent_tokenizer.tokenize(para)])
            return [Result(paras)]
        return _read_result_block

    def results(self, fileids=None, categories=None):
        files = self._resolve(fileids, categories)
        if self._sent_tokenizer is None:
            raise ValueError('No sentence tokenizer for this corpus')

        return concat([self.CorpusView(path, self._read_result_block_wrapper(re.search(r".*res/(.*)",path.path).group(1)), encoding=enc)
                        for (path, enc, files) in self.abspaths(files, True, True)])