A project for binary classification of car photos into damaged and good (undamaged) categories using Keras with TensorFlow backend and sklearn.

This repository is structured as follows.

Scraper
-------

Contains a script used for scraping photos of cars with unrepairable damage from an auction site.

Data Analysis
-------------

Contains Jupyter Notebooks describing the collected data and splitting it into training, validation and test datasets.

Edge Detection
--------------

Contains a Notebook experimenting with edge detection in car photos converted to grayscale. However, this approach has not been pursued.

Feature Extraction
------------------

Contains Notebooks extracting features from penultimate layers of pretrained VGG-19 and ResNet50 networks for subsequent training according to transfer learning approach. For the sake of convenience, extracted features for images from training and validation datasets have been saved.

SVM
---

Contains Notebooks detailing SVM classifier models with RBF and linear kernels trained on features extracted from VGG-19 and ResNet50.

NN
--

Contains Notebooks detailing single and multiple layer neural networks trained on features extracted from VGG-19 and ResNet50 to classify images.

Final Model
-----------

Contains a Notebook with a class that incapsulates the picked classifier (VGG-19 + linear SVM). Classifier's performance on the test set is also analysed. 

The resulting classifier can be run on any image with 3 color channels as in the example. A pickled trained SVM classifier is provided in the folder (svm_vgg_19.pkl) and should be downloaded to where the code is run. Pretrained weights for the VGG-19 network used for feature extraction will be downloaded by Keras automatically on running the code for the first time.
