# Custom_dataset_object_detection_using_Yolov3_darknet


## Saya disini menggunakan Google colab

kita akan mengimplemntasikan Yolov3 pada python 3 menggunakan darknet (framework). model ini akan menghasilkan bounding box dan mengklasifikasi 


The repository includes:
* konversi XML to txt (yolo format)
* mengatur data config (obj.names, obj.data, yolov3_custom.cfg,yolov3_detect_custom.cfg)
* training codes menggunakan google colab
* testing codes menggunakan google colab
* Evaluation codes menggunakan google colab (mAP dan FPS)



# Getting Started
* Bounding box setiap gambar dengan menggunakan LabelImg (jika belum mempunyai data)
* convert XML to txt
* training 
* testing
* evaluasi

## Preparasi data seperti berikut

download repositories ini dan download yolov3 dan darknet dibawah

Yolov3  =  
darknet =  

upload data diatas ke google colab seperti gambar berikut:

![Pastikan peletakan data seperti berikut ](assets/6.png)


# step to convert XML to Csv 

## 1. Open xml_to_text.py untuk mnegkonversi
* buka code xml_to_txt.py (just make sure the path right)
![coding konversi xml to txt](assets/2.png)

file xml dan jpg diletakkan dalam satu folder dan di convert ke txt
![file yang akan convert](assets/4.png)

file xml sudah di convert ke txt 

![hasil convert](assets/1.png)


* letakkan file txt dan jpg dalam satu folder yang sama, lalu jadikan file zip dengan nama obj
![Object Detection Sample(segera)](assets/7.png)


## 2. Persiapan Train
* Upload semua file kedalam google drive
![Object Detection Sample(segera)](assets/6.png)

* folder dalam yolov3 :
![Object Detection Sample(segera)](assets/5.png)

* ubah jumlah clases didalam obj.data sesuai dengan jumlah kelas yang digunakan

![Object Detection Sample(segera)](assets/9.png)

* ubah nama kelas sesuai dengan nama kelas yang digunakan

![Object Detection Sample(segera)](assets/10.png)

* ubah config dalam yolov3_custom.cfg





# Step to train  with your own data

## 1. train own dataset
Buka file YOLOv3.ipynb dengan menggunakan google colab
![Object Detection Sample(segera)](assets/13.png)



First we must register out dataset and define the label name

![Register Dataset #1](assets/3.PNG)

![Register Dataset #2](assets/4.PNG)

then we the part u must change is config for train model

![Train Model](assets/5.PNG)

## 2. Execute all program 
just run all part and get the result

## 3. result like this

![Result ](assets/6.PNG)



