from flask import Flask, request, jsonify, make_response
import pandas as pd
# import flask

app = Flask(__name__)

faces_position = []
faces = []
final_dest = []


@app.route('/kinect')
def receive_kinect_info():
    # data = eval(request.args.get('faces'))
    # print(request.args.get('faces'))
    global faces
    global final_dest
    faces = eval(str(request.args.get('faces')))
    final_dest = eval(str(request.args.get('final_destination')))
    print(type(faces), faces)
    return "ok"


@app.route('/get_kinect')
def get_kinect_data():
    resp = make_response(jsonify(**{"faces": faces, "final_dest": final_dest}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0')
