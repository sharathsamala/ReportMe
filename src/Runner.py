
import label_image
import Utils
import pymongo


image_path = "/home/global/Desktop/30Hacks/IMG_4456.JPG"

classification_result = label_image.validate_image(image_path)

img_details = Utils.get_img_info(image_path)
print(img_details)
print(classification_result)


def create_mongo_json(img_details, calssification_results):

    #{'Latitude': 12.920883333333332, 'Longitude': 77.67735277777778, 'Altitude': 872.7133182844244, 'UTC-Time': '12:37:53', 'Date': '04/26/2019'}
    #{'face': 0.52732426, 'stagnant water': 0.26294482, 'pothole': 0.18175466, 'phone': 0.024173899, 'trash': 0.0038023798}

    mongo_json = {
        "latitude": "",
        "longitude" : "",
        "category" : "",
        "image": "",
        "image_created_date" : "",
        "last_mod_time": ""
    }





## 172.17.151.54
## mongodb+srv://whitewolf:<password>@whitewolf-h6rxj.gcp.mongodb.net/test?retryWrites=true
#
#
# client = pymongo.MongoClient("mongodb+srv://whitewolf:whitewolf@whitewolf-h6rxj.gcp.mongodb.net/mydb?retryWrites=true")
# db = client.mydb
#
# print(db.command("serverStatus"))
