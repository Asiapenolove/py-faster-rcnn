import h5py
import os
import numpy
mat_file=os.path.join(os.getcwd(), '..','wider_face_split','v1','wider_face_train.mat')
mat_f = h5py.File(mat_file,'r')


event_list = mat_f.get('event_list')
file_list = mat_f.get('file_list')
face_bbx_list = mat_f.get('face_bbx_list')

for event_idx, event in enumerate(event_list.value[0]):
    dir_name = mat_f[event].value.tostring().decode('utf-16')
    for im_idx, im in enumerate(mat_f[file_list.value[0][event_idx]].value[0]):
        # loop each image's name
         im_name = mat_f[im].value.tostring().decode('utf-16')
         print os.path.join(dir_name, im_name)
         bbox = mat_f[mat_f[face_bbx_list.value[0][event_idx]].value[0][im_idx]].value
         bshape= bbox.shape
         print bshape[1]
         for i in range(bshape[1]):
             strtemp=""
             for xywh in range(4): 
                strtemp+=str(int(bbox[xywh,i]))
                if(xywh!=3):
                    strtemp+=" "
             print strtemp
