
import label_image
import Utils
import pymongo


image_path = "/home/global/Desktop/30Hacks/IMG_4456.JPG"

#classification_result = label_image.validate_image(image_path)

img_details = Utils.get_img_info(image_path)
print(img_details)


## 172.17.151.54
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["wolf"]

# mydict = { "name": "John", "address": "Highway 37" }
#
# x = mycol.insert_one(mydict)

x = mycol.find_one()
print(x)

