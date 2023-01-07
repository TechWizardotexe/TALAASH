import base64
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

img_db = client["aadharDB"]
user_img = img_db["img"]



data = user_img.find({"name": "milind"})
for user in data:
    decodeit = open('x/hello_level.jpeg', 'wb')
    decodeit.write(base64.b64decode(user["img"]))
    decodeit.close()
with open("C:\\Users\\milin\\Desktop\\techhacks\\Hackathon\\techwizards\\Techwizards\\471407501308.jpg", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())
print(converted_string)
yo = {
    "img": converted_string,
    "name": "Milind"
}
user_img.insert_one(yo)