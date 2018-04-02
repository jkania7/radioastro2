import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

fluxes = np.loadtxt('fluxes.txt',skiprows=1)
print("fluxed={0}".format(fluxes))

plt.figure()
plt.errorbar(fluxes[:,0],fluxes[:,1],yerr=fluxes[:,2])
plt.title(r"Flux desity as a function of frequency")
plt.show()
