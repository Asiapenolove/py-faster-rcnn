#!/bin/bash

# 

case "$1" in
   "") echo "Not given dataste , using FDDB..." 
        dataset="FDDB";
        SetFolder="FDDB_2010";
   ;;
   "FDDB") echo "using FDDB ..." 
        dataset="FDDB";
        SetFolder="FDDB_2010";
   ;;
   "WIDER") echo "using WIDER ..." 
        dataset="WIDER"
        SetFolder="WIDER_2016"
   ;;
   *) echo "dataset $1 unknown"
        exit 1;
   ;;
esac


# check folder exist or not
cwd=$PWD
DIRECTORY="$cwd/data/FacesDevkit2017"
DIRECTORY_FDDB="$cwd/data/FacesDevkit2017/$SetFolder"

if [ -d "$cwd/data/scripts/Face_dataset_scripts/$dataset" ]; then
    if [ ! -d "$DIRECTORY" ]; then
        echo "the FaceDevkit2017 doesn't exist."
        echo "Create one, and fetching FDDB dataset..."
        mkdir $DIRECTORY;
    fi
else
    echo "folder data/scripts/Face_dataset_scripts/$dataset not found"
    echo "make sure you execute this shell in FRCN_ROOT!"
    echo "i.e. ~ooxx/py-faster-rcnn$ ./data/scripts/get_FaceData.sh [dataset]"
    exit 1
fi

if [ ! -d "$DIRECTORY_FDDB" ]; then
        # get the dataset
        cd $cwd/data/scripts/Face_dataset_scripts/$dataset;
        ./get_data.sh;

        # creating folder FDDB_2010/WIDER_2017 contatins:
        #    Annotations /JpgeImages / Imagesets
        cd pyxml;
        ./runit.sh;

        # move FDDB_2010/WIDER_2017 to FacesDevkit
        mv $SetFolder $DIRECTORY_FDDB
        mkdir -p $DIRECTORY/results/$SetFolder/Main
else
    echo "the FacesDevkit2017/$SetFolder already exist." 
fi

