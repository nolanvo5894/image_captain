import streamlit as st
from PIL import Image
import ell
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Image Description App",
    page_icon="🖼️",
    layout="centered"
)

# Title
st.title("Image Description App")
st.write("Upload an image and get a description using GPT-4o-mini")

# Create the image description function
@ell.simple(model="gpt-4o-mini")
def describe_image(img: Image.Image):
    return [
        ell.system("You are a helpful assistant that describes images."),
        ell.user(["What's in this image?", img])
    ]

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Add a button to trigger the description
    if st.button("Get Description"):
        with st.spinner("Analyzing image..."):
            try:
                # Get the description
                description = describe_image(image)
                
                # Display the result
                st.success("Analysis complete!")
                st.write("### Description:")
                st.write(description)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}") 