import pandas as pd
import numpy as np
import tensorflow as tf
import streamlit as st
from io import BytesIO
import PIL.Image as Image

st.title("X-Ray Image Classifier")
img_size=128
categories=["NORMAL","PNEUMONIA"]
model = tf.keras.models.load_model("my_model.keras")
if model:
    print("Model loaded")

def load_classifier():
    st.subheader("Upload on X-Ray image to detect if it is Normal or Pneumonia")
    file=st.file_uploader("",type=['jpeg','png'])
    if file!=None:
        img=Image.open(BytesIO(file.read())).convert('RGB')
        img=img.resize((img_size,img_size))
        new_array=tf.keras.preprocessing.image.img_to_array(img) 
        new_array=new_array.reshape(-1,img_size,img_size,3)
        st.image(file)
        st.write("")
        st.write("")

        if st.button("Predict"):
            preds=""
            predction=model.predict(new_array/255.0)
            print(predction)
            print(predction[0][0])
            confidence = predction[0][0] * 100
            preds = f"{categories[int(round(predction[0][0]))]} - {confidence:.2f}%"
            st.write(preds)

def main():
    load_classifier()

if __name__=='__main__':
    main()