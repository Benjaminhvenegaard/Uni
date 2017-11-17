
#Graph which will be looked upon
graph = {'A': set(['B','C']),
         'B': set(['A','D','E']),
         'C': set(['A','F']),
         'D': set(['B']),
         'E': set(['B','F']),
         'F': set(['C','E'])}
print()
#Depth first search algorithm
def dfs_paths(graph, start, goal):                  # dfs_paths is defined with a graph, a start point, a goal point
    print( "dfs_paths()")                           # Print
    stack = [(start, [start])]                      # [starten], [elemterne skrevet på reste af listen]
    while stack:                                    # Biggining of while-loop
        (vertex, path) = stack.pop()                # Pops the next vertex in the path 
        print( " vertex:", vertex)                  # Print
        print( " path:", path)                      # Print
        for next in graph[vertex] - set(path):      # Sets a vertex on a path
            print( " next is", next)                #
            if next == goal:                        # Checks if qoal is reached
                print( " ->found goal!")            # 
                yield path + [next]                 # Yield is the same as a return function but for lists and more complicated since it takes a generator which are iterators but can only iterate once
            else:                                   #
                stack.append((next, path + [next])) # inserting (path + [next] on id = next
    print( "stack is empty")                        #

dfs_result = list(dfs_paths(graph,'A','F'))         # sets list as dfs_paths(using graph, start, end)
print( "DFS result:",dfs_result)                    # Prints the result

print()                                             # Prints out an epmty line
    
#Breadth first search algorithm
def dfs_paths(graph, start, goal):                  # 
    print( "dfs_paths()")
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)               # Since it is a queue it will be first in first out
        print( " vertex:", vertex)                  
        print( " path:", path)
        for next in graph[vertex] - set(path):
            print( " next is", next)
            if next == goal:
                print( " ->found goal!")
                yield path + [next]
            else:
                queue.append((next, path + [next]))
    print( "queue is empty")

dfs_result = list(dfs_paths(graph,'A','F'))
print( "DFS result:",dfs_result)

print()


