import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(10)
for i in range(10):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
p.disconnect()
numpy.save('data/Backleg_touch.npy',backLegSensorValues)