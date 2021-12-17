

from functions import *

img1_name = input("Enter the name of image 1: ")
img1 = cv2.imread(img1_name)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)


img2_name = input("Enter the name of image 2: ")
img2 = cv2.imread(img2_name)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


#Resizing the images to the same size
rows,columns = np.shape(img1[:,:,1])

if(np.shape(img1) != np.shape(img2)):
    img2 = cv2.resize(img2,(rows,columns))
    

Fused = fuse_images(img1,img2)

f = plt.figure(figsize=(12,16))

f.add_subplot(1,3,1)
imgplot(img1, "First Image")

f.add_subplot(1,3,2)
imgplot(img2, "Second Image")

f.add_subplot(1,3,3)
imgplot(Fused, "Fused Image")


# In[ ]:




