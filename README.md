# Facial Recognition based Attendance System
This is a TensorFlow and OpenCV implementation of the face recognizer described in the paper ["FaceNet: A Unified Embedding for Face Recognition and Clustering"](http://arxiv.org/abs/1503.03832). The FaceNet TensorFlow implementation used is origionally done by [David Sandberg](https://github.com/davidsandberg/facenet). This project uses a nodeJS based server that acts as the front end, from where images of people can be uploaded and later processed for attendance. One image containing multiple faces can be processed at a time.
## Compatibility
The code is tested using Tensorflow r1.7.0 under Ubuntu 18.04.4 LTS with Python 2.7.17 and Python 3.6.9 and OpenCV 3.2.0
