import pybullet_data
import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
for i in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    print(i)
p.disconnect()
