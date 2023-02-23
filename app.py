# ------------------------------------------------------#
# Import librairies
# ------------------------------------------------------#

import datetime
import urllib
import time
import cv2 as cv
import streamlit as st


from libraries.plugins import Motion_Detection
from libraries.utils import GUI, AppManager, DataManager

# ------------------------------------------------------#
# ------------------------------------------------------#
import base64


st.set_page_config(page_title="Detectify App", page_icon=":newspaper:", layout="wide")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("media\cover2.jpeg")
img1 = get_img_as_base64("media\menu1.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/jpg;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img1}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


def imageWebApp(guiParam):
    """ """
    # Load the image according to the selected option
    conf = DataManager(guiParam)
    image = conf.load_image_or_video()

    # GUI
    if st.button("* Start Processing *"):
        # Apply the selected plugin on the image
        bboxed_frame, output = AppManager(guiParam).process(image, True)

        # Display results
        st.image(bboxed_frame, channels="BGR", use_column_width=True)


def main():
    """ """
    # Get the parameter entered by the user from the GUI
    guiParam = GUI().getGuiParameters()

    # Check if the application if it is Empty
    if guiParam["appType"] == "Image Applications":
        if guiParam["selectedApp"] is not "Empty":
            imageWebApp(guiParam)

    else:
        raise st.ScriptRunner.StopException


# ------------------------------------------------------#
# ------------------------------------------------------#

if __name__ == "__main__":
    main()
