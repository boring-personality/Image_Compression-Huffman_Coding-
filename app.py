import cv2
import numpy as np
from Huffman import Huff

image=cv2.imread("lena1.png",0)
obj=Huff(image)
root=obj.CreateTree()
obj.Code(root)
coded_image=obj.encode()
temp=0
for code in coded_image:
    temp+=len(code)

average_length=temp/len(coded_image)
print("Average length of code is ",average_length,"bits")

cv2.imshow("OriginalImage",image)
cv2.waitKey()

shape=image.shape
original_size=(shape[0]*shape[1])/1024               #in Kb
print("Size of the image is ",original_size,"Kb")

comp_size=(temp/8)/1024             #for Kb
print("Size after compression is ",comp_size,"Kb")

ret=obj.decode(root)
ret=np.array(ret,np.uint8)
ret_image=np.reshape(ret,shape)
cv2.imshow("RetrivedFromCompression",ret_image)
cv2.waitKey()
cv2.destroyAllWindows()
print("Compression Ratio is ",8/average_length)
