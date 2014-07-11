# Because the files are small, it is most efficient to read them whole
def read_whole_essay_block(stream):
    i = 0
    s = ''
    p = list()
    while len(p) < 2:
        line = stream.readline()
        # End of file:
        if not line:
            raise
        # Blank line:
        elif line and not line.strip():
            if s: 
                p.append(s)
                s = ''
        # Other line:
        else:
            s += line
        
    p.append(stream.read())
    return p
    
    
def read_whole_lessay_block(stream):
    i = 0
    s = ''
    p = list()
    while len(p) < 1:
        line = stream.readline()
        # End of file:
        if not line:
            raise
        # Blank line:
        elif line and not line.strip():
            if s: 
                p.append(s)
                s = ''
        # Other line:
        else:
            s += line
        
    p.append(stream.read())
    return p
        

def read_whole_annotation_block(stream):
    i = 0
    s = ''
    p = list()
    while True:
        line = stream.readline()
        # End of file:
        if not line:
            if s:
                p.append(s)
                return p
            else: return p
        # Blank line:
        elif line and not '\t\t\t' in line and not line.strip():
            if s: 
                p.append(s)
                s = ''
        # Other line:
        else:
            s += line
            
def read_whole_result_block(stream):
    i = 0
    s = ''
    p = list()
    while True:
        line = stream.readline()
        # End of file:
        if not line:
            return p
        # Not blank line:
        elif line.strip():
            p.append(line)