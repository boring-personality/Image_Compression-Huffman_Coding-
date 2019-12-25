#Huffman coding for image
import cv2
import numpy as np


class Node:
    def __init__(self,data,freq,left=None,right=None):
        self.data=data
        self.freq=freq
        self.left=left
        self.right=right

class Huff:
    def __init__(self,img):
        self.dict={}
        self.code=[]
        self.hist_dic={}
        self.img=img
        hist,bins = np.histogram(self.img.ravel(),256,[0,256])
        bins=bins.tolist()
        hist=hist.tolist()
        #Remove zeros
        for hist,bin in zip(hist,bins):
            self.hist_dic[bin]=hist
        dic=self.hist_dic.copy()
        for key in dic.keys():
            if self.hist_dic[key]==0:
                del(self.hist_dic[key])

        self.bins=self.hist_dic.keys()
        self.hist=[self.hist_dic[x] for x in self.bins]

    def CreateTree(self):
        charList=self.bins
        freqList=self.hist
        minHeap=[Node(c,f) for c,f in zip(charList,freqList)]

        while(len(minHeap)!=1):
            minHeap=sorted(minHeap,key=lambda x:x.freq,reverse=True)
            #print([x.freq for x in minHeap])
            #print([x.data for x in minHeap])
            intNode=Node(None,minHeap[-1].freq+minHeap[-2].freq)
            intNode.left=minHeap[-2]
            intNode.right=minHeap[-1]
            minHeap.pop()
            minHeap.pop()
            minHeap.append(intNode)

        return minHeap[0]

    def Code(self,tree,s=""):
        if tree.data is not None:
            print(tree.data,end=" ")
            print(s)
            self.dict[tree.data]=s
            return
        self.Code(tree.left,s+'0')
        self.Code(tree.right,s+'1')

    def encode(self):
        flat=self.img.flatten().tolist()
        for pix in flat:
            self.code.append(self.dict[pix])
        return self.code

    def decode(self,tree):
        current=tree
        self.string=[]
        for code in self.code:
            for bit in code:
                if bit=="0":
                    current=current.left
                else:
                    current=current.right

            if current.left==None and current.right==None:
                self.string.append(current.data)
                current=tree
        return self.string
