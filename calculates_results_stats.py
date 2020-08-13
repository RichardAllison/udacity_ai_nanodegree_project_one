#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Richard Allison
# DATE CREATED: 6 May 2020
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the program run using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    results_stats_dic = {}
    total_images = len(results_dic)
    dog_image_count = 0
    matches = 0                
    correctly_classified_as_dog = 0
    correctly_classified_as_not_dog = 0
    correctly_classified_dog_breed = 0
    for value in results_dic.values():
        if value[3] == 1:
            dog_image_count += 1
            if value[4] == 1:
                correctly_classified_as_dog += 1
                if value[2] == 1:
                    correctly_classified_dog_breed += 1
        elif value[3] == 0:
            if value[4] == 0:
                correctly_classified_as_not_dog += 1
        if value[2] == 1:
            matches += 1
            
    not_dog_image = total_images - dog_image_count
    incorrectly_classified_breed = (correctly_classified_as_dog
                                    - correctly_classified_dog_breed)
    
    #number of images
    results_stats_dic['n_images'] = total_images
    
    #number of dog images
    results_stats_dic['n_dogs_img'] = dog_image_count
    
    #number of NON-dog images
    results_stats_dic['n_notdogs_img'] = not_dog_image
    
    #number of matches between pet & classifier labels   
    results_stats_dic['n_match'] = matches
    
    #number of correctly classified dog images
    results_stats_dic['n_correct_dogs'] = correctly_classified_as_dog
    
    #number of correctly classified NON-dog images
    results_stats_dic['n_correct_notdogs'] = correctly_classified_as_not_dog
    
    #number of correctly classified dog breeds
    results_stats_dic['n_correct_breed'] = correctly_classified_dog_breed
    
    #percentage of correct matches
    results_stats_dic['pct_match'] = matches/total_images * 100
    
    if dog_image_count != 0:
        #percentage of correctly classified dogs
        results_stats_dic['pct_correct_dogs'] = (correctly_classified_as_dog
                                                 /dog_image_count * 100)
    
        #percentage of correctly classified dog breeds
        results_stats_dic['pct_correct_breed'] = (correctly_classified_dog_breed
                                                  /dog_image_count * 100)
    else:
        results_stats_dic['pct_correct_dogs'] = 0
        results_stats_dic['pct_correct_breed'] = 0
        
    #percentage of correctly classified NON-dogs
    if not_dog_image != 0:
        results_stats_dic['pct_correct_notdogs'] = (correctly_classified_as_not_dog
                                                    /not_dog_image * 100)
    else:
        results_stats_dic['pct_correct_notdogs'] = 0
    
    return results_stats_dic
