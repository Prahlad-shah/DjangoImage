import numpy as np
from numpy.linalg import norm
import pickle
# from tqdm import tqdm, tqdm_notebook
import os
import random
import time
import math
import tensorflow
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.mobilenet import MobileNet
from keras.applications.inception_v3 import InceptionV3
from keras.models import Model
from keras.layers import Input, Flatten, Dense, Dropout, GlobalAveragePooling2D
from keras.applications.resnet50 import ResNet50, preprocess_input
from django.conf import settings
from pathlib import Path
import PIL
from PIL import Image
from sklearn.neighbors import NearestNeighbors
import glob

class ExtractFeatureUpload():
    feature_list = pickle.load(open('/media/hdd/kalilinux/projects/website_projects/src/IMG_Classifier/trained-models/features-flickr-resnet.pickle',
                                'rb'))
    root_dir = Path(str(settings.MEDIA_ROOT),'/Flickr_32')
    filenames = []
    relFilenames = []
    def __init__(self):
        self.model = ResNet50(weights='imagenet',
                 include_top=False,
                 input_shape=(224, 224, 3),
                pooling='max')
        

    def extract_features(self, img_path):
        input_shape = (224, 224, 3)
        img = image.load_img(img_path,
                             target_size=(input_shape[0], input_shape[1]))
        img_array = image.img_to_array(img)
        expanded_img_array = np.expand_dims(img_array, axis=0)
        preprocessed_img = preprocess_input(expanded_img_array)
        features = self.model.predict(preprocessed_img)
        flattened_features = features.flatten()
        normalized_features = flattened_features / norm(flattened_features)
        return normalized_features

    def fileNamesOfData(self):
        start = '/media/hdd/kalilinux/projects/website_projects/src/IMG_Classifier'
        for filename in sorted(glob.glob('/media/hdd/kalilinux/projects/website_projects/src/IMG_Classifier/media/Flickr_32/**/*.jpg', recursive=True)):
            self.filenames.append(filename)
        
        for imagename in self.filenames:
            relpath = os.path.relpath(imagename, start)
            self.relFilenames.append(relpath)
        return self.relFilenames
    
    def classNames(self):
        classNames = os.listdir('/media/hdd/kalilinux/projects/website_projects/src/IMG_Classifier/media/Flickr_32')
        return sorted(classNames)
    
    def featureListAttributes(self):
        num_images = len(self.filenames)
        num_of_features_length_of_all = len(self.feature_list)
        num_features_per_image = len(self.feature_list[0])
        return num_images, num_features_per_image, num_of_features_length_of_all
    
    def knnMethod(self, feature_user_image):
        fileindex = []
        neighbors = NearestNeighbors(n_neighbors=15,
                             algorithm='brute',
                             metric='euclidean').fit(self.feature_list)
        distances, indicess = neighbors.kneighbors([feature_user_image])
        for i in range(0, 14):
            fileIndex = self.relFilenames[indicess[0][i]]
            fileindex.append(fileIndex)
        return fileindex
    
        