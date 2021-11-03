# Purpose

Create JSON files from Keras models to do inference with [lwtnn](https://github.com/lwtnn/lwtnn)

# How to clone?

get source code (v2.12.1) from
https://github.com/lwtnn/lwtnn/releases/tag/v2.12.1

# How to use?

## Get lwtnn

```
git clone git@github.com:lwtnn/lwtnn.git
```

Compile lwtnn with *CompileLWTNN.sh*:

```
source CompileLWTNN.sh
```

**Note:** if another version than v2.12.1 was downloaded, update ```lwtnn-2.12.1``` to the appropriate version in *CompileLWTNN.sh*

## Create intermediate inputs to lwtnn

### Create Variables.json file

*Variables.json* should specify the name of the input variables (features) and of the labels (targets)

Example:

```
{
  "inputs": [
    {
      "name": "ef_0",
      "offset": 0,
      "scale": 1
    },
    {
      "name": "ef_1",
      "offset": 0,
      "scale": 1
    },
    {
      "name": "ef_2",
      "offset": 0,
      "scale": 1
    },
    {
      "name": "ef_3",
      "offset": 0,
      "scale": 1
    },
    {
      "name": "ef_12",
      "offset": 0,
      "scale": 1
    },
    {
      "name": "etrue",
      "offset": 0,
      "scale": 1
    }
  ],
  "class_labels": ["extrapWeight_0","extrapWeight_1","extrapWeight_2","extrapWeight_3","extrapWeight_12"]
}
```

### Create architecture files with *PrepareLWTNNinputs.py*:

Set:

- ```Particle```: should match with particles used during training 
- ```Versions```: should match with version used during training
- ```ActivationType```: should match with option used during training
- ```PATH```: path to HDF5 files (outputs of Regression.py from RegressionWithKeras)

Run:

```
python PrepareLWTNNinputs.py
```

## Create JSON files with *CreateJSONs.py*:

Set:

- ```Particle```
- ```Version```
- ```lwtnn```: should match version of lwtnn which was downloaded
- ```PATH```: path to input models (HDF5 files)
- ```outPATH```: path to output models (JSON files)

Run:

```
python CreateJSONs.py
```
