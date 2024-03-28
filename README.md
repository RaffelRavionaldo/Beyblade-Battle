Model : YOLOv8 Nano Version

Video : https://drive.google.com/file/d/1sWPt_fqvK82YPGzzOqg-BkOyBNMsog1h/view?usp=sharing

Before running my code, don't forget to install ultralytics library with this syntax: pip install ultralytics

-----------------------------------------------------------------------------------------------------------

## 1. Collect Data

I downloaded a YouTube video and extracted the image from the video from my code called extract_picture.py, In my code I defined a variable called frame_total to get 150 images, you can change it with another integer value.

## 2. Label data

After we get images from the video, we label them with labelImg repo that you can access via this link : https://github.com/HumanSignal/labelImg. from labeling we get the txt file that contains object classes and the position of the object we want to detect before we run the repo, don't forget to prepare classes.txt that contains the name of the object you want to detect.

## 3. Split data

After label the image, we need to split the dataset into 3 folders, train, val and test, every folder have another 2 folder too to save images and labels, so the structure will like this :

-- Train

---- Images

-------- img_1.jpg

---- Labels

-------- img_1.txt

-- Test

..........................

## 4. Train the model.

Before we train the model, we need to create the yaml file, the structure look like this :

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/3f9b8a92-4db1-4e75-ba2c-fa2c3a0ca3e3)

with :

1. names : name of the object you want to detect (just copy and paste from classes.txt on step 2)
2. nc : number of classes that you want to detect
3. train, test and val is location of folder train, test and val from step 3.


