import sys
import os

from flask import Flask, render_template, url_for,request, redirect, Response
import random, json

import pyautogui

from directkeys import sendKey, W, A, S, D

cur_pose = {}

app = Flask(__name__,template_folder='/')#static_folder='.', root_path='.')

# @app.route('/')
# def output():
# 	# serve index template
# 	return render_template('index.html')

# @app.route('/')
# def serve():
# 	# serve index template
# 	fs = " "
# 	for i in os.listdir():
# 		fs = fs +" "+ i
# 	# return fs
# 	return app.send_static_file('./index.html')

@app.route('/')
def home():
  return redirect(url_for('static', filename = 'index.html'))


# @app.route('/my_model/model.json')
# def model():
# 	return app.send_static_file('my_model/model.json')
# @app.route('/my_model/weights.bin')
# def weights():
# 	return app.send_static_file('my_model/weights.bin')

mouse_step = 10
speed = 0.5
topspeed = 10
mouse_ctrl = True
keybd_ctrl = False

@app.route('/static/pose', methods = ['POST'])
def worker():
	# read json + reply
	# print('hi')
	global cur_pose
	global speed

	cur_pose = request.get_json(force = True)
	# print(posedata)

	for i in range(4):
		direc,pred = cur_pose[i].split(':')
		# print(direc,pred,"ok")
		if float(pred) >= 0.70:
			print(direc)

			if mouse_ctrl:
				speed += speed
				if direc == 'up':
					pyautogui.move(0,-mouse_step-speed)
				if direc == 'down':
					pyautogui.move(0,mouse_step+speed)
				if direc == 'left':
					pyautogui.move(-mouse_step-speed,0)
				if direc == 'right':
					pyautogui.move(mouse_step+speed,0)
					
			if keybd_ctrl:
				# pyautogui.press(direc)
				if direc == 'up':
					sendKey(W)
				if direc == 'down':
					sendKey(S)
				if direc == 'left':
					sendKey(A)
				if direc == 'right':
					sendKey(D)
		else:
			speed = 0.1
	return "ok"


if __name__ == '__main__':
	# run!
	# os.system("chrome http://localhost:5000")
	# app.debug = True
	app.run(port = 5000)

