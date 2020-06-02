from django.shortcuts import render
from .neural_style import get_image
import urllib
from instabot import Bot

def index(request):
    return render(request,'index.html')
def result(request):
    url=get_image('https://miro.medium.com/max/756/1*6jTexd8pJUHp0NdVxc6dkA.png','https://www.edvardmunch.org/images/paintings/the-scream.jpg')['output_url']
    urllib.request.urlretrieve(url, "0.jpg")
    bot = Bot()
    bot.login(username = request.POST["username"],password=request.POST["pw"],is_threaded=True) 
    bot.upload_photo(r"C:\Users\user\ig_nst\0.jpg")
    return render(request,'result.html')

