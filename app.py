import streamlit as st
from PIL import Image


def main():
  
	st.title("Image Captioning App")
	st.text("Built with Neural_Talk_2 API and Streamlit")
	st.markdown("### [NeuralTalk 2 by Andrej Karpathy](https://github.com/karpathy/neuraltalk)\
     `            `[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Hardly-Human/toonify-images)\
	`            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/)")

	image_file = st.file_uploader("Upload Image", type = ['jpg','png','jpeg'])

	if image_file is None:
		st.warning("Upload Image and Generate Captions")

	if image_file is not None:
		image1 = Image.open(image_file)
		rgb_im = image1.convert('RGB') 
		image = rgb_im.save("saved_image.jpg")
		image_path = "saved_image.jpg"
		st.image(image1)


if __name__== "__main__":
	main()