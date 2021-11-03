
Particle = 'photons'
Version  = 'v14'
lwtnn    = 'lwtnn-2.12.1'

# Path to input models
PATH  = '/home/jbossios/cern/FastCaloSim/Keras_Multipurpose_Regression/Results/'
PATH += '{}/{}/Models/'.format(Particle,Version)

# Path to output models
outPATH = 'Outputs/'

###################################
# DO NOT MODIFY (below this line)
###################################

import os,sys

# Supported eta bins
if Particle == 'photons' or Particle == 'electrons':
  EtaBins = ['{}_{}'.format(x*5,x*5+5) for x in range(26)]
elif Particle == 'pions':
  EtaBins = ['{}_{}'.format(x*5,x*5+5) for x in range(16)]
else:
  print(f'ERROR: {Particle} not supported, exiting')
  sys.exit(1)

#############################################################
# 1. Get models and save architecture and weights separately
#############################################################

from tensorflow import keras
from tensorflow.keras.layers.experimental import preprocessing

# obsolete (moved elsewhere)
#for EtaBin in EtaBins:
#  ModelFile = '{}Real_relu_{}_{}_best_model.h5'.format(PATH,Particle,EtaBin)
#  model     = keras.models.load_model(ModelFile,custom_objects={'Normalization': preprocessing.Normalization})
#  # get the architecture as a json string
#  arch = model.to_json()
#  # save the architecture string to a file somehow, the below will work
#  with open('{}architecture_{}_{}.json'.format(PATH,Particle,EtaBin), 'w') as arch_file:
#    arch_file.write(arch)
#  # now save the weights as an HDF5 file
#  model.save_weights('{}weights_{}_{}.h5'.format(PATH,Particle,EtaBin))

#############################################################
# 2. Prepare JSON files for athena
#############################################################
command = ''
counter = 0
for EtaBin in EtaBins:
  counter += 1
  #command += lwtnn+'/converters/keras2json.py     {0}architecture_{1}_{2}.json {3} > {4}inputs_{1}_{2}.json && '.format(PATH,Particle,EtaBin,ModelFile,outPATH)
  #command += lwtnn+'/converters/kerasfunc2json.py {0}architecture_{1}_{2}.json {3} > {4}inputs_{1}_{2}.json && '.format(PATH,Particle,EtaBin,ModelFile,outPATH)
  #command += lwtnn+'/converters/kerasfunc2json.py {0}architecture_{1}_{2}.json {0}weights_{1}_{2}.h5 {0}variables.json > {3}NN_{1}_{4}_{2}.json && '.format(PATH,Particle,EtaBin,outPATH,Version) # not 4 Seq
  command += lwtnn+'/converters/keras2json.py     {0}architecture_{1}_{2}.json {0}variables.json {0}weights_{1}_{2}.h5 > {3}NN_{1}_{4}_{2}.json && '.format(PATH,Particle,EtaBin,outPATH,Version) # meant 4 Seq

command = command[:-2]
print(command)
os.system(command)

