import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

# from hillclimber import HILL_CLIMBER

# hc = HILL_CLIMBER()
# hc.Evolve()
# hc.Show_Best()

# for n in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")