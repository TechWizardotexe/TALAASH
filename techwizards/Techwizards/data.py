from pymongo import MongoClient
import base64

client = MongoClient("mongodb://localhost:27017/")

db = client["aadharDB"]
aadharDB = db["fingerDB"]

with open("C:\\Users\\milin\\Desktop\\techhacks\\Hackathon\\techwizards\\Techwizards\\static\\471407501308.bmp", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())

yo = {
    "img" : converted_string,
    "name" : "MILIND SRIVASTAVA",
    "aadhar" : "471407501308",
    # "FIR_Date" : "06-01-2023",
    "Gender" : "Male",
    "contact" : "8052069832",
    "DOB" : "28-09-2003",
    # "FIR_no" : 100,
    "Address" : "Rajendra Nagar,Gorakhnath,Gorakhpur",
    "is_encoded" : "False"
}

aadharDB.insert_one(yo)
