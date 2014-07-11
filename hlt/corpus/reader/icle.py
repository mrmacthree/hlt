def read_noskipblank_block(stream):
	s = ''
	while True:
		line = stream.readline()
		# End of file:
		if not line:
			if s: return [s]
			else: return []
		# Blank line:
		elif line and not line.strip():
			if s: return [s]
			else: s += 'empty_line'
		# Other line:
		else:
			s += line

class ICLECorpusReader(CategorizedPlaintextCorpusReader):

	def __init__(self, *args, **kwargs):
		CategorizedPlaintextCorpusReader.__init__(self, *args, **kwargs)

	def prompt_paras(self, fileids=None, categories=None):
		paragraphs = self.paras(fileids, categories)
		prev_para = ''
		for para in paragraphs:
			if para[0][0] == '<':
				yield prev_para
			prev_para = para

	def prompt_sents(self, fileids=None, categories=None):
		paragraphs = self.prompt_paras(fileids, categories)
		for para in paragraphs:
			for sent in para:
				yield sent

	def prompt_words(self, fileids=None, categories=None):
		sentences = self.prompt_sents(fileids, categories)
		for sent in sentences:
			for word in sent:
				yield word

	def essay_paras(self, fileids=None, categories=None):
		paragraphs = self.paras(fileids, categories)
		prev_para = [['']]
		for para in paragraphs:
			if para[0][0] != '<' and prev_para[0][0] != '<':
				yield prev_para
			prev_para = para

	def essay_sents(self, fileids=None, categories=None):
		paragraphs = self.essay_paras(fileids, categories)
		for para in paragraphs:
			for sent in para:
				yield sent

	def essay_words(self, fileids=None, categories=None):
		sentences = self.essay_sents(fileids, categories)
		for sent in sentences:
			for word in sent:
				yield word

class ICLELemmatizedCorpusReader(CategorizedPlaintextCorpusReader):

	def __init__(self, *args, **kwargs):
		CategorizedPlaintextCorpusReader.__init__(self, *args, **kwargs)

	def prompt_paras(self, fileids=None, categories=None):
		paragraphs = self.paras(fileids, categories)
		prev_para = ''
		for para in paragraphs:
			if para[0][0] == 'empty_line':
				yield prev_para
			prev_para = para

	def prompt_sents(self, fileids=None, categories=None):
		paragraphs = self.prompt_paras(fileids, categories)
		for para in paragraphs:
			for sent in para:
				yield sent

	def prompt_words(self, fileids=None, categories=None):
		sentences = self.prompt_sents(fileids, categories)
		for sent in sentences:
			for word in sent:
				yield word

	def essay_paras(self, fileids=None, categories=None):
		paragraphs = self.paras(fileids, categories)
		prev_para = [['']]
		for para in paragraphs:
			if para[0][0] != 'empty_line' and prev_para[0][0] != 'empty_line':
				yield prev_para
			prev_para = para

	def essay_sents(self, fileids=None, categories=None):
		paragraphs = self.essay_paras(fileids, categories)
		for para in paragraphs:
			for sent in para:
				yield sent

	def essay_words(self, fileids=None, categories=None):
		sentences = self.essay_sents(fileids, categories)
		for sent in sentences:
			for word in sent:
				yield word

