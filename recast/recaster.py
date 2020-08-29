from PIL import Image
import os
	
def cast(imageName,fromFormat,toFormat,quality=100):
    if toFormat == fromFormat:
        raise
    uploaded_file_url = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media\\' + imageName)
    im = Image.open(uploaded_file_url)
    rgb_im = im.convert('RGB')
    newImage = uploaded_file_url.replace(fromFormat, toFormat)
    rgb_im.save(newImage, quality=quality)
