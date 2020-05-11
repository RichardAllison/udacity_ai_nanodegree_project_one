# Udacity AI Programming with Python Nanodegree Program 
# Project 1: Use a Pre-trained Image Classifier to Identify Dog Breeds

## Project Goal
In this project you will use a created image classifier to identify dog breeds. We ask you to focus on Python and not on the actual classifier (We will focus on building a classifier ourselves later in the program).

### Description:
Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information.

Some people are planning on registering pets that **aren’t actual dogs**.

You need to use an already developed *`Python`* classifier to make sure the participants are dogs.

**Note, you DO NOT need to create the classifier. It will be provided to you. You will need to apply the Python tools you just learned to USE the classifier.**

###Your Tasks:
 - Using your Python skills, you will determine which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs".
 - Determine how well the "best" classification algorithm works on correctly identifying a dog's breed.
 - If you are confused by the term image classifier look at it simply as a tool that has an input and an output. The Input is an image. The output determines what the image depicts. (for example: a dog). Be mindful of the fact that image classifiers do not always categorize the images correctly. (We will get to all those details much later on the program).
 - Time how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more time to run and use more computational resources to run.

##Answers to Questions on Classify Uploaded Images
Questions to Answer regarding Uploaded Image Classification:
Once the program stops running and the results files appear in the workspace, open and review each of the three to answer the following questions:

1. **Did the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed? If not, report the differences in the classifications.**

Yes, all three correctly classified the breed of dog in Dog_01.jpg as "eskimo dog, husky"


2. **Did each of the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed of dog as that model architecture classified Dog_02.jpg? If not, report the differences in the classifications.**

Yes, all three correctly classified the breed of dog in Dog_02.jpg as "eskimo dog, husky"


3. **Did the three model architectures correctly classify Animal_Name_01.jpg and Object_Name_01.jpg to not be dogs? If not, report the misclassifications.**

Yes, all three model architectures correctly classified Macaw_01.jpg as "macaw" and Violin_01.jpg as "violin, fiddle".

4. **Based upon your answers for questions 1. - 3. above, select the model architecture that you feel did the best at classifying the four uploaded images. Describe why you selected that model architecture as the best on uploaded image classification.**

None of the architectures misclassified any of the uploaded images and all correctly identified the dog breed, therefore I am unable to make a conclusion on the basis of this small sample of data.

However based on the results of the classification of the pet_images directory (*Final Results* below), the VGG architecture was the most successful both in categorising dog images as dogs and in correctly identifying the breed of dog.

## Final Results

| Total Images | 40 |
| Dog Images | 30 |
| Not-a-dog Images | 10 |

| CNN Model Architecture | % Correct Not-a-dog | % Correct Dog | % Correct Breed | % Match Labels
| ----------- | ----------- | ----------- | ----------- | ----------- |
| ResNet | 90 | 100 | 90 | 90 | 82.5 |
| AlexNet | 100 | 100 | 80 | 75 |
| VGG | 100 | 100 | 93 1/3 | 87.5 |
