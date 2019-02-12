#Time complexity to build segment tree O(n) and space complexity O(n)
#Time complexity for range query O(log n)


from math import pow,log2,ceil
from sys import maxsize
#import sys
#sys.setrecursionlimit(100000)


def segment(low,high,pos):


    if (low==high):
        segment_tree[pos]=arr[low]
        return

    mid=(high+low)//2

    segment(low,mid,2*pos+1)
    segment(mid+1,high,2*pos+2)

    segment_tree[pos]=min(segment_tree[2*pos+1],segment_tree[2*pos+2])


def rangequery(qlow,qhigh,low,high,pos):

    


    if qlow<=low and qhigh>=high:
        return segment_tree[pos]

    elif qlow>high or qhigh<low:
        return maxsize

    else:
        mid=int((high+low)/2)
        
        xx=rangequery(qlow,qhigh,low,mid,2*pos+1)
        yy=rangequery(qlow,qhigh,mid+1,high,2*pos+2)
        
        return min(xx,yy)
        

arr=[1,2,3,4,-1,2,3,5,5,-5]
low=0
length=len(arr)
high=length-1
height=int(ceil(log2(length)))
pos=0 #root of segment tree
size_of_segment_tree=2*int(pow(2,height))-1
segment_tree=[0]*size_of_segment_tree
segment(low,high,pos)
querylow=int(input())
queryhigh=int(input())
if querylow<0 or queryhigh>size_of_segment_tree-1:
    print() ("Error 404! ")

print(rangequery(querylow,queryhigh,low,high,0)) #0 represents root of the node
