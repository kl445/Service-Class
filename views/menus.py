import pprint

import requests
from flask import Blueprint, render_template
from requests import Response

from keys import KAKAO_REST_KEY
from rest_client.read_KAKAO import KAKAO_BASE_URL

menus_blueprint = Blueprint('menus', __name__)
headers = {'Authorization': 'KakaoAK ' + KAKAO_REST_KEY}

@menus_blueprint.route("/main")
def menus_main():
    return "welcome news main"


@menus_blueprint.route("/sports")
def menus_sport():
    return "welcome sports news"


@menus_blueprint.route("/images")
def images():

    res2: Response = requests.get(
        url=KAKAO_BASE_URL + "/v2/search/image?query=냥냥이",
        headers=headers
    )

    if res2.status_code == 200:
        docs = res2.json()
        images = []

        for image in docs['documents']:
            images.append(image['image_url'])

        print(images)
    else:
        print("Error {0}".format(res2.status_code))

    return render_template(
        'images.html',
        images=images,
        nav_menu="image"
    )


@menus_blueprint.route("/books")
def books():

    res = requests.get(
        url=KAKAO_BASE_URL + "/v3/search/book?target=title&query=미움받을 용기",
        headers=headers
    )

    if res.status_code == 200:
        books = res.json()

        # pprint.pprint(book['documents'])

        for book in books['documents']:
            print("{0:50s}-{1:20s}".format(book['title'], str(book['authors'])))


    else:
        print("Error {0}".res.status_code)

    return render_template(
        'books.html',
        books=books['documents'],
        nav_menu="book"
    )
