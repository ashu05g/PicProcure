![image](https://github.com/user-attachments/assets/1b9a5144-551a-481e-99c0-47f5d6f81696)

# Pic Procure Share with Concealment
Obtain your pic with special care and effort!
PicProcure is a Django Project build for clustering of images based on registered users using Azure Storage Service

## Installation
Make sure you have Visual Studio Build Tool 2019 downloaded. Use the package manager pip to install remaining libraries
```bash
pip install -m requirements.txt
```
## Abstract:
I have lots of images and I want to share with the people who are there in the images. What should I do? Just simply upload it on the cloud and share the link to the images with all of them. But what if you are only interested in viewing/getting the images you are present in? Presenting to you **Pic Procure Share with Concealment**, the ultimate solution to all these problems. It processes and identifies image content, then clusters the images into separate folders based on each face identified using advanced Machine Learning and Azure Cloud Technologies.

## Introduction:
PicProcure reduces the user's workload by automatically sorting images based on the people in them. Using the best Clustering Algorithm in terms of speed and Azure Storage Services, it completes the process within minutes. Here's how it works:

1. Sign in to our system by providing your credentials, including a profile picture.
2. Create an event and allow some time (2 hours) for your contacts to register for the event.
3. Upload the images, wait for processing, and witness the magic!
   
Registered users will then be able to view their images on the site for at least 2 days. They can either download individual images or all images as a zip file.

## Tools and Technologies used:
- **Azure Storage Service** (for storing images)
- **Azure SQL Database** (backend storage)
- **Django Framework** (for web development)
- **Visual Studio Build Tool for 2019** (for C++ compiler)
- **DLib Library** (for clustering images)
- **Azure VM** (for deployment)
- **HTML, CSS, Bootstrap** (frontend)

## WorkFlow/Implementation:

### User Functionalities:
- Standard features like user sign-up and login have been implemented.
- If a user forgets their password, a reset code is sent to their registered email to allow password resetting.

### Event Functionalities:
- A user needs to create an event to share images.
- Other users can register for the event from the view-events page.
- The event creator must wait for up to 2 hours to allow everyone to register before uploading the images.

### Clustering Functionality:
The event creator uploads images that are stored in an Azure blob container using the **django-storage[azure]** library. Once this process completes, the core functionality of clustering begins.

We use the profile pictures of registered users along with the uploaded event images for clustering. We leverage pre-trained neural network models:
- **shape_predictor_5_face_landmarks**
- **dlib_face_recognition_resnet_model_v1**

These models identify and recognize faces using `dlib.get_frontal_face_detector()`, `dlib.shape_predictor()`, and `dlib.face_recognition_model_v1()`. After that, we compute a 128D vector for each face, which helps cluster the images using the **Chinese Whisper Algorithm**.

### Why use the Chinese Whisper Algorithm?
Chinese Whispers is a hard partitioning, randomized, time-linear flat clustering method. It performs well for large collections of images with numerous individuals. The randomization feature means running it multiple times on the same dataset may produce different results. It’s also the best-performing algorithm among image clustering methods.

At the end of the process, the system generates separate containers on the cloud. Since the registered users' profile pictures are taken during clustering, the system compares the images in each container with the registered profile pictures. Once a match is found, the container is renamed to that specific user. The system then links the container with the users.

### Final Steps:
Registered users can visit the site to view their images. They have the option to download either individual images or a zip file containing all images from the event. This ensures privacy and provides easy, efficient sharing of images.

## Screenshots for the Demo:

- **Sign-Up Page**

![image](https://github.com/user-attachments/assets/73bb428e-3b53-4cea-9636-4a3602bf6dd6)

- **My Profile Page**

![image](https://github.com/user-attachments/assets/0b92b6a9-2f89-48e7-ab85-4aaca1c2c9be)

- **Creating a New Event**

![image](https://github.com/user-attachments/assets/6b115c69-753a-4937-811c-855d95b24c49)

- **Viewing Events and Registered Users**

![image](https://github.com/user-attachments/assets/511049cd-8d9f-424d-afdc-a7233eb4002c)

- **Downloading Your Pictures in a Folder**

![image](https://github.com/user-attachments/assets/ccebd364-466b-4934-b9b3-c8dd43aa3a49)
