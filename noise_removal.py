'''
Salt and pepper noise on an image:
    Impulse noise - > Defects in camera pixels
    Noise is either max or min values in this case

Gaussian noise in image:
    Most of the real noise is like gaussian noise
    Distribution is gaussian in nature(uniformly distributed-> normal bell curve distributed)-
        Mean
        Standard Deviation

Techniques - 
    Smoothing- 
        Objective is to- Remove or reduce noise on image
        Linear smoothing transformations:
            Image averaging
            Local averaging
            Gaussian smoothing- edges get damaged

        Non Linear transformations:
            Rotating mask  
            Median filter-
                Uses the median value
                Not affected by noise
                Doesn't blur edges much
                Damages thin lines and sharp corners if any 

'''
#Converted C++ implementation into python from nicolei tutorials

import cv2
# set the maximum height value and the maximum pixel value as 255
max_value_h = 360/2
max_value = 255

#optional - store the image paths in some string 
path1 = "/sample_image.jpg"

#read the image and store it into some matrix
img  = cv2.imread(path1,cv2.IMREAD_COLOR)

cv2.resize(img,img,{500,500})

#check if image properly read or not
if(img.empty()):
    print("Could not properly read the image..")
    exit(0)

#make a lower bound vector -> list
#HSV -> Hue Saturation Value
lower_bound  = [170,80,50] #for trial and error
low_h = lower_bound[0], low_s = lower_bound[1], low_v= lower_bound[2]
high_h = max_value_h , high_s = max_value, high_v = max_value

#make new Matrix objects for hsvImg and imgThreshold
#converting from BGR to HSV colorspace
hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#to detect the object based on HSV range values
imgThreshold = cv2.inRange(hsvImg,(low_h,low_s,low_v),(high_h,high_s,high_v)) 

#making medianBlurImg and gaussianBlueImg
medianBlurImg = cv2.medianBlur(img,9) #9 is the size of kernel
gaussianBlurImg = cv2.GaussianBlur(img, (1,1),9,9)

cv2.imshow("Original image",img)
cv2.imshow("Median blurred image",medianBlurImg)
cv2.imshow("Gaussian blurred image",gaussianBlurImg)

#wait for a keystroke in the window and here the keystroke to destroy the window is q
k = cv2.waitKey(0)
if k == 'q':
    cv2.destroyAllWindows()

