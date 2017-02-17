echo "[WIDER] check data setfolder exist" 

DIRECTORY="../wider_face_split/"
if [ ! -d "$DIRECTORY" ]; then
    echo "[WIDER] Oops ,It seems data not downloaded properly !"
    exit 1;
fi

DIRECTORY="../WIDER_train/"
if [ ! -d "$DIRECTORY" ]; then
    echo "[WIDER] Oops ,It seems data not downloaded properly !"
    exit 1;
fi

echo "[WIDER] Createing xywhfile....."
python mat_extract.py > xywhXfile.txt;

echo "[WIDER] Since WIDER is a larger dataset, it may take for a while"
echo "[WIDER] Createing WIDER_2016 fold, Images , Annotation xmls..."

start=`date +%s`
python anno2xml.py
end=`date +%s`

runtime=$((end-start))

rm xywhXfile.txt
echo "[WIDER] totally it takes :" $runtime "seconds"

#creating training testing set
python randomSet.py WIDER_2016 0.9
