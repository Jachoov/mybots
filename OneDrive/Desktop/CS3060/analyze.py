import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = "backLegSensorValues")
matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLegSensorValues")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()