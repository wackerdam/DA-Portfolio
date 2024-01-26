import requests
from PIL import Image
from io import BytesIO

def show_image_from_url(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.show()
    else:
        print(f"Failed to fetch image from {url}. Status code: {response.status_code}")
imageurl = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
show_image_from_url(imageurl)