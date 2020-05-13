import numpy as np
import matplotlib.pyplot as plt

#create a list
my_list1 = [1,2,3,4]
print(my_list1)
type(my_list1)
for item in my_list1:
	print(type(item))

#create a array from list
my_array1 = np.array(my_list1)
print(my_array1)

#create a 2d list
my_list2 = [11,22,33,44]
my_list = [my_list1,my_list2]
print(my_list)

#create a 2d array
my_array = np.array(my_list)

#create a all-1 index
#my_array2=np.ones(10,10)

#orthogonal matrix
my_array2=np.eye(5)

#arane
my_array2=np.arange(20)

print(my_array2)

#data types
dt = np.dtype('float32')
#print(dt.name)

a = np.array([[0,0,0,0],[0,0,0,0]],dtype=np.dtype('f'))
print(a)

arr = np.arange(50).reshape((10,5))
arr1=arr.T#transpose

arr3d = np.arange(50).reshape((5,5,2))
print(arr3d)

points = np.arange(-5,5,0.01)
dx,dy=np.meshgrid(points,points)
z = (np.sin(dx) + np.sin(dy))
plt.imshow(z)
plt.colorbar()
plt.title('test')
plt.show()

arr = np.arange(5)
np.savetxt('calvin-array',arr,delimiter=",")
arr_1 = np.load('calvin-array.npy')