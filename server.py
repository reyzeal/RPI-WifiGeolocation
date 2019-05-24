#!/usr/bin/python3
from flask import Flask, request, render_template, json
from Library import Wifi

app = Flask(__name__,template_folder='Assets/templates',static_folder='Assets/static')

# @app.route('/', methods=['GET'])
# def index():
#     return "hello world"

@app.route('/api/ap', methods=['GET'])
def listAP():
    mapList = Wifi.retrieve()
    dataList = []
    for i in mapList:
        dataList.append({'ssid':i.ssid,'address':i.address,'signal':i.signal})
    return json.jsonify(dataList)

@app.route('/',methods=['GET'])
@app.route('/<module>',methods=['GET'])
def index(module=None):
    return render_template('Layout/app.html')

@app.route('/app/<module>',methods=['GET'])
def appModule(module='home'):
    if module   ==  'home':
        return render_template('home.html')
    elif module ==  'detected':
        return render_template('detected.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2019,debug=True)
