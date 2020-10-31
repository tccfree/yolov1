import voc
import cv2
import os

image_dir = 'data/VOC_allimgs/'
label_txt = ['data/voc2007.txt', 'data/voc2012.txt']
val_label = 'data/voc2007test.txt'

tot = 0
c = 0
miss = []
for i in range(1):
    with open(val_label) as f:

        for j, line in enumerate(f.readlines()):
            c+=1
            splitted = line.strip().split()
            fname = splitted[0]
            path = os.path.join(image_dir, fname)

            try:
                img  = cv2.imread(path)
                h,w,_ = img.shape
            except:
                tot += 1
                miss.append((i, j, fname))
print(miss)
print(tot,c)

