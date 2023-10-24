import numpy as np
from numpy.linalg import norm
import pickle
from tqdm import tqdm, tqdm_notebook
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
    feature_list = pickle.load(open('/media/hdd/kalilinux/GITHubProjects/djangomage/trained-models/features-flickr-resnet.pickle',
                                'rb'))
    # root_dir_dataset = Path(str(settings.MEDIA_ROOT),'/Flickr_32')
    
    root_dir_dataset = '/media/hdd/kalilinux/GITHubProjects/djangomage/media/Flickr_32'
    filenames = []
    relFilenames = []
    distances = []
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
        start = settings.BASE_DIR
        for filename in sorted(glob.glob('/media/hdd/kalilinux/GITHubProjects/djangomage/media/Flickr_32/**/*.jpg', recursive=True)):
            self.filenames.append(filename)
        
        for imagename in self.filenames:
            relpath = os.path.relpath(imagename, start)
            self.relFilenames.append(relpath)
        return self.relFilenames
    
    def classNames(self):
        classNames = os.listdir('/media/hdd/kalilinux/GITHubProjects/djangomage/media/Flickr_32')
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
    
    def get_file_list(self):
        extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']
        file_list = []
        for root, directories, filenames in os.walk(self.root_dir_dataset):
            for filename in filenames:
                if any(ext in filename for ext in extensions):
                    filepath = os.path.join(root, filename)
                    if os.path.exists(filepath):
                      file_list.append(filepath)
                    else:
                      print(filepath)
        return file_list


    
    def getDistanceInfo(self):
        neighbors = NearestNeighbors(n_neighbors=len(self.feature_list),
                             algorithm='brute',
                             metric='euclidean').fit(self.feature_list)
        distances, indices = neighbors.kneighbors(self.feature_list)

        # # Calculating some stats
        # print("Median distance between all photos: ", np.median(distances))
        # print("Max distance between all photos: ", np.max(distances))
        # print("Median distance among most similar photos: ",
        #       np.median(distances[:, 2]))
        median_dist_all_photo = np.median(distances)
        max_dist_all_photo = np.max(distances)
        median_dist_allsimilar_photo = np.median(distances[:, 2])
        return median_dist_all_photo, max_dist_all_photo, median_dist_allsimilar_photo
        
    # Helper function to get the classname
    def getClassname(self, str):
        return str.split('/')[-2]
    
    # Helper function to get the classname and filename
    def getClassname_filename(self, str):
        return str.split('/')[-2] + '/' + str.split('/')[-1]

    

    def calculate_accuracy(self):
        num_nearest_neighbors = 5
        correct_predictions = 0
        incorrect_predictions = 0
        neighbors = NearestNeighbors(n_neighbors=num_nearest_neighbors,
                                     algorithm='brute',
                                     metric='euclidean').fit(self.feature_list)
        for i in tqdm(range(len(self.feature_list))):
            distances, indices = neighbors.kneighbors([self.feature_list[i]])
            for j in range(1, num_nearest_neighbors):
                if (self.getClassname(str(self.filenames[i])) == self.getClassname(
                        self.filenames[indices[0][j]])):
                    correct_predictions += 1
                else:
                    incorrect_predictions += 1
                    
            accuracy = round(100.0 * correct_predictions /
                      (1.0 * correct_predictions + incorrect_predictions), 2)
            
            precision = round(100.0 * correct_predictions /
                      (1.0 * correct_predictions + (incorrect_predictions)), 2)
            recall = round(100.0 * correct_predictions /
                      (1.0 * correct_predictions + (incorrect_predictions)), 2)
            f1score = round(100.0 * 2*correct_predictions /
                      (2.0 * correct_predictions + (incorrect_predictions)), 2)
            
        return accuracy, precision, recall, f1score


        