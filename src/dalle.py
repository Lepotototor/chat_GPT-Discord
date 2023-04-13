import openai
import requests
from PIL import Image
import io


class DALLE:
    def __init__(self, key):
        # Définir clé API
        openai.api_key = key
        self._dalle_url = "https://api.openai.com/v1/images/generations"

    def générerImage(self, prompt):
        # Set up json
        params = {
            "model": "image-alpha-001",
            "prompt": prompt,
            "num_images": 1,
            "size": "512x512",
            "response_format": "url",
        }

        # Send request
        response = requests.post(self._dalle_url, headers={"Authorization": f"Bearer {openai.api_key}"}, json=params)
        response_json = response.json()

        # Retrieve the generated image URL from the API response
        image_url = response_json["data"][0]["url"]

        # Download the image from the URL
        image_data = requests.get(image_url).content

        # Open and display the image using the Python Imaging Library (PIL)
        image = Image.open(io.BytesIO(image_data))


        return image








#image.show()
#image.save("test.png")
