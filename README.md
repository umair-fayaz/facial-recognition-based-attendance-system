# Facial Recognition based Attendance System
This is a TensorFlow and OpenCV implementation of the face recognizer described in the paper ["FaceNet: A Unified Embedding for Face Recognition and Clustering"](http://arxiv.org/abs/1503.03832). The FaceNet TensorFlow implementation used is origionally done by [David Sandberg](https://github.com/davidsandberg/facenet). This project uses a nodeJS based server that acts as the front end, from where images of people can be uploaded and later processed for attendance. One image containing multiple faces can be processed at a time.
## Compatibility
The code is tested using Tensorflow r1.7.0 under Ubuntu 18.04.4 LTS with Python 2.7.17 and Python 3.6.9 and OpenCV 3.2.0
## Implementation
Clone my repo: 
```
git clone https://github.com/umair-fayaz/facial-recognition-based-attendance-system.git
```
**NOTE:** The file structure followed in this tutorial assumes the repo to be cloned as: 
```
/home/facial-recognition-based-attendance-system
```
Now as *facial-recognition-based-attendance-system* as the working directory, install all the requirements with the command:
```
pip install -r requirements.txt
```
The folders in the *[…]/data/images* directory are used for storing the testing and training image files (these are the pictures of people you’re trying to recognize).
## Steps
The following commands are formatted for the file structure I used, if you are using a different file structure modify them for your image and model directories.<br />
Set your python path variable to the src directory of your project (in my case the project is in *facial-recognition-based-attendance-system* folder in my home directory).
```
export PYTHONPATH=~/facial-recognition-based-attendance-system/src
```
### Training a model
In order to train a model, training images should be placed in *[…]/data/images/train_raw* folder under the name of the person to be trained. As an example, I have included a folder named *Kofi_Annan* in which raw images, containing only the pictures of him alone are kept. Similarly, a new folder is to be created by the name of person to be trained. Place at least 8 or 9 photos for better accuracy. <br /><br />
**NOTE:** Name of the folder should follow the *"Snake_Case"* naming style as the same named will be used as label later.
<br />
#### Align the training images:
Once the images for training are ready, before training, these images need to be alligned first. This is done as: 
```
python ~/facial-recognition-based-attendance-system/src/align/align_dataset_mtcnn.py \
~/facial-recognition-based-attendance-system/data/images/train_raw \
~/facial-recognition-based-attendance-system/data/images/train_aligned \
--image_size 160
```
#### Train a classifier
After the images are alligned, we now train a classifier on training images (this generates a pickle file containing the embeddings for the people you want to recognize):
```
python ~/facial-recognition-based-attendance-system/src/classifier.py TRAIN \
~/facial-recognition-based-attendance-system/data/images/train_aligned/ \
~/facial-recognition-based-attendance-system/models/20180402-114759.pb \
~/facial-recognition-based-attendance-system/models/my_classifier.pkl
```
### Running the attendance system
After performing the training, we can now run our system and start taking attendance. *[…]/src/students.py* file contains a dictionary in which student details are given. This is only for the purpose of testing the system. The file contains names of students. These names are same as the folders named for training. The attendance status is marked as "ABSENT" for all the names initially which is changed after a face is recognized with accuracy more than 0.5.
#### Running the server
A NodeJS based server is used which hosts a simple minimal HTML file for front end. This HTML page enables the client to upload a picture of people whose attendance is to be taken. These people should already be trained and their details should be present in *[…]/src/students.py* file. <br />
This enables the clients to use this system on any machine that has a browser and can render HTML files. Clients can make use of this system even on their smart phones.
##### Run
``` 
node server.js
```
The server runs on Port 3000. Test whether it is working open your browser and go to *http://localhost:3000/*. This should open a web page asking to upload an image.
#### Running Watchdog
Watchdog is a Python API library and shell utilitiy to monitor file system events. We use it to monitor *[…]/image_cache* folder. This is the folder where the images uploaded are saved. Watchdog API monitors this directory for the new images uploaded. Once it notices a new image uploaded, it triggers python script that starts detecting faces from the image and then feeding the faces to recognizer and finally performing attendance.
##### Installing Watchdog
You can use pip to install watchdog quickly and easily:
```
$ pip install watchdog
```
##### Running Watchdog
```
python watch_dog.py 
```
or
```
python3 watch_dog.py 
```
<br /> <br />
Once the server and Watchdog are up and running, the system is ready to use. Client uploades images, automatically detection and recognition will be performed and attendance will be returned.
