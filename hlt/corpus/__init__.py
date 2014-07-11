from hlt.corpus.reader import *

spacedFileIDToPromptID = dict()
with open('~/spac-cat.txt', 'r') as f:
    for line in f:
        s = line.split()
        spacedFileIDToPromptID[s[0]] = list()
        spacedFileIDToPromptID[s[0]].append(s[1])
f.close()

lemmatizedFileIDToPromptID = dict()
with open('~/lem-cat.txt', 'r') as f:
    for line in f:
        s = line.split()
        lemmatizedFileIDToPromptID[s[0]] = list()
        lemmatizedFileIDToPromptID[s[0]].append(s[1])
f.close()

AnnRFileIDToPromptID = dict()
with open('~/AnnR-cat.txt', 'r') as f:
    for line in f:
        s = line.split()
        AnnRFileIDToPromptID[s[0]] = list()
        AnnRFileIDToPromptID[s[0]].append(s[1])
f.close()

icle = ICLECorpusReader('/shared/mlrdir1/disk1/mlr/corpora/ICLE/spaced', r'.*\.spaced', 
    cat_map=spacedFileIDToPromptID,
    para_block_reader=read_whole_essay_block)

lemm = ICLECorpusReader('/shared/mlrdir1/disk1/mlr/corpora/ICLE/lemmatized', r'.*\.lemmatized', 
    cat_map=lemmatizedFileIDToPromptID,
    para_block_reader=read_whole_lessay_block,
    element_class=LEssay)

ann = PromptAgreementAnnotationsCorpusReader('/shared/mlrdir1/disk1/mlr/corpora/ICLE/ThesisAgreement/AnnR', r'.*\.promptagg', 
    cat_map=AnnRFileIDToPromptID,                                  
    para_block_reader=read_whole_annotation_block)


pa = PromptAgreementDataset(icle, lemm, ann, None)