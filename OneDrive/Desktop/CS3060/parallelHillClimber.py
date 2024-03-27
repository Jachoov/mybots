from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):
        for i in self.parents:
            self.parents[i].Start_Simulation("DIRECT")
        for i in self.parents:
            self.parents[i].Wait_For_Simulation_To_End()
        # for currentGeneration in range(c.numberOfGenerations):
        #     if currentGeneration == 0:
        #         self.parent.Evaluate("GUI")
        #     else:
        #         self.parent.Evaluate("DIRECT")
        #     self.Evolve_For_One_Generation()
    
    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass
    
    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()
        
        self.child.Evaluate("DIRECT")
        
        self.Select()
        
        self.Print()
        
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
    
    def Mutate(self):
        self.child.Mutate()
    
    def Evaluate(self):
        pass

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
            
    def Print(self):
        print("parent: " + str(self.parent.fitness) + " child: " + str(self.child.fitness))