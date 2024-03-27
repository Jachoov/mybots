import numpy
import os
import pyrosim.pyrosim as pyrosim
from sys import exit
import random
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        sensorNeurons = [0,1,2]
        motorNeurons = [3,4]
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system("start /B python simulate.py " + directOrGUI  + " " + str(self.myID))#os.system("python simulate.py " + directGUI)
        
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        
        f = open("fitness"+str(self.myID)+".txt","r")
        self.fitness = str(f.read())
        f.close()
        # print(self.fitness)
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGUI  + " " + str(self.myID))#os.system("python simulate.py " + directGUI)
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        
        f = open("fitness"+str(self.myID)+".txt","r")
        self.fitness = str(f.read())
        print(self.fitness)
        os.system("del fitness"+str(self.myID)+".txt")
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x = 3
        y = 3
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="Frontleg", pos=[.5,0,-0.5] , size=[1,1,1])
        pyrosim.End()
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
        currentRows = [0,1,2]
        currentColumns = [0,1]
        for currentRow in currentRows:
            for currentColumn in currentColumns:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn] )
            
        pyrosim.End()
        
    def Mutate(self):
        self.weights[random.randint(0,2),random.randint(0,1)] = random.random() * 2 - 1
        
    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID