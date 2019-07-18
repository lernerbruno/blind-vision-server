from flask import Flask, request
import pandas as pd


app = Flask(__name__)

faces_position = [];
@app.route('/kinect')
def receive_kinect_info():
    data = request.args.get('data').lower()
    print(eval(data))
    return


@app.route('/get_kinect')
def get_kinect_data(name):
    return
