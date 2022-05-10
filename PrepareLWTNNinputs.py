
Particle       = 'pions'
Version        = 'v41'
ActivationType = 'relu'
loss_def       = 'MSE'  # options: weighted_mean_squared_error, MSE and MAE

# Path to HDF5 files
PATH = '/home/jbossios/cern/FastCaloSim/Keras_Multipurpose_Regression/Results/{}/{}/Models/'.format(Particle,Version)

##################################################################################
# DO NOT MODIFY (below this line)
##################################################################################

# Supported eta bins
EtaBins = ['{}_{}'.format(x*5, x*5+5) for x in range(100)] # full detector

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers.experimental import preprocessing
import keras.backend as K

# Define custom loss
def weighted_mean_squared_error(y_true, y_pred):
  return K.mean(K.square(y_true-y_pred)*weights)

##########################
# Loop over eta bins
##########################
for EtaBin in EtaBins:

  print('INFO: Processing {} eta bin'.format(EtaBin))

  OutBaseName = 'Real_{}_{}_{}'.format(ActivationType,Particle,EtaBin)

  ###############################
  # Get model
  ###############################
  custom_objects_dict = {}
  if loss_def == 'weighted_mean_squared_error':
    custom_objects_dict['weighted_mean_squared_error'] = weighted_mean_squared_error
  if not custom_objects_dict: # dict is empty
    model = keras.models.load_model('{}Real_{}_{}_{}_best_model.h5'.format(PATH, ActivationType, Particle, EtaBin))
  else:
    model = keras.models.load_model('{}Real_{}_{}_{}_best_model.h5'.format(PATH, ActivationType, Particle, EtaBin), custom_objects=custom_objects_dict)

  # Get the architecture as a json string
  arch = model.to_json()
  # Save the architecture string to a file
  with open('{}architecture_{}_{}.json'.format(PATH,Particle,EtaBin), 'w') as arch_file:
    arch_file.write(arch)
  # Save the weights as an HDF5 file
  model.save_weights('{}weights_{}_{}.h5'.format(PATH,Particle,EtaBin))

print('>>> ALL DONE <<<')
