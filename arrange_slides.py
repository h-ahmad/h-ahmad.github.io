# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:36:06 2024

@author: Hussain Ahmad Madni
"""

import os
import shutil

source_path = 'tcga_svs'
dest_path = 'tcga_svs_slides'
for slide_folder in os.listdir(source_path):
    slide_misc_path = os.path.join(source_path, slide_folder)
    for slide_misc in os.listdir(slide_misc_path):
        if slide_misc.split('.')[-1] == 'svs':
            slide_full_path = os.path.join(slide_misc_path, slide_misc)
            destination_path = os.path.join(dest_path, slide_misc)
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {slide_misc}")
            except Exception as e:
                print(f"Error moving {slide_misc}: {e}")