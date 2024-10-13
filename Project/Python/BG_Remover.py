import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np
import io
import base64

st.title('Background Remover')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Processing...")

    input_img = np.array(image)
    output_img = remove(input_img)

    st.write("Done!")
    st.image(output_img, caption='Your image with background removed.', use_column_width=True)

    # Convert the output image to bytes
    img_pil = Image.fromarray(output_img)
    byte_io = io.BytesIO()
    img_pil.save(byte_io, 'PNG')
    byte_io.seek(0)

    # Create a download link for the output image
    b64 = base64.b64encode(byte_io.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="image_no_bg.png">Download image</a>'
    st.markdown(href, unsafe_allow_html=True)
