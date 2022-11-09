from flask import Flask
import pyautogui
from flask_cors import cross_origin

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
@cross_origin()
def mover():
    pyautogui.moveRel(100,100,10)


if __name__=="__main__":
    app.run()