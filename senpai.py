import os
import sys
import requests
import numpy as np
import jsonpickle
import jsonpickle.ext.numpy as jsonpickle_numpy
import json

jsonpickle_numpy.register_handlers()
path = os.path.abspath(os.path.dirname(sys.argv[0]))
tmp_image = path+"/tmp.jpg"
data_dir = path+"/MyFriends/"
fs_server = "https://face-senpai.herokuapp.com/"


def take_picture():
    import androidhelper
    droid = androidhelper.Android()
    rest = droid.cameraInteractiveCapturePicture(tmp_image)
    return rest.error is None


def make_request():
    files = {'file': (tmp_image, open(tmp_image, 'rb')), }
    try:
        response = requests.post(fs_server, files=files)
        face = jsonpickle.decode(json.loads(
            response.content.decode("utf-8"))["msg"])
        return face
    except BaseException:
        return False


def train():
    if take_picture():
        r = make_request()
        if not r:
            print("failed in make_request!")
        else:
            nama = input("please give a name: ")
            nama = nama.replace(" ", "_")
            with open(data_dir+nama, "w") as f:
                f.write(r)
            print("success!")
    else:
        print("failed at take picture!")


def hello(you, me):
    you = jsonpickle.decode(json.loads(you))
    me = you = jsonpickle.decode(json.loads(me))
    distance = np.linalg.norm([you] - me, axis=1)
    compare = list(distance <= 0.6)
    if compare[0]:
        return True
    else:
        return False


def recognize():
    ls = os.listdir(data_dir)
    if take_picture():
        r = make_request()
        if not r:
            print("failed in make_request!")
        else:
            found = False
            for data in ls:
                with open(data_dir+data, "r") as coba:
                    coba = coba.read()
                if hello(r, coba):
                    print("hello %s!" % data.replace("_", " "))
                    found = True
                    break
                else:
                    pass
            if not found:
                print("no data is matches!")
    else:
        print("failed at take picture!")


def list_database():
    print("\n".join(os.listdir(data_dir)))
