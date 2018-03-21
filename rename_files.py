# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:27:17 2017

@author: Fernando
"""

# Script to rename files
import os

def rename_files():
    list_files = os.listdir(r"C:\Users\Fernando\Documents\PYTHON\prueba")
    print(list_files)
    current_path = os.getcwd()
    print("the current directory is: %s" % (current_path))
    os.chdir(r"C:\Users\Fernando\Documents\PYTHON\prueba")
    
    for file_name in list_files:
        print("Old file name: %s" % (file_name))
        new_file_name = file_name.replace("MOD","mpg")
        os.rename(file_name,new_file_name)
        print("New file name: %s" % (new_file_name))
        #os.rename(file_name,file_name.replace("MOD","mpg"))

        # new_file = file_name + 'mpg'
        # print("New file name: %s" % (new_file_name))
    os.chdir(current_path)
      
        
rename_files()