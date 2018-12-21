import sys, os, time
import write_data as wd
import numpy as np
from skimage import io

#Argument is the diffusion coefficient for now
import argparse

parser = argparse.ArgumentParser(description='Submitting different diffusion parameters')
parser.add_argument('-m', metavar='M', type=str, action='store', default='parent_model', required=False, help='model passed to import')
#Namespace with the arguments
args = parser.parse_args()


def main(model, **data):
    #===============Model selection==================================
    if not os.path.exists('../sim/'):
        os.makedirs('../sim/')

    mod = __import__(model)

    sim_model = mod.Model(**data)

    #=================Model + Parameter Creation=====================
    #This is where we create our models from the different functions in either data_model.py or custom_model.py
    sim_model.initialize()
    sim_model.solution = np.copy( sim_model.source_loc )

    #================Euleur's method============================
    init_time = sim_model.time
    print(init_time)
    tic = time.time()
    for t in np.arange( init_time, sim_model.total_time + 1., sim_model.dt ): #run from time saved previously
        tic1 = time.time()
        sim_model.simulation_step()

        sim_model.time = t

        #--------------------Saving Data-------------------
        if sim_model.time in np.arange(0 , sim_model.total_time + 1, sim_model.save_data_time):
            sim_model.save_sim()

        #saving the sum at each time step.
        if sim_model.timeSum[0,sim_model.timeSum.shape[1]-1] < sim_model.time:
            sim_model.save_time_sum()

        #-------------------------------------------

        #CHange to a for loop, for any updates that might happen and their time
        if sim_model.time in np.arange( 0, sim_model.total_time, sim_model.update_time):
            sim_model.update_simulation()

        toc1 = time.time()
        print toc1 - tic1, "sec for roughly one time step..."
    toc = time.time()
    print toc - tic, "sec for total simulation."

if __name__ == "__main__":
    main(model=vars(args)['m'], **data)
