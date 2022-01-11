# IIITD ALIVE DSM submission

Submission for IIITD's ALIVE lab project round 2.

## Overview
### Relevant files
- [train.ipynb](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/train.ipynb)
- [drowsiness_detector.py](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/drowsiness_detector.py)
- [model.tflite](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/model.tflite)

### Dataset
The model uses a combination of 2 datasets to improve the accuracy. These datasets are -
- https://www.kaggle.com/prasadvpatil/mrl-dataset (2000 open eye images and 2000 closed eye images)
- https://www.kaggle.com/serenaraju/yawn-eye-dataset-new (Dataset used partially, i.e, only the closed and open eye images were used. 726 open eye images and 726 closed eye images)

The total number of images used -
- 2726 open eye images
- 2726 closed eye images

### Usage
1. Clone this repository.
```
git clone https://github.com/Saransh-cpp/IIITD_ALIVE_DSM
```
2. Run [train.ipynb](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/train.ipynb) to re-train the model (the model is already trained).
3. To start the live video feed for drowsiness detection, run -
```
cd IIITD_ALIVE_DSM
python drowsiness_detector.py
```
4. To stop the live feed press `q`.


### Model architecture
- The training step uses `Transfer Learning` with `VGG19`.
- Last layer of `VGG19` has been removed and a `Flatten` layer with a new output layer has been added.
- The model uses `adam` optimizer and `categorical_crossentropy` loss function.

The [train](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/train.ipynb) notebook is very well documented.

### Drowsiness setector in action (screenrecording)

https://user-images.githubusercontent.com/74055102/148997410-5392039c-364d-4a47-9702-9685a0fe7daf.mp4

## Tasks
### Task 1
The model has been trained and converted into `tflite` format in the [train](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/train.ipynb) notebook. The trained `tflite` model is also present [here](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/model.tflite).

### Task 2
Drowsiness detector to run on live video feed has been created in [drowsiness_detector.py](https://github.com/Saransh-cpp/IIITD_ALIVE_DSM/blob/main/drowsiness_detector.py).
