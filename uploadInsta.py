from instagrapi import Client
from instagrapi.types import Usertag, Location
import config


def uploadOnInsta(date):
    cl = Client()
    cl.login(config.username, config.password)

    media = cl.photo_upload(
        path="Temp/menu.jpg",
        caption=f"Menu du {date}",
        location=Location(name="Amiens, France", lat =49.875816, lng=2.296731)
    )