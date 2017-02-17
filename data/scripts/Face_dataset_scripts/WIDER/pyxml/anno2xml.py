from lxml import etree
import sys
import cv2
import math
import glob
import os

cur_ind=0
target_dir=os.path.join(os.getcwd(), 'WIDER_2016')
target_dir_Jpg=os.path.join(target_dir,'JPEGImages')
target_dir_Ana=os.path.join(target_dir,'Annotations')

if not os.path.exists(target_dir):
    os.makedirs(target_dir)   

if not os.path.exists(target_dir_Jpg):
    os.makedirs(target_dir_Jpg)

if not os.path.exists(target_dir_Ana):
    os.makedirs(target_dir_Ana)   


target_dir_Jpg_set=os.path.join(target_dir_Jpg,'*.jpg')

outfileID=len(glob.glob(target_dir_Jpg_set))


def img2xml(path,objects,shape):
    root = etree.Element("annotation")
    folder = etree.SubElement(root, "folder")
    filename = etree.SubElement(root, "filename")
    source = etree.SubElement(root, "source")
    databases = etree.SubElement(source, "database")

    folder.text = "WIDER2017"
    filename.text = str(path).zfill(6)
    databases.text = "WIDER"

    size = etree.SubElement(root, "size")
    width = etree.SubElement(size,"width")
    height = etree.SubElement(size,"height")
    depth = etree.SubElement(size,"depth")
    depth.text = str(shape[2])
    width.text = str(shape[1])
    height.text = str(shape[0])

    obj_count=0
    for obj in objects:
        #object
        obj=[float(i) for i in obj.split()]
        #the smallest circumscribed parallelogram
        #[link] https://github.com/nouiz/lisa_emotiw/blob/master/emotiw/common/datasets/faces/FDDB.py
        xmin_ = int(obj[0])
        ymin_ = int(obj[1])
        xmax_ = int(obj[0]+obj[2])
        ymax_ = int(obj[1]+obj[3])
        
        # check if out of box
        if(xmin_ >0 and ymin_>0 and xmax_<shape[1] and ymax_<shape[0]):
            obj_count+=1
            object_=etree.SubElement(root, "object")
            name=etree.SubElement(object_, "name")
            name.text="face"
            pose=etree.SubElement(object_, "pose")
            pose.text="Unspecified"
            truncated=etree.SubElement(object_, "truncated")
            truncated.text="0"
            difficult=etree.SubElement(object_, "difficult")
            difficult.text="0"
            # bndbox
            bndbox=etree.SubElement(object_, "bndbox")
            xmin=etree.SubElement(bndbox,"xmin")
            ymin=etree.SubElement(bndbox,"ymin")
            xmax=etree.SubElement(bndbox,"xmax")
            ymax=etree.SubElement(bndbox,"ymax")
            xmin.text = str(xmin_)
            ymin.text = str(ymin_)
            xmax.text = str(xmax_)
            ymax.text = str(ymax_)
    if obj_count>0:
        et = etree.ElementTree(root)
        xml_output_path = os.path.join(target_dir_Ana,path+".xml")
        et.write(xml_output_path, pretty_print=True)
        return True
    else: 
        return False

  
# the annotation files path
originalPics_folds=os.path.join("..","WIDER_train","WIDER_train","images")

if __name__=="__main__":
    # you need to modify the path_img below
    # and the FDDB-fold-were assign by your own
    if len(sys.argv) < 2:
        file_path='xywhXfile.txt'
    elif len(sys.argv)==2:
        file_path=sys.argv[1]
    else:
        print "usage : python example.py [ellipseList]"
    current_file=open(file_path,'r')
    image_with_target=[i.replace('\n','') for i in current_file.readlines()]
    while (cur_ind<len(image_with_target)):
        path_img = os.path.join(originalPics_folds,image_with_target[cur_ind]+'.jpg')
        img = cv2.imread(path_img) 
        cur_ind+=1
        len_obj=int(image_with_target[cur_ind])
        cur_ind+=1
        objects=image_with_target[cur_ind:cur_ind+len_obj]
        cur_ind+=len_obj
        path=str(outfileID).zfill(6)
        if(img2xml(path,objects,img.shape)):
            image_output_path = os.path.join(target_dir_Jpg, path+".jpg")
            cv2.imwrite(image_output_path, img)
            outfileID+=1

