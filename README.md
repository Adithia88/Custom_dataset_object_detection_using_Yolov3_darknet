# Custom_dataset_object_detection_using_Yolov3_darknet


## Saya disini menggunakan Google colab

kita akan mengimplemntasikan Yolov3 pada python 3 menggunakan darknet (framework). model ini akan menghasilkan bounding box dan mengklasifikasi 

![Object Detection Sample(segera)](assets/1.png)

The repository includes:
* konversi XML to txt (yolo format)
* menatur data config (obj.names, obj.data, yolov3_custom.cfg,
* training codes menggunakan google colab
* 
* Evaluation on MS COCO metrics (AP) (Soon)
* Example of training on your own dataset



## Installation
1. Clone this repository

![Put file like this](assets/2.PNG)

2. download dataset here : https://drive.google.com/file/d/1USBWv96I3H5RfQ1lUYbwDgqgULJif3Ia/view?usp=sharing

# Getting Started
* convert XML to csv
* open Detectron2_custom_object_detection.ipynb (this code include all  Training, Testing and evaluation soon)


# step to convert XML to Csv 

## 1. Prepare dataset and make sure the path 
open code xml_to_csv.py (just make sure the path right)


# Step to train  with your own data

## 1. train own dataset
This example will explain which part u must change to train your own dataset. open Detectron2_custom_object_detection.ipynb 

First we must register out dataset and define the label name

![Register Dataset #1](assets/3.PNG)

![Register Dataset #2](assets/4.PNG)

then we the part u must change is config for train model

![Train Model](assets/5.PNG)

## 2. Execute all program 
just run all part and get the result

## 3. result like this

![Result ](assets/6.PNG)



