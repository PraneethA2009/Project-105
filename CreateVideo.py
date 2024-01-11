import os
import cv2


path = "C:/Users/Public/Documents/python/Projects/P105/Images"


Images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:

        file_name = os.path.join(path, file)
        

        print(file_name)
        

        Images.append(file_name)
count = len(Images)
frame = cv2.imread(Images[0])
width, height, channels = frame.shape
size = (width, height)
print(size)
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(count):

    img = cv2.imread(Images[i])
    out.write(img)
out.release()