import urllib.request
import os


def download_picture(url):

    image_name = "wallpaper.jpg"
    image_name = os.getcwd() + "/" + image_name
    
    return image_name


def set_wallpaper(image_path):
    
    command = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri {}'.format(image_path)
    os.system(command)


download_img = download_picture('https://source.unsplash.com/random/1920*1920')
set_wallpaper(download)
