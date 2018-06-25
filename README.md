# ImageAI-image-Prediction
A python library built to empower developers to build applications and systems with self-contained Computer Vision capabilities.

ImageAI is a python library built to empower developers to independently build applications and systems with self-contained Computer Vision capabilities. Built with simplicity in mind, ImageAI supports a list of state-of-the-art Machine Learning algorithms for image recognition, object detection, custom object detection, video object detection, video object tracking, custom image recognition training and custom prediction. Eventually, ImageAI will provide support for a wider and more specialized aspects of Computer Vision including and not limited to image recognition in special environments and special fields and custom image prediction.\

Note :
First download the below Dependencies

TABLE OF CONTENTS
▣ First Prediction

▣ Prediction Speed

▣ Image Input Types

▣ Multiple Images Prediction

▣ Prediction in MultiThreading

▣ Documentation

https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Prediction

ImageAI provides 4 different algorithms and model types to perform image prediction. To perform image prediction on any picture, take the following simple steps. The 4 algorithms provided for image prediction include SqueezeNet, ResNet, InceptionV3 and DenseNet. Each of these algorithms have individual model files which you must use depending on the choice of your algorithm. To download the model file for your choice of algorithm, click on any of the links below: 

- SqueezeNet (Size = 4.82 mb, fastest prediction time and moderate accuracy) 
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/squeezenet_weights_tf_dim_ordering_tf_kernels.h5
- ResNet50 by Microsoft Research (Size = 98 mb, fast prediction time and high accuracy)
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_weights_tf_dim_ordering_tf_kernels.h5
- InceptionV3 by Google Brain team (Size = 91.6 mb, slow prediction time and higher accuracy) 
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/inception_v3_weights_tf_dim_ordering_tf_kernels.h5
- DenseNet121 by Facebook AI Research (Size = 31.6 mb, slower prediction time and highest accuracy) 
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/DenseNet-BC-121-32.h5

1. ImagePrediction

FirstPrediction.py

Great! Once you have downloaded this model file, start a new python project, and then copy the model file to your project folder where your python files (.py files) will be . Download the image below, or take any image on your computer and copy it to your python project's folder. Then create a python file and give it a name; an example is FirstPrediction.py. Then write the code below into the python file: 


FirstPrediction.py
from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()


prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()


predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "1.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
print(eachPrediction + " : " + eachProbability)


Sample Result: 


convertible : 52.459555864334106

sports_car : 37.61284649372101

pickup : 3.1751200556755066

car_wheel : 1.817505806684494

minivan : 1.7487050965428352

The code above works as follows: 
from imageai.Prediction import ImagePrediction
import os

The code above imports the ImageAI library and the python os class. 
execution_path = os.getcwd()

The above line obtains the path to the folder that contains your python file (in this example, your FirstPrediction.py) . 

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
In the lines above, we created and instance of the ImagePrediction() class in the first line, then we set the model type of the prediction object to ResNet by caling the .setModelTypeAsResNet() in the second line and then we set the model path of the prediction object to the path of the model file (resnet50_weights_tf_dim_ordering_tf_kernels.h5) we copied to the python file folder in the third line.

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "1.jpg"), result_count=5 )
In the above line, we defined 2 variables to be equal to the function called to predict an image, which is the .predictImage() function, into which we parsed the path to our image and also state the number of prediction results we want to have (values from 1 to 1000) parsing result_count=5 . The .predictImage() function will return 2 array objects with the first (predictions) being an array of predictions and the second (percentage_probabilities) being an array of the corresponding percentage probability for each prediction.

for eachPrediction, eachProbability in zip(predictions, probabilities):
print(eachPrediction + " : " + eachProbability)
The above line obtains each object in the predictions array, and also obtains the corresponding percentage probability from the percentage_probabilities, and finally prints the result of both to console.




2. Multiple Images Prediction

You can run image prediction on more than one image using a single function, which is the .predictMultipleImages() function. It works by doing the following: 
- Define your normal ImagePrediction instance 
- Set the model type and model path 
- Call the .loadModel() function 
- Create an array and add all the string path to each of the images you want to predict to the array. 
- You then perform prediction by calling the .predictMultipleImages() function and parse in the array of images, and also set the number predictions you want per image by parsing result_count_per_image=5 (default value is 2) 

Find the sample code below: 

from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()


multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsResNet()
multiple_prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
multiple_prediction.loadModel()


all_images_array = []


all_files = os.listdir(execution_path)
for each_file in all_files:
if(each_file.endswith(".jpg") or each_file.endswith(".png")):
all_images_array.append(each_file)


results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)


for each_result in results_array:
predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
for index in range(len(predictions)):
print(predictions[index] + " : " + percentage_probabilities[index])
print("-----------------------")


In the above code, the .predictMultipleImages() function will return an array which contains a dictionary per image. Each dictionary contains the arrays for predictions and percentage probability for each prediction. 
Sample Result:


  

convertible : 52.459555864334106

sports_car : 37.61284649372101

pickup : 3.1751200556755066

car_wheel : 1.817505806684494

minivan : 1.7487050965428352

-----------------------

toilet_tissue : 13.99008333683014

jeep : 6.842949986457825

car_wheel : 6.71963095664978

seat_belt : 6.704962253570557

minivan : 5.861184373497963

-----------------------

bustard : 52.03368067741394

vulture : 20.936034619808197

crane : 10.620515048503876

kite : 10.20539253950119

white_stork : 1.6472270712256432

-----------------------



Documentation
imageai.Prediction.ImagePrediction class

The ImagePrediction class can be used to perform image prediction in any python application by instanciating it and calling the available functions below: 
- setModelTypeAsSqueezeNet() This function should be called should you chose to use the SqueezeNet model file for the image prediction. You only need to call it once. 
- setModelTypeAsResNet() This function should be called should you chose to use the ResNet model file for the image prediction. You only need to call it once. 
- setModelTypeAsInceptionV3() This function should be called should you chose to use the InceptionV3Net model file for the image prediction. You only need to call it once. 
- setModelTypeAsDenseNet This function should be called should you chose to use the DenseNet model file for the image prediction. You only need to call it once. 
- setModelPath() You need to call this function only once and parse the path to the model file path into it as a string. The model file type must correspond to the model type you set. 
- loadModel() You need to call this function once only before you attempt to call the predictImage() function .
This function receives an optional value which is "prediction_speed". The value is used to reduce the time it takes to predict an image, down to about 60% of the normal time, with just slight changes or drop in prediction accuracy, depending on the nature of the image. 
* prediction_speed (optional); Acceptable values are "normal", "fast", "faster" and "fastest" 

- predictImage() This function is used to predict a given image by receiving the following arguments: 
****** input_type (optional) , the type of input to be parsed. Acceptable values are "file", "array" and "stream" 
****** image_input , file path/numpy array/image file stream of the image. 
****** result_count (optional) , the number of predictions to be sent which must be whole numbers between 
1 and 1000. The default is 5. 
This function returns 2 arrays namely 'prediction_results' and 'prediction_probabilities'. The 'prediction_results' 
contains possible objects classes arranged in descending of their percentage probabilities. The 'prediction_probabilities' 
contains the percentage probability of each object class. The position of each object class in the 'prediction_results' 
array corresponds with the positions of the percentage possibilities in the 'prediction_probabilities' array. 

:param input_type: 
:param image_input: 
:param result_count: 
:return prediction_results, prediction_probabilities: 

- predictMultipleImages() This function is used to predict more than one image by receiving the following arguments: 
****** input_type , the type of inputs contained in the parsed array. Acceptable values are "file", "array" and "stream" 
****** sent_images_array , an array of image file paths, image numpy array or image file stream 
****** result_count_per_image (optionally) , the number of predictions to be sent per image, which must be whole numbers between 1 and 1000. The default is 2. 

This function returns an array of dictionaries, with each dictionary containing 2 arrays namely 'prediction_results' and 'prediction_probabilities'. The 'prediction_results' contains possible objects classes arranged in descending of their percentage probabilities. The 'prediction_probabilities' contains the percentage probability of each object class. The position of each object class in the 'prediction_results' array corresponds with the positions of the percentage possibilities in the 'prediction_probabilities' array. 

:param input_type: 
:param sent_images_array: 
:param result_count_per_image: 
:return output_array: 
