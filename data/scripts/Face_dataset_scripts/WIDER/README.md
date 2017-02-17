# Five steps for creating DataSet

## step1 first download the dataset from WIDER dataset
http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/

Wider Face Training Images : WIDER_train.zip (~1.3GB)

Face annotations : wider_face_split.zip (~6MB)

## step2 git clone repository from github
```
git clone https://github.com/penolove/WIDER_DataSet_4_faster_rcnn.git
```

## step3 put those zips and put it into folder WIDER_DataSet_4_faster_rcnn like this:

![alt tag](https://raw.githubusercontent.com/penolove/WIDER_DataSet_4_faster_rcnn/master/zip_img.png)

and then execute  (unzip and checksum)

```
./get_data.sh
```

if always checksum fail just directly
```
FILE=wider_face_split.zip
unzip $FILE -d wider_face_split

FILE=WIDER_train.zip
unzip $FILE -d WIDER_train
```



## step4 run the script

```
cd pyxml_wider
./runit.sh
```

for my machine , it takes ~350 s.
the shell will create WIDER_2016 directory  contains JPEGImages/Annotations

## step5 after done the script
you can use labelImg to see if it deals properly(This is god dame awesome) [ref](https://github.com/tzutalin/labelImg)

![alt tag](https://raw.githubusercontent.com/penolove/WIDER_DataSet_4_faster_rcnn/master/WIDER.png)

## step6 clean data created during execution
```
make clean
```
