'''
Input:  G, a connected nx graph
        z, a node in G
Output: a list G' nodes in order lex_bfs
'''

def lex_bfs(G, z):
    n = len(G.nodes())
    nodes = G.nodes()[:]
    label = []
    for i in range(n):
        label.append([0])
    index = nodes.index(z)
    label[index] = [n]
    enum = []
    print nodes
    for val in range(n, 0, -1):

        max_label = max(label)
        #print "max lab " + str(max_label)
        index = label.index(max_label)
        m = nodes[index]
        enum.append(m)
        #print "enum " + str(enum)
        nodes.remove(m)
        label.remove(max_label)
        for neighbor in G.neighbors(m):
            if neighbor in nodes:
                index = nodes.index(neighbor)
                label[index].insert(-1,val)
    #enum.reverse()
    return enum