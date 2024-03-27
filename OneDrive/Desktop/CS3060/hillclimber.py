from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        
    def Evolve(self):
        # self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            if currentGeneration == 0:
                self.parent.Evaluate("GUI")
            else:
                self.parent.Evaluate("DIRECT")
            self.Evolve_For_One_Generation()
    
    def Show_Best(self):
        self.parent.Evaluate("GUI")
    
    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()
        
        self.child.Evaluate("DIRECT")
        
        self.Select()
        
        self.Print()
        
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def Mutate(self):
        self.child.Mutate()
    
    def Evaluate(self):
        pass

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
            
    def Print(self):
        print("parent: " + str(self.parent.fitness) + " child: " + str(self.child.fitness))