import numpy as np
import matplotlib.pyplot as plt

###########################################################################
########################### PLOTTING STARTS HERE
###########################################################################

import matplotlib as mpl
from matplotlib.colors import LogNorm
from matplotlib.ticker import LogLocator
from skimage import io

def tif2npy(sim, filename, time):
    nanoParticles = io.imread('../data/' + sim + filename)
    nanoP = nanoParticles.astype(float)/np.max(nanoParticles.astype(float))
    nanoP = np.asarray(nanoP)
    saveto = '../data/' + sim + '/diff_' + str(time) + 'sec'
    np.save(saveto, nanoP)

def main(sim, time = ''):
    if time == '':
        time = np.load('../sim/' + sim + '/lastTime_seconds.npy')

    #colors_techniques = plt.cm.viridis(np.linspace(0.,1.,len(techniques))) #BuPu
    lines = [':', '-', ':', '-', ':', '-', '-']
    n = 10
    colors_gradient = plt.cm.inferno(np.linspace(0,1,n))

    fig, ax = plt.subplots()
    nanoP = np.load('../sim/' + sim +'/diff_' + str(time) + 'sec' + '.npy')
    nanoP = nanoP/np.max(nanoP) #in case max in not concentration

    nanoP[nanoP < 10**(-3)] = 10**(-3)
    downsize = 1

    cax = ax.contourf(range(0,np.shape(nanoP)[0],1)[::downsize], range(0,np.shape(nanoP)[1],1)[::downsize], nanoP[::downsize,::downsize], levels=np.logspace(-3, 0, 100), locator=mpl.ticker.LogLocator(50), cmap=plt.cm.inferno)
    cbar = fig.colorbar(cax, ticks=[10**0, 10**(-3)])

    #cbar.ax.set_ylabel(r'$Concentration$')
    for c in ax.collections:
        c.set_edgecolor("face")
    plt.title("Normalized concentration of np")
    ax.set_xlabel(r"$z$-direction ($\mu m$)")
    ax.set_ylabel(r"$y$-direction ($\mu m$)")
    ax.minorticks_off()
    filename = "../sim/" + sim + "_" + str(time)
    plt.show()

if __name__ == "__main__":
    main('parent_model_tumor160_stack2', time='2D1800.0')
