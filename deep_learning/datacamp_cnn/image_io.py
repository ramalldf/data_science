#Matplotlib operations

# Import matplotlib
import matplotlib.pyplot as plt

# Load the image
data = plt.imread('bricks.png')

# Display the image
plt.imshow(data)
plt.show()

#==Assigning Colors to Pixels==
# In an RBG image, the last index is the channel you work with
# Set the red channel in this part of the image to 1
data[:10,:10,0] = 1

# Set the green channel in this part of the image to 0
data[:10,:10,1] = 0

# Set the blue channel in this part of the image to 0
data[:10,:10,2] = 0

# Visualize the result
# Since only the red channel had a nonzero value (and the pixel
# coordinates overalpped), youll end up with a red block
# (if any other channel had a value it wouldnt just be red)
plt.imshow(data)
plt.show()

