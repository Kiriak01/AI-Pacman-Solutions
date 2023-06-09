# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    stack = util.Stack()  
    path = [] 
    source = problem.getStartState()
    if problem.isGoalState(source):
        return path 
    
    visited = set() 
    stack.push((source,[])) 

    while stack:
        node,path = stack.pop()
        visited.add(node)  
        if problem.isGoalState(node):
            return path 
        children = problem.expand(node) 
        for child in children:
            childState = child[0] 
            childDir = child[1] 
            if childState not in visited:
                childPath = path + [childDir]   
                stack.push((childState,childPath))  
            
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    queue = util.Queue() 
    source = problem.getStartState() 
    path = [] 
    if problem.isGoalState(source):
        return path 
    
    visited = set() 
    queue.push((source,[]))
    visited.add(source)  

    while queue:
        node,path = queue.pop()  
        if problem.isGoalState(node):
            return path 
        children = problem.expand(node) 
        for child in children:
            childState = child[0]
            childDir = child[1] 
            if childState not in visited:
                childPath = path + [childDir]  
                queue.push((childState,childPath))   
                visited.add(childState) 
                      
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    pQueue = util.PriorityQueue()    
    source = problem.getStartState()
    path = []
    h = heuristic(source,problem)    
    g = 0 
    f = g + h 
    if problem.isGoalState(source): 
        return path 
    pQueue.push((source,[],),f)   
    visited = set() 
    
    while pQueue:
        node,path = pQueue.pop()
        if node in visited:
            continue
        else:
            visited.add(node) 
        if problem.isGoalState(node):
            return path 
        children = problem.expand(node) 
        for child in children:
            childState = child[0]
            childDir = child[1] 
            if childState not in visited:
                childPath = path + [childDir]
                g = problem.getCostOfActionSequence(childPath)     
                h = heuristic(childState,problem)  
                f = g + h  
                pQueue.push((childState,childPath),f)  
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
