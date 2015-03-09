class Agreement:
    names = ['Agree Strongly', 'Agree Somewhat', 'Neutral', 'Disagree Somewhat', 'Disagree Strongly', 'Never Addressed', 'No Opinion']
    AgreeStrongly, AgreeSomewhat, Neutral, DisagreeSomewhat, DisagreeStrongly, NeverAddressed, NoOpinion = range(7)
    
class Confidence:
    names = ['High', 'Medium', 'Low', 'None']
    High, Medium, Low, None_ = range(4)
    
class Reasons:
    names = ['C-BrieflyDiscussed', 'C-ConflictingOpinions', 'C-ConfusinglyPhrased', 
             'C-NeverAddressed', 'C-PartialResponse', 'C-Relevance', 
             'C-SubtlerPoint', 'C-WriterPosition', 'C-Other', 
             'A-ConflictingOpinions', 'A-ExplicitlyStated', 'A-NoOpinion', 
             'A-PartialResponse', 'A-SubtlerPoint', 'A-WriterPosition', 
             'A-Other'] 
             
    names_combined = ['ConfusinglyPhrased', 'PartialResponse', 'WriterPosition', 
                      'NeverAddressed', 'NoOpinion', 'ExplicitlyStated', 
                      'BrieflyDiscussed', 'Other', 'ConflictingOpinions', 
                      'Relevance', 'SubtlerPoint']
    
    all_used_labels =  ['ConfusinglyPhrased', 'PartialResponse', 'WriterPosition', 
                        'ExplicitlyStated', 'BrieflyDiscussed', 'ConflictingOpinions', 
                        'Relevance', 'SubtlerPoint']

    thesis_labels = ['ConfusinglyPhrased','ExplicitlyStated', 'WriterPosition', 
                     'ConflictingOpinions', 'PartialResponse', 'SubtlerPoint', 
                     'Relevance']

    overall_labels = ['BrieflyDiscussed', 'WriterPosition', 'ConflictingOpinions', 
                      'PartialResponse', 'SubtlerPoint', 'Relevance']

    Null = -1
    C_BrieflyDiscussed, C_ConflictingOpinions, C_ConfusinglyPhrased, C_NeverAddressed, C_PartialResponse, C_Relevance, C_SubtlerPoint, C_WriterPosition, C_Other, A_ConflictingOpinions, A_ExplicitlyStated, A_NoOpinion, A_PartialResponse, A_SubtlerPoint, A_WriterPosition, A_Other = range(16)
    
class SubAnnotation(object):
    def __init__(self, annotation):
        #print annotation
        def parse(text):
            if text == "null":
                return -1
            elif text == "Agree Strongly" or text == "High" or text == "C-BrieflyDiscussed":
                return 0
            elif text == "Agree Somewhat" or text == "Medium" or text == "C-ConflictingOpinions":
                return 1
            elif text == "Neutral" or text == "Low" or text == "C-ConfusinglyPhrased":
                return 2 
            elif text == "Disagree Somewhat" or text == "None_" or text == "C-NeverAddressed":
                return 3 
            elif text == "Disagree Strongly" or text == "C-PartialResponse":
                return 4
            elif text == "Never Addressed" or text == "C-Relevance":
                return 5
            elif text == "No Opinion" or text == "C-SubtlerPoint":
                return 6 
            elif text == "C-WriterPosition":
                return 7
            elif text == "C-Other":
                return 8
            elif text == "A-ConflictingOpinions":
                return 9
            elif text == "A-ExplicitlyStated":
                return 10
            elif text == "A-NoOpinion":
                return 11
            elif text == "A-PartialResponse":
                return 12
            elif text == "A-SubtlerPoint": 
                return 13
            elif text == "A-WriterPosition": 
                return 14
            elif text == "A-Other":
                return 15
            else: 
                raise Exception('Bad Parse', text)
                
        self.promptPart = annotation[0]
        #self.agreement = parse(annotation[1][0])
        self.agreement = annotation[1][0]
        #self.confidence = parse(annotation[1][1])
        if len(annotation[1]) < 2:
            self.confidence = 'UNK'
        else:
            self.confidence = annotation[1][1]
        #self.reasons = [parse(x) for x in annotation[2]]
        self.reasons = annotation[2]
        self.rationales = annotation[3]
              
            
class Annotation(object):
    def __init__(self, annotation):
        #print annotation
        self.fileID = annotation[0]
        #print self.fileID
        self.prompt = annotation[1]
        self.annotations = [SubAnnotation(x) for x in annotation[2:-1]]
        self.promptID = annotation[-1]
        
    def __repr__(self):
        return "Annotation(" + self.fileID + ", " + self.promptID + ")"