'''


@author: Jason
'''

def compute_rank(graph):
    d = 0.8
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
        
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for inlink in graph:
                if page in graph[inlink]:
                    newrank += ( ranks[inlink] * d / len(graph[inlink]))
                             
                     
            
            newranks[page] = newrank
        ranks = newranks
    return ranks