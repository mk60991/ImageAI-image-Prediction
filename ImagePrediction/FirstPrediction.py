# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 07:15:42 2018

@author: hp
"""

from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()


prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "C:\\Users\\hp\\Downloads\\ImageAI image Prediction1\\resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()


predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "C:\\Users\\hp\\Downloads\\ImageAI image Prediction1\\images\\1.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    
    
    print(eachPrediction + " : " + eachProbability)

