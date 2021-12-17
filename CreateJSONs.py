
Particle = 'pionsANDelectrons'
Version  = 'v27'
lwtnn    = 'lwtnn-2.12.1'

# Path to input models
PATH  = '/home/jbossios/cern/FastCaloSim/Keras_Multipurpose_Regression/Results/'
PATH += '{}/{}/Models/'.format(Particle,Version)

# Path to output models
outPATH = 'Outputs/{}/'.format(Version)

###################################
# DO NOT MODIFY (below this line)
###################################

import os,sys

# Create output folder
if not os.path.exists(outPATH):
  os.makedirs(outPATH)

# Supported eta bins
if 'photons' in Particle or 'electrons' in Particle or Particle == 'all':
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

#############################################################
# 2. Prepare JSON files for athena
#############################################################
command = ''
for EtaBin in EtaBins:
  command += lwtnn+'/converters/keras2json.py {0}architecture_{1}_{2}.json {0}variables.json {0}weights_{1}_{2}.h5 > {3}NN_{2}.json && '.format(PATH,Particle,EtaBin,outPATH) # meant 4 Seq
command = command[:-2]
print(command)
os.system(command)

