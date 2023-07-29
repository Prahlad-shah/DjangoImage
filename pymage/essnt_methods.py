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
    
    
		

    