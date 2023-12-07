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



class RandomValues():
    
    def readFile(self):
        filenames = []
        start_path = os.path.abspath('/media/hdd/kalilinux/GITHubProjects/djangomage')
        filenames = []
        for filename in sorted(glob.glob('/media/hdd/kalilinux/GITHubProjects/djangomage/media/Flickr_32/**/*.jpg', recursive=True)):
            relpath = os.path.relpath(filename, start_path)
            filenames.append(relpath)
        return filenames
    
    def randomizeList(self, datalist:list):
        import random
        nologodata = []
        logolist =  []
        brandnamelist = []
        random_list = []
        randbrandlist = []
        for nologo in datalist:
            if 'no-logo' in nologo:
                nologodata.append(nologo)
            else:
                brandname = str(nologo).split('/')
                brandname = brandname[-2]
                brandnamelist.append(brandname)
                logolist.append(nologo)
                
        for x in range(10):
            randomdata = logolist[random.randint(0, len(logolist))]
            random_list.append(randomdata)

        for x in random_list:
            randomdatabrandname = str(x).split('/')
            randomdatabrandname = randomdatabrandname[-2]
            randbrandlist.append(randomdatabrandname)
        return random_list, randbrandlist


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
class WebScraping():
    def doCrawl(siteurl):
        pass
    
    def getBrandURL(brandname):
        urlpath = f'https://www.google.com/search?q={brandname}&oq={brandname}&gs_lcrp=EgZjaHJvbWUqBwgAEAAYjwIyBwgAEAAYjwIyGwgBEC4YQxiDARjHARjUAhixAxjRAxiABBiKBTIGCAIQRRhAMgwIAxAAGEMYgAQYigUyBggEEEUYPDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBCDE4NzVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'
        response = requests.get(urlpath)
        soup = BeautifulSoup(response.content, "html.parser")
        link_elements = soup.select("a[href]")
        URList = []
        links = []
        for x in link_elements:
            if brandname in str(x):
                URList.append(x.get('href'))
        for x in URList:
            if '/url?q=' in str(x):
                link = x.removeprefix('/url?q=')
                links.append(link)
        return links
        
            
    def getExactBrandURL(brandname):
        urlpath = f'https://www.google.com/search?q={brandname}&oq={brandname}&gs_lcrp=EgZjaHJvbWUqBwgAEAAYjwIyBwgAEAAYjwIyGwgBEC4YQxiDARjHARjUAhixAxjRAxiABBiKBTIGCAIQRRhAMgwIAxAAGEMYgAQYigUyBggEEEUYPDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBCDE4NzVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'
        response = requests.get(urlpath)
        soup = BeautifulSoup(response.content, "html.parser")
        link_elements = soup.find_all('a')
        URList = []
        for x in link_elements:
            if brandname in str(x):
                # print(x.get('href'))
                URList.append(x.get('href'))
        exactURL = URList[11], URList[12],URList[13],URList[14], URList[15], URList[16],URList[17],URList[18],URList[19],URList[20],URList[21],URList[22],URList[23],URList[24],URList[25],URList[26]
        return list(exactURL)
        
        
        

		

    