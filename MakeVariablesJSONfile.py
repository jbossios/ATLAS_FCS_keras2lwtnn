def get_layers(particle, eta_bin):
  layers_dict = {
    'photons' : {'3_1_0_12_2': 'eta_0_130', '3_1_0_17_2': 'eta_130_135', '4_5_18_3_1_0_6_17_2': 'eta_135_145', '4_5_18_1_0_6_17_2': 'eta_145_150', '4_5_6_17': 'eta_150_160', '4_5_6_7_8': 'eta_160_300', '21_23_6_7_22_8': 'eta_300_500'},
    'electrons' : {'3_1_0_12_2': 'eta_0_130', '3_1_0_17_2': 'eta_130_135', '4_5_18_3_1_0_6_17_2': 'eta_135_145', '4_5_18_1_0_6_17_2': 'eta_145_150', '4_5_6_17': 'eta_150_160', '4_5_6_7_8': 'eta_160_300', '21_23_6_7_22_8': 'eta_300_500'},
    'electronsANDphotons' : {'3_1_0_12_2': 'eta_0_130', '3_1_0_17_2': 'eta_130_135', '4_5_18_3_1_0_6_17_2': 'eta_135_145', '4_5_18_1_0_6_17_2': 'eta_145_150', '4_5_6_17': 'eta_150_160', '4_5_6_7_8': 'eta_160_300', '21_23_6_7_22_8': 'eta_300_500'},
    'pions' : {'3_1_0_12_14_2_13': 'eta_0_90', '20_18_19_3_1_17_0_12_14_2_13_16_15': 'eta_90_130', '20_18_3_6_7_2_15_4_19_1_14_12_13_16_5_0_17_9_8': 'eta_130_150', '4_9_5_11_18_19_6_10_7_17_8': 'eta_150_170', '4_9_5_11_18_6_10_7_8': 'eta_170_240', '4_9_5_11_6_10_7_8': 'eta_240_280', '4_9_5_11_21_23_6_10_7_22_8': 'eta_280_350', '22_23_21': 'eta_350_500'},
    'pionsANDelectrons' : {'3_1_0_12_14_2_13': 'eta_0_90', '20_18_19_3_1_17_0_12_14_2_13_16_15': 'eta_90_130', '20_18_3_6_7_2_15_4_19_1_14_12_13_16_5_0_17_9_8': 'eta_130_150', '4_9_5_11_18_19_6_10_7_17_8': 'eta_150_170', '4_9_5_11_18_6_10_7_8': 'eta_170_240', '4_9_5_11_6_10_7_8': 'eta_240_280', '4_9_5_11_21_23_6_10_7_22_8': 'eta_280_350', '22_23_21_6_7_8': 'eta_350_500'},
    'all' : {'3_1_0_12_14_2_13': 'eta_0_90', '20_18_19_3_1_17_0_12_14_2_13_16_15': 'eta_90_130', '20_18_3_6_7_2_15_4_19_1_14_12_13_16_5_0_17_9_8': 'eta_130_150', '4_9_5_11_18_19_6_10_7_17_8': 'eta_150_170', '4_9_5_11_18_6_10_7_8': 'eta_170_240', '4_9_5_11_6_10_7_8': 'eta_240_280', '4_9_5_11_21_23_6_10_7_22_8': 'eta_280_350', '22_23_21_6_7_8': 'eta_350_500'},
  }[particle]
  eta_min = int(eta_bin.split('_')[0])
  eta_max = int(eta_bin.split('_')[1])
  for key, eta_range in layers_dict.items():
    min_range = int(eta_range.split('_')[1])
    max_range = int(eta_range.split('_')[2])
    if eta_min >= min_range and eta_max <= max_range:
      layers = list(set([int(item) for item in key.split('_')]))
      return list(set([int(item) for item in key.split('_')]))
  return []

def main(particles, version, path):
  print('Creating JSON variables file for particles={}, version={}'.format(particles, version))
  eta_bins = ['{}_{}'.format(x*5, x*5+5) for x in range(100)] # full detector
  for eta_bin in eta_bins:
    layers = get_layers(particles, eta_bin)
    out_name_file = f'{path}{particles}/{version}/Models/variables_eta_{eta_bin}.json'
    with open(out_name_file, 'w') as ofile:
      ofile.write('{\n')
      ofile.write('  "inputs": [\n')
      for layer in layers:
        ofile.write('    {\n')
        ofile.write(f'      "name": "ef_{layer}",\n')
        ofile.write(f'      "offset": 0,\n')
        ofile.write(f'      "scale": 1\n')
        ofile.write('    },\n')
      ofile.write('    {\n')
      ofile.write(f'      "name": "etrue",\n')
      ofile.write(f'      "offset": 0,\n')
      ofile.write(f'      "scale": 1\n')
      ofile.write('    }\n')
      ofile.write('  ],\n')
      labels = [f'extrapWeight_{layer}' for layer in layers]
      labels_string = '","'.join(labels)
      ofile.write(f'  "class_labels": ["{labels_string}"]\n')
      ofile.write('}\n')

if __name__ == '__main__':
  main(particles = 'pions', version = 'v41', path = '/home/jbossios/cern/FastCaloSim/Keras_Multipurpose_Regression/Results/')
  print('>>> ALL DONE <<<')
