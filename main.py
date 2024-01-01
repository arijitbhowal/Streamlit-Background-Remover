import requests
import base64
import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates as im_coordinates
import cv2
import numpy as np
import os

api_endpoint = 'https://arijitbhowal.ap-south-1.modelbit.com/v1/remove_background/latest'

# set layout
st.set_page_config(page_title="Remove Background", page_icon="📝", layout="wide", initial_sidebar_state='expanded')

col1, col2 = st.columns([1, 2])

# Display header and background image in col1
col1.title("Background Remover")
bg_image_path = "./bg-img.png"  # Replace with the path to your background image
col1.image(bg_image_path, use_column_width=True)

# file uploader
file = col2.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

# read image
if file is not None:
    image = Image.open(file).convert('RGB')

    image = image.resize((660, int(660 * image.height / image.width)))  # Make image smaller
    colm1, colm2 = col2.columns(2)

    placeholder0 = col2.empty()
    with placeholder0:
        value = im_coordinates(image)
        if value is not None:
            print(value)

    if colm1.button("Original Image", use_container_width=True):
        placeholder0.empty()
        placeholder1 = col2.empty()
        with placeholder1:
            col2.image(image, use_column_width=True)

    # Disable the "Remove Background" button until x and y coordinates are available
    remove_bg_button_disabled = value is None or 'x' not in value or 'y' not in value

    if colm2.button("Remove Background", type='primary', use_container_width=True, disabled=remove_bg_button_disabled):
        placeholder0.empty()
        placeholder2 = col2.empty()

        filename = '{}_{}_{}.png'.format(file.name, value['x'], value['y'])

        if os.path.exists(filename):
            result_image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        else:
            _, image_bytes = cv2.imencode('.png', np.asarray(image))

            image_bytes = image_bytes.tobytes()

            image_bytes_encoded_base64 = base64.b64encode(image_bytes).decode('utf-8')

            api_data = {'data': [image_bytes_encoded_base64, value['x'], value['y']]}
            response = requests.post(api_endpoint, json=api_data)

            result_image = response.json()['data']

            result_image_bytes = base64.b64decode(result_image)

            result_image = cv2.imdecode(np.frombuffer(result_image_bytes, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

            cv2.imwrite(filename, result_image)

        with placeholder2:
            col2.image(result_image, use_column_width=True)

# Display steps to use the website
st.sidebar.markdown("### Steps to Use:")
st.sidebar.markdown("1. **Upload Image:** Choose an image with one person in it.")
st.sidebar.markdown("2. **Click on a Point:** Click on a point on the body of the person in the image.")
st.sidebar.markdown("3. **Remove Background:** Click on the 'Remove Background' button to generate the new image.")
st.sidebar.markdown("Note: Ensure there is only one person in the frame.")
