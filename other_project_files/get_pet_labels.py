#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Janeth Manyalla
# DATE CREATED: 12/4/2022                                
# REVISED DATE: 12/5/2022
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
#     results_dic = {}
#     indx = 0
#     string = ''
#     underscore_indx = 0
#     count = 0
#     underscore_list = []
#     for image in image_dir:
#         underscore_list = []        #resetting the list 
#         for i, c in enumerate(image):
#             if c.isdigit() and count==0:
#                 indx = i
#                 count += 1
#         count = 0
#         string = image[:indx-1].strip().lower()
        
#         for i in range(len(string)):
#             if string[i] == '_':
#                 underscore_list.append(i)
#         indx = 0
#         for j in range(len(underscore_list)):
#             if image not in results_dic:
#                 results_dic[image] = string[indx:underscore_list[j]]
#                 indx = underscore_list[j]
#             else:
#                 results_dic[image] = results_dic[image]+' '+string[indx+1:underscore_list[j]]
#                 indx = underscore_list[j]
                
#             if j == len(underscore_list)-1:
#                 results_dic[image] = results_dic[image]+' '+string[underscore_list[j]+1:]
#     return results_dic

#     results_dic = dict()
    
#     filename_list = listdir("pet_images/")
#     image_name_list = []
    
#     for idx in range(0, len(filename_list), 1):
#         image_name_list = filename_list[idx].split('_')
#         for name in image_name_list:
#             if name.isalpha():
#                 if filename_list[idx] not in results_dic:
#                     results_dic[filename_list[idx]] = [name.lower().strip()] 
#                 else:
#                     results_dic[filename_list[idx]][0] = results_dic[filename_list[idx]][0] + ' ' + name.lower().strip() 

    in_files = listdir(image_dir)
    
    results_dic = dict()
   
    for idx in range(0, len(in_files), 1):
       if in_files[idx][0] != ".":
           pet_label = ""
           for name in in_files[idx].split('_'):
                if name.isalpha():
                    if len(pet_label)==0:
                        pet_label += name.lower().strip()
                    else:
                        pet_label += ' '+name.lower().strip()
                        
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", in_files[idx])
    return results_dic
    
#     return results_dic
