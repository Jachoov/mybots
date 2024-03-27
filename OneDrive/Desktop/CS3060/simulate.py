from simulation import SIMULATION
import sys

# python simulate.py DIRECT
# python simulate.py GUI
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI,solutionID)
simulation.Run()
simulation.Get_Fitness()