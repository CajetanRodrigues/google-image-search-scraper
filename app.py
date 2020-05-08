from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from flask import Flask, request 
import json
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ["GET"]) 
def getPage():
    return "Google Image Search"

# url = http://127.0.0.1:80/searchImages
@app.route('/searchImages', methods = ["POST"]) 
def searchImages():
    data=request.json
    searchQuery = data['searchQuery']
    html = urlopen('https://en.wikipedia.org/wiki/'+ searchQuery)
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    imageList = []
    for image in images: 
        # print(image['src']+'\n')
        imageList.append(image['src'])
    print(imageList)
    return json.dumps(imageList)
    
if __name__ == '__main__':  
    # app.run(host='0.0.0.0',port=443,debug = True,ssl_context=('cert.pem', 'key.pem'))
    # app.run(host='127.0.0.1',port=5000,debug = True,ssl_context='adhoc')
    app.run(host='0.0.0.0',port=80,debug = True)