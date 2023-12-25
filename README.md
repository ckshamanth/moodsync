@ -1,57 +0,0 @@
# Emotion-Music-Recommendation
A project recommending music based on facial expressions using the FER 2013 dataset and the Spotify API.

![moodsync ss](https://github.com/ckshamanth/moodsync/assets/122350335/b4056eeb-9c91-47d9-be2d-b36a36933d72)


# Project Overview:
Trained on the FER 2013 dataset, the emotion recognition model detects seven emotions. The application captures live video from the webcam, predicts emotions using the model, and fetches corresponding song playlists from Spotify via the spotipy wrapper, displaying recommendations on the screen.

# Key Features:
- Real-time expression detection and song recommendations.
- Integration with Spotify API for playlist retrieval.
- Neumorphism UI design for the website.

# How to Run:
Flask:
- Install dependencies using `pip install -r requirements.txt`.
- In Spotipy.py, enter Spotify Developer account credentials in 'auth_manager' if updating playlists.
- Run `python app.py` and grant camera permission if prompted.

# Technology Stack:
- Keras
- Tensorflow
- Spotipy
- Tkinter (for testing)
- Flask

# Dataset:
Utilizing the well-known FER2013 dataset, our model classifies seven emotions. Find the dataset [here](https://www.kaggle.com/msambare/fer2013).

Note: The dataset is imbalanced, with the 'happy' class being overrepresented, potentially impacting accuracy.

# Model Architecture:
- Sequential model with Conv2D, Maxpool2D, Dropout, and Dense layers:
  1. Conv2D layers with filter sizes from 32 to 128, all with 'relu' activation.
  2. Pooling layers with a pool size of (2,2).
  3. Dropout set to 0.25.
  4. Final Dense layer with 'softmax' activation for classifying seven emotions.
- Used 'categorical_crossentropy' loss, 'Adam' optimizer, and 'accuracy' metric.

Note: Experimented with other models like VGG16, but this architecture provided satisfactory accuracy.

# Image Processing and Training:
- Images were normalized, resized to (48,48), and converted to grayscale in batches of 64 using Keras' 'ImageDataGenerator'.
- Training took approximately 13 hours locally for 75 epochs, achieving around 66% accuracy.

# Current Status:
The project functions smoothly, delivering good frame rates for live detection due to multithreading.

# Components:
- Spotipy: Module for connecting to and retrieving tracks from Spotify.
- haarcascade: Face detection.
- camera.py: Video streaming, frame capture, prediction, and recommendation module passed to main.py.
- main.py: Main Flask application file.
- index.html: Web page for the application (basic HTML and CSS).
- utils.py: Utility module for webcam video streaming with threads for real-time detection.
- train.py: Script for image processing and model training.