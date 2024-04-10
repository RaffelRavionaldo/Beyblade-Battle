Model : YOLOv8 Nano Version

Video input : https://drive.google.com/file/d/1sWPt_fqvK82YPGzzOqg-BkOyBNMsog1h/view?usp=sharing

Video output : https://drive.google.com/file/d/1SXSWvfkxsb4-xOuETEB4CNhJJ0gpr9aR/view?usp=sharing

Dataset for training : https://drive.google.com/drive/folders/1S083U2eWm-EKZyTFqF3EcCqRNYWtxQ2F?usp=sharing

Before running my code, don't forget to install ultralytics library with this syntax: pip install ultralytics

notes for code : 
1. run.ipynb = the code to detect the winner between 1vs1 beyblade.
2. train.ipynb = the code to train yolov8.
3. extract_pict.py = the code to extract images from video.

notes for output :
1. winner.jpg : The image of the winner Beyblade.
2. losser.jpg : The image of the losser Beyblade.
3. kondisi terakhir.jpg = The last frame processed before the battle ended.
4. battle_result.csv : CSV file that contains battle time (on seconds), location of the winner and loser on the battle, and the reason for the winner (is because the opponent is out of the arena (musuh keluar arena), stopped spinning (musuh berhenti berputar) or the owner the the beyblade (musuh diambil).
5. best.pt : The yolov8 nano weight after training the model with our data.

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

Before we train the model, we need to create the yaml file, the structure looks like this :

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/3f9b8a92-4db1-4e75-ba2c-fa2c3a0ca3e3)

with :

1. names : name of the object you want to detect (just copy and paste from classes.txt on step 2)
2. nc : number of classes that you want to detect
3. train, test, and val is the location of the folder train, test, and val from step 3.

For the code to train the model, you can see that at Train.ipynb, in this case, I train the model with 40 epochs, and here is the result for validation data :

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/12ce8c9f-1499-4caf-b4ee-733a067f5017)

we got a 0.6033 class loss which means is good.

## 5. Logic on The code.

To detect who the winner is between 1vs1 in Beyblade, you can see the code on run.ipynb

### A. The check_battle function.

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/cd472899-5e2d-4ad3-a263-b307ac5bc4f7)

is to check if there are already have 2 beyblades in the arena of battle, if yes we can get the starting of the battle.

### B. Create_Region function.

Is to define the area of the battle arena. we will use the coordinate to check on the is_out function, to call it you need to press D on your keyboard, click on 4 end points of the arena and then press F for save your arena coordinate.

### C. is_out function.

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/fc92fa1e-6d48-40bb-b883-13a9b10f82e2)

To know if any Beyblade gets out from the battle arena or not, we detect it with the cv2.pointpolygontest function, so if the Xcenter and Ycenter of all Beyblade on the polygon (in this case is the arena we draw in create_region function) all beyblade will get winner status, but if one of them get out from polygon so the status will change into lose.

### D. check_spin_status function.

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/cebe8e20-cec3-4c67-86b7-8d0ff804acfd)

Is like checking "The RPM" of the Beyblade, so if the Beyblade stops spinning, the value on the movement variable will be below 1, so that's why I define min_movement = 1.

After I give a short explanation of each function in my code, so now I will explain the main code.

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/1482814d-e3c5-4ee4-aca4-bf5a4d0e0c0a)

In the above code, we call the is_out function to get the status of 2 Beyblades, if the 2 Beyblades are still in the fight, we will get 2 winners in the kondisi dictionary, but if one of them is out we will get the 1 winner and 1 loser in kondisi dictionary, then we capture the winner and losses. the kondisi dictionary will be reset after checking because we will check the spin of Beyblade.

![image](https://github.com/RaffelRavionaldo/Kecilin-Beyblade-test/assets/94748637/be4dd80b-872b-4c63-8de6-536c40e9ea65)

The logic of this code is the same as the is_out condition.
