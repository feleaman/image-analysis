import numpy as np
from PIL import Image
from sys import exit

# gradient between 0 and 1 for 256*256
array = np.linspace(0,1,256*256)

# reshape to 2d
mat = np.reshape(array,(256,256))
print(np.shape(mat))
print(type(mat))


# Creates PIL image
img = Image.fromarray(np.uint8(mat * 255) , 'L')
img.show()



cwt = np.array([[1, 1, 1, 1], [0, 0.5, 0, 0.5], [0.25, 0, 0.25, 0]])
print(np.shape(cwt))
print(type(cwt))
img = Image.fromarray(np.uint8(cwt * 255) , 'L')
img.show()