import requests
KAKAO_BASE_URL="https://dapi.kakao.com"
from keys import KAKAO_REST_KEY
import pprint

if __name__ == "__main__":

    headers = {'Authorization':'KakaoAK '+KAKAO_REST_KEY }
    res = requests.get(
        url=KAKAO_BASE_URL+"/v3/search/book?target=title&query=미움받을 용기", headers=headers

    )
    if res.status_code == 200:
         book = res.json()

         # pprint.pprint(book['documents'])

         for book in book['documents']:
             print("{0:50s}-{1:20s}".format(book['title'], str(book['authors'])))


    else:
        print("Error {0}".res.status_code)



    # res2 = requests.get(
    #     url=KAKAO_BASE_URL + "/v2/search/image?query=류승룡",
    #     headers=headers
    #
    # )
    # if res2.status_code == 200:
    #     docs = res2.json()
    #     images=[]
    #     for image in docs['documents']:
    #         images.append(image['image_url'])
    #
    #     pprint.pprint(images)
    #
    #     # for img in img['documents']:
    #     #     print("{0:50s}-{1:20s}".format(img['title'], str(img['authors'])))
    # else:
    #     print("Error {0}" .format(res2.status_code))
    # # print(res.status_code)
    # # print(res.json())