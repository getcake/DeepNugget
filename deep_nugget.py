#!/usr/local/bin/python3.7
from twilio.twiml.messaging_rsponse import Message, Messagingrsponse
from flask import Flask, request, redirect, send_from_directory
from imageai.Detection import ObjectDetection
import pyperclip
import requests
import os

cdir = os.getcwd()
app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def main():
    rsp = Messagingrsponse()

    dt = ObjectDetection()
    dt.setModelTypeAsYOLOv3() # use yolo
    dt.setModelPath(os.path.join(
        cdir, "yolo.h5"))
    dt.loadModel()
    if request.values['NumMedia'] != '0':
        fn = request.values['MessageSid'] + '.jpg'
        rsp_str = ''
        with open(fn, 'wb') as f:
            image_url = request.values['MediaUrl0']
            f.write(requests.get(image_url).content)
            dts = dt.detectObjectsFromImage(input_image=fn, output_image_path= fn)
            for obj in dts:
                perc = obj["percentage_probability"]
                rsp_str += (str(obj["name"] + " : ") + str(perc) + "%\n")
                print(obj["name"], " : ", obj["percentage_probability"])

        msg = rsp.message(rsp_str)
        msg.media('http://USE_YOUR_OWN_NGROK_URL/output/{}'.format(fn))
        os.system('deeppyer ' + fn)
        os.system('imgur-uploader ' + 'deepfried.jpg')
        pasted = pyperclip.paste()
        pasted = str(pasted)
        #rsp.message(rsp_str)
        if "donut" in rsp_str:
            rsp.message("Not a chicken nugget, but I'll fry it anyways!")
            rsp.message(str(pasted))
        else:
            print('else')

    else:
        rsp.message("You gotta send a picture.")
    return str(rsp)

@app.route('/output/<fn>', methods=['GET', 'POST'])
def uploaded_file(fn):
    return send_from_directory(cdir, fn)
