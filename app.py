import streamlit as st
from PIL import Image
import requests

def footer():
	st.markdown("""
	* * *
	Built with ❤️ by [Rehan uddin](https://hardly-human.github.io/)
	""")
	st.success("Rehan uddin (Hardly-Human)👋😉")
	st.markdown("### [Give Feedback](https://www.iamrehan.me/forms/feedback_form/feedback_form.html)\
	 `            `[Report an Issue](https://www.iamrehan.me/forms/report_issue/report_issue.html)")


def main():
  
	st.title("Image Captioning App")
	st.text("Built with Neural_Talk_2 API and Streamlit")
	st.markdown("### [NeuralTalk 2 by Andrej Karpathy](https://github.com/karpathy/neuraltalk)\
     `            `[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Hardly-Human/Image-Captioning-App)\
	`            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/)")

	image_file = st.file_uploader("Upload Image", type = ['jpg','png','jpeg'])

	if image_file is None:
		st.warning("Upload Image and Generate Captions")

	if image_file is not None:
		image1 = Image.open(image_file)
		rgb_im = image1.convert('RGB') 
		image = rgb_im.save("saved_image.jpg")
		image_path = "saved_image.jpg"
		st.image(image1, width = 700)

	if st.button("Generate Caption"):
		if image_file is not None:
			r = requests.post(
			    "https://api.deepai.org/api/neuraltalk",
			    files={
			        'image': open('saved_image.jpg', 'rb'),
			    },
			    headers={'api-key': 'aa48ee59-f392-4783-b1ac-ab410534ca61'}
			)
			output = r.json()["output"].title()
			st.warning('Output : "{}"'.format(output))
		else:
			st.error("Please Upload Image!!!")

if __name__== "__main__":
	main()
	footer()