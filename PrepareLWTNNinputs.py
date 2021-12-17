
Particle       = 'pionsANDelectrons'
Version        = 'v27'
ActivationType = 'relu'

# Path to HDF5 files
PATH = '/home/jbossios/cern/FastCaloSim/Keras_Multipurpose_Regression/Results/{}/{}/Models/'.format(Particle,Version)

##################################################################################
# DO NOT MODIFY (below this line)
##################################################################################

# Supported eta bins
if 'photons' in Particle or 'electrons' in Particle or Particle == 'all':
  EtaBins = ['{}_{}'.format(x*5,x*5+5) for x in range(26)]
elif Particle == 'pions':
  EtaBins = ['{}_{}'.format(x*5,x*5+5) for x in range(16)]

##########################
# Loop over eta bins
##########################
for EtaBin in EtaBins:

  print('INFO: Processing {} eta bin'.format(EtaBin))

  OutBaseName = 'Real_{}_{}_{}'.format(ActivationType,Particle,EtaBin)

  import numpy as np
  import pandas as pd
  import tensorflow as tf
  import matplotlib.pyplot as plt
  from tensorflow import keras
  from tensorflow.keras.layers.experimental import preprocessing

  ###############################
  # Get model
  ###############################
  model = keras.models.load_model('{}Real_{}_{}_{}_best_model.h5'.format(PATH,ActivationType,Particle,EtaBin))

  # Get the architecture as a json string
  arch = model.to_json()
  # Save the architecture string to a file
  with open('{}architecture_{}_{}.json'.format(PATH,Particle,EtaBin), 'w') as arch_file:
    arch_file.write(arch)
  # Save the weights as an HDF5 file
  model.save_weights('{}weights_{}_{}.h5'.format(PATH,Particle,EtaBin))

print('>>> ALL DONE <<<')
