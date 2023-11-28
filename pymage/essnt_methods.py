from io import BytesIO
from PIL import Image
from django.conf import settings
from pathlib import Path
import os

from datetime import datetime

class EssentialMethodsClass():
    base_dir = settings.BASE_DIR
    media_dir = settings.MEDIA_ROOT

    def get_Uploaded_Image(self, upload_image):
        buffer = BytesIO()
        buffer.write(upload_image.read())
        buffer.seek(0)
        img = Image.open(buffer)  # PIL image
        return img
    
    
    def getrelativePathMediaTemplate(self, full_path, exclude_path):
        relpath = os.path.relpath(full_path, exclude_path)
        return relpath  

# importing pandas as pd
import pandas as pd
import glob
import os
class ConvertCSV():
    
    def __init__(self) -> None:
        csvpath = settings.BASE_DIR
        data_dict = pd.read_csv(Path(str(csvpath)+'/trained-models/projectdata.csv', usecols=['BrandName', 'ImageURL']))

    def convertCSVFile(self):
        start_path = os.path.abspath('/media/hdd/kalilinux/GITHubProjects/djangomage')
        filenames = []
        for filename in sorted(glob.glob('/media/hdd/kalilinux/GITHubProjects/djangomage/media/Flickr_32/**/*.jpg', recursive=True)):
            filenames.append(filename)

        for imagefile in filenames:
            relpath = os.path.relpath(imagefile, start_path) 
            brand = relpath.split('/') 
            self.brand_names.append(brand[-2])
            self.image_relpath.append(relpath)      
        # print(brand_names)

        data_dict = {'BrandName':self.brand_names, 'ImageURL':self.image_relpath}
        df = pd.DataFrame(data_dict)
        return df.to_csv('projectdata.csv')
        
    def searchBrandsName(name = 'adidas'):
        csvpath = settings.BASE_DIR
        data_dict = pd.read_csv(Path(str(csvpath)+'/trained-models/projectdata.csv', usecols=['BrandName', 'ImageURL']))        
        brand_names = data_dict['BrandName']
        BName_result_list = []
        for bname in brand_names:
            if name in bname:
                BName_result_list.append(bname)
                
        # print(BName_result_list)
        return BName_result_list
            
        
            
    def searchURLImage(name = 'adidas'):
        csvpath = settings.BASE_DIR
        data_dict = pd.read_csv(Path(str(csvpath)+'/trained-models/projectdata.csv', usecols=['BrandName', 'ImageURL']))        
        URL_result_list = []
        urls = data_dict['ImageURL']
        for url in urls:
            if name in url:
                URL_result_list.append(url)
        
        # print(URL_result_list)
        return URL_result_list


        
        
      
		

    