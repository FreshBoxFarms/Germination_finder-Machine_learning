# Germination_finder-Machine_learning

Input Image:
![Input image](https://user-images.githubusercontent.com/121043136/230652496-d650cea5-70a1-4c41-b115-bba629e9a66e.PNG)

HSV adjustment Menubar:
![HUV value adjstment menubar](https://user-images.githubusercontent.com/121043136/230652668-f17c9120-5e51-4537-a647-22a0f385de1d.PNG)

Output result::
![identified plant clount number](https://user-images.githubusercontent.com/121043136/230652734-66686c1c-14ef-4799-aa4a-0941156838ac.PNG)


This code is an implementation of a computer vision application that processes an input image and detects plants in it using color and contour detection. The application allows the user to adjust the color range and blur parameters using trackbars, and see the result in real-time.

When the code is executed, it loads an image called "Knipsel.png" using the cv2.imread() function. It then initializes the color range and blur parameters, and creates trackbars using the cv2.createTrackbar() function to allow the user to adjust the parameters.

The update_range() and update_blur() functions are called whenever the user adjusts the trackbars. These functions update the global variables lower_color, upper_color, and blur_kernel_size based on the values of the trackbars. They then call the update_result() function to update the result image based on the new parameters.

The update_result() function first applies a Gaussian blur to the input image using the cv2.GaussianBlur() function, and then converts the image from the BGR color space to the HSV color space using the cv2.cvtColor() function. It then applies a mask to the image based on the lower and upper color range specified by the user using the cv2.inRange() function.

Next, it finds the contours of the objects in the masked image using the cv2.findContours() function. It filters the contours based on their area to exclude small noise using the cv2.contourArea() function. It then draws the contours of the detected plants on the result image using the cv2.drawContours() function, and updates the plant count display using the cv2.putText() function.

Finally, the update_result() function shows the result image using the cv2.imshow() function.

The user can adjust the trackbars to change the color range and blur parameters, and see the effect on the result image in real-time. The original and result images are displayed using the cv2.imshow() function. The user can close the windows by pressing any key on the keyboard.

Overall, this code provides a simple and interactive way to detect plants in an image using color and contour detection techniques.





