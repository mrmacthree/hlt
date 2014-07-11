class ClassifierType:
    BothReason, OverallReason, PerPromptPartReason = range(3)

class Result(object):
    def __init__(self, result):
        self.fileID = result[0]
        if 'BothReason' in self.fileID:
            self.classifier_type = 'BothReason'
        elif 'OverallReason' in self.fileID:
            self.classifier_type = 'OverallReason'
        elif 'PerPromptPartReason' in self.fileID:
            self.classifier_type = 'PerPromptPartReason'
        else:
            raise
            
        for res in result[1:-1]:
            r = res.split()
            self.__dict__[r[0]] = [float(x) for x in r[1:]]
        self.Agreement = float(result[-1].split()[1])