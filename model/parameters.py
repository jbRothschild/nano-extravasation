import numpy as  np
"""
Units: seconds, micrometers
"""

#IMAGE LOADING
TUMOR_IMAGE = 160
STACK = 2

#FILES TO LOAD
LOAD_DIR = "../extravasationfinalimgs/"
DATA_NAME = "MSC" + str(TUMOR_IMAGE) + "-T-stack" + str(STACK) + "-Nov29-2018"

DOMAIN = "tissue_boundary/" + DATA_NAME + "-cropped.tif"
VESSEL = "thresh_vessels/" + DATA_NAME + "isothresh_vessels.tif"
HOLES = "gaps_100x/" + DATA_NAME + ".tif"
GEN_HOLES = "gaps_actual/" + DATA_NAME + ".tif"

SIM_DIR = "../sim/parent_model_tumor" + str(TUMOR_IMAGE) + "_stack" + str(STACK)

#SIMULATION PARAMETERS
DIF_COEF = 0.05
VISC = 0.0
TOT_TIME = 3600. * .5 #30 minutes
TIME_STEP = 10. #( dt*D/x^2 + dt*D/y^2 + dt*D/z^2 ) =< 1/2
SAVE_TIME = 1800.
GLOB_DX = 2.
GLOB_DY = 2.
GLOB_DZ = 2.
GAP_MULT = 1
