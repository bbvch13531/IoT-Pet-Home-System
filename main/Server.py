#-*-coding: utf-8-*-
from flask import Flask,request,jsonify,send_from_directory
from ServerManager import MessageClass

## json 타입들 초기화

mMessage = MessageClass()

UPLOAD_FOLDER = 'uploaded'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
## Flask 키는 소스

@app.route("/keyboard",methods =["GET"])
def keyboard():
    return jsonify(mMessage.getBaseKeyboard()),200

## 키보드 정보 가져옴

@app.route("/message",methods=["POST"])
def message():
    data = request.get_json()   ## 요청메세지로부터 json 데이터를 가져옴
                                ## 게다가 딕셔너리 형태로 반환해줌
    user_key = data['user_key']
    message = data['content']
    return jsonify(mMessage.postTextMessage(user_key,message)),200
## 메세지를 보냈을 때 처리

@app.route("/friend",methods=["POST"])
def friendAdd():
    return "HTTP/1.1 200 OK"
## 친구 추가했을 때

@app.route("/friend/<user_key>", methods=["DELETE"])
def friendDelete(user_key):
    return "HTTP/1.1 200 OK"
## 친구 삭제했을 때

@app.route("/chat_room/<user_key>",methods=["DELETE"])
def chat_roomOut():
    return "HTTP/1.1 200 OK"
## 채팅방에서 나갔을 때

@app.route("/pi_regist", methods=["POST"])
def settingPi():
    data = request.get_json()
    PiKey = data["PiKey"]
    userList = data["userList"]
    url = data["url"]

    return jsonify(mMessage.updatePiData(PiKey, userList, url)), 200

@app.route('/download/<filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)

if __name__ == "__main__":
    ssl_cert = '/etc/letsencrypt/live/pethome.ga/fullchain.pem'
    ssl_key =  '/etc/letsencrypt/live/pethome.ga/privkey.pem'
    contextSSL =  (ssl_cert, ssl_key)
    app.run(host='0.0.0.0', port=8080, debug = True, ssl_context = contextSSL)
    
