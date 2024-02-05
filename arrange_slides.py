# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:36:06 2024

@author: Hussain Ahmad Madni
"""

import os
import shutil
from pandas import read_csv

source_path = '/lus/grand/projects/mayopath/data/TCGA/TCGA_slides'
dest_path = 'tcga_svs_slides'

csv_path = 'dataset_csv.csv'
csv_data = read_csv(csv_path)
slide_list = csv_data['slide_id'].tolist()

for slide_folder in os.listdir(source_path):
    slide_misc_path = os.path.join(source_path, slide_folder)
    for slide_misc in os.listdir(slide_misc_path):
        if slide_misc.split('.')[-1] == 'svs' and slide_misc in slide_list:
            slide_full_path = os.path.join(slide_misc_path, slide_misc)
            destination_path = os.path.join(dest_path, slide_misc)
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {slide_misc}")
            except Exception as e:
                print(f"Error moving {slide_misc}: {e}")