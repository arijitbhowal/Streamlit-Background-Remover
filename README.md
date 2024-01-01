# A Streamlit Web App to Remove Background with Segment Anything Model

It is a simple web application built with Streamlit and OpenCV that allows users to upload an image, specify a point on the person's body, and remove the background.

## Table of Contents
- [Background](#background)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Demo](#demo)


## Background

This project utilizes the Streamlit framework to create an interactive user interface and OpenCV for advanced image processing. The key feature of this application is the removal of image backgrounds, made possible by deploying the background removal function on [ModelBit](https://modelbit.com/), an external API for machine learning model deployment.

### Background Removal Functionality

The core functionality of removing the background is deployed on ModelBit, and this project leverages the API provided by ModelBit to seamlessly remove backgrounds from uploaded images. The integration with ModelBit allows for efficient and effective background removal, providing users with a powerful tool for enhancing their images.

By using the ModelBit API, the background removal process becomes a streamlined and automated task, enhancing the overall user experience of this application.

## Features

- Upload an image.
- Specify a point on the person's body.
- Remove the background to generate a new image.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/arijitbhowal/remove-background.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**

    ```bash
    streamlit run main.py
    ```

4. **Open your web browser and navigate to [http://localhost:8501](http://localhost:8501).**

## Usage

1. Upload an image using the file uploader.
2. Click on a point on the person's body.
3. Click the "Remove Background" button to generate the new image.

## Demo
### Web App Interface
![Screenshot of the Web App Interface](https://github.com/arijitbhowal/Streamlit-Background-Remover/assets/88677587/599950ce-1ca1-47b6-8a9c-8096239325d6)

### Upload Image
![Screenshot of Image Upload](https://github.com/arijitbhowal/Streamlit-Background-Remover/assets/88677587/0b8a66d1-17cd-4694-b01f-40b8016f7ae5)

1. **Remove Background Button:**
   - The "Remove Background" button is initially disabled.

2. **Enable the Button:**
   - Click on any point on the person's body to provide x and y coordinates.
   - The button becomes enabled.

![Screenshot of Remove Background Button Enabled](https://github.com/arijitbhowal/Streamlit-Background-Remover/assets/88677587/f0193e4d-0ac7-48d1-a109-c54b2b4d654a)

### Remove Background
![Screenshot of Background Removal](https://github.com/arijitbhowal/Streamlit-Background-Remover/assets/88677587/9f8d77ab-afeb-48a8-adb5-422b8e485422)

### Toggle between the original image and the new image
![Toggle to original image](https://github.com/arijitbhowal/Streamlit-Background-Remover/assets/88677587/878415f8-3d24-44cd-8f6a-01df6e108ac2)



