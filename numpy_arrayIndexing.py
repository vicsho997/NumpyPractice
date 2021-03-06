""" Negative Indexing"""
#Use negative indexing to access an array from the end.
#Print the last element from the 2nd dim:
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) 



""" Access 3-D Arrays"""
#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
#Access the third element of the second array of the first array:
#Example Explained -https://www.w3schools.com/python/numpy_array_indexing.asp
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr1[0, 1, 2])


""" Access 2-D Arrays"""
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
#Access the 2nd element on 1st dim:
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr2[0, 1])

#Access the 5th element on 2nd dim:
arr3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd dim: ', arr3[1, 4]) 

"""Access Array Elements """
#Get the first element from the following array:
arr4 = np.array([1, 2, 3, 4])

print(arr4[0]) 
#Get the second element from the following array.
arr5 = np.array([1, 2, 3, 4])

print(arr5[1]) 
#Get third and fourth elements from the following array and add them.
arr6 = np.array([1, 2, 3, 4])

print(arr6[2] + arr6[3]) 