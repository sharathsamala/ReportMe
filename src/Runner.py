
import label_image
import Utils
import pymongo
import operator
import datetime
import tkinter as tk
from tkinter import filedialog
import traceback

image_path = "/home/global/Desktop/30Hacks/IMG_4456.JPG"
comment = "verry_bad_road"
client = pymongo.MongoClient('localhost', 27017)

root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename()


classification_result = label_image.validate_image(image_path)

img_details = Utils.get_img_info(image_path)
message_string = "**************************************************\n" \
                 "Image Classification      : {}\n" \
                 "Image Accuracy            : {}\n" \
                 "Image Location details    : {}\n" \
                 "Image Validation          : {}\n" \
                 "Message                   : {}\n" \
                 "Ticket ID                 : {}\n" \
                 "**************************************************\n"


def create_mongo_json(img_details, calssification_results, comment, img_path):

    #{'Latitude': 12.920883333333332, 'Longitude': 77.67735277777778, 'Altitude': 872.7133182844244, 'UTC-Time': '12:37:53', 'Date': '04/26/2019'}
    #{'face': 0.52732426, 'stagnant water': 0.26294482, 'pothole': 0.18175466, 'phone': 0.024173899, 'trash': 0.0038023798}

    result = True
    validation = "Failed"
    mongo_json = {
        "latitude": "",
        "longitude": "",
        "category" : "",
        "image": "",
        "image_created_date": "",
        "last_mod_time": "",
        "ticket_id": "",
        "comment": "NA"
    }


    category = max(calssification_results.items(), key=operator.itemgetter(1))[0]

    if calssification_results[category] > 0.4:
        validation = "Passed"

    if str(img_details) == "{}":
        validation = "Failed"
        return False, (message_string.format(category, calssification_results[category],
                                      "No location detected, Please take the picture with GPS enabled",validation,
                                      "Failed to create a Ticket for the given problem", "NA" ))

    if validation == "Failed":
        return False, (message_string.format(category, calssification_results[category],
                                      (str(img_details["Latitude"])+", "+str(img_details["Longitude"])),validation,
                                      "Failed to identify the probable problem category , Please upload the right Image", "NA" ))


    img_date = datetime.datetime.strptime(str(img_details["Date"])+"T"+str(img_details["UTC-Time"]), "%m/%d/%YT%H:%M:%S")
    d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")

    mongo_json["latitude"] = str(img_details["Latitude"])
    mongo_json["longitude"] = str(img_details["Longitude"])
    mongo_json["category"] = category
    mongo_json["image"] = img_path
    mongo_json["image_created_date"] = img_date
    mongo_json["last_mod_time"] = datetime.datetime.now()
    mongo_json["ticket_id"] = "NA"
    mongo_json["comment"] = comment
    mongo_json["accuracy"] = str(calssification_results[category])

    return result, mongo_json


def insert_mongo(mongo_json, mongo_conn):

    collection = mongo_conn.mydb.wolf

    try:
        next_val = collection.find_one(sort=[("ticketid", -1)])["ticketid"] + 1

    except:
        print(next_val)
        print(traceback.format_exc())

    mongo_json["ticketid"] = next_val
    collection.insert_one(mongo_json)
    return next_val


result, data = create_mongo_json(img_details, classification_result, comment, image_path)

if result:
    print(data)

    tick_id = insert_mongo(data, client)

    print(message_string.format(data["category"], data["accuracy"], str(data["latitude"])
                                +", "+str(data["longitude"]), "Passed", "Registerd the problem successfully", str(tick_id)))

else:
    print(data)
    raise Exception



