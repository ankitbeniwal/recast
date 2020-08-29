from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import recaster, settings

def home(request):
    if request.method == 'POST' and request.FILES['imageFile']:
        image = request.FILES['imageFile']
        toFormat = request.POST['toFormat']
        quality = request.POST['quality']
        fs = FileSystemStorage()
        try:
            imageName = fs.save(image.name, image)
            fromFormat = imageName.split('.')[-1]
            recaster.cast(imageName,fromFormat,toFormat,quality)
            newImageURL = settings.MEDIA_URL + imageName.replace(fromFormat, toFormat)
            return render(request, 'home.html', {'newImage': newImageURL})
        except:
            return render(request, 'home.html', {'error': 'There was some error! Please try again.'})
        finally:
            fs.delete(imageName)

    return render(request, 'home.html')
