"""A ideia do código é criar um aplicativo simples para abrir a câmera e
mostrar a hora. Para isso usou a cv2 que é a biblioteca para abrir a câmera do computador
streamlit para a parte do GUI e abrir uma janela com o botão start e datetime para importar
a hora e data atual"""
import cv2
import streamlit as st
from datetime import datetime

st.title("Motion Detector")
start = st.button('Start Camera')

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get current time as a datetime object
        now = datetime.now()

        # Get day and time add them to the frame
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)
