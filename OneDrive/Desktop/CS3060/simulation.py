from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import constants as c
import time

class SIMULATION:
    def __init__(self, directOrGUI,solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
        self.physicsClient = p.connect(p.DIRECT) #(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()#
        self.robot = ROBOT(solutionID)#
        
        
    def Run(self):
        for t in range(500):
            if self.directOrGUI == "GUI":
                time.sleep(1/100)#60)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
        
    def __del__(self):
        p.disconnect()
        
    def Get_Fitness(self):
        self.robot.Get_Fitness()