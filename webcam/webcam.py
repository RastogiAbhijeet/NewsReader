import sys, os
sys.path.append("../")

import cv2
import numpy as np

# from summerProject.webcam import face_detection_utilities as fdu
import face_detection_utilities as fdu
os.environ["THEANO_FLAGS"] = "mode=FAST_RUN,device=gpu,floatX=float32"
import model.myVGG as vgg
# import summerProject.model.myVGG as vgg
import time
import keras 
import theano

class Webcam:
	def __init__(self,duration = 10):
		self.windowsName = 'Preview Screen'
		self.FACE_SHAPE = (48, 48)
		self.model = vgg.VGG_16('my_model_weights_83.h5')
		self.emotion = ['Angry', 'Fear', 'Happy','Sad', 'Surprise', 'Neutral']
		self.showCam = 1
		self.averageEmotion = 5
		self.captureDuration = duration


	def refreshFrame(self, frame, faceCoordinates):
		if faceCoordinates is not None:
			fdu.drawFace(frame, faceCoordinates)
		cv2.imshow(self.windowsName, frame)

	def showScreenAndDectect(self, capture):
		flag, frame = capture.read()
		faceCoordinates = fdu.getFaceCoordinates(frame)
		self.refreshFrame(frame, faceCoordinates)
		if faceCoordinates is not None:
			face_img = fdu.preprocess(frame, faceCoordinates, face_shape=self.FACE_SHAPE)
			input_img = np.expand_dims(face_img, axis=0)
			input_img = np.expand_dims(input_img, axis=0)
			result = self.model.predict(input_img)[0]
			index = np.argmax(result)
			print(index)
			return index

	def getCameraStreaming(self):
		capture = cv2.VideoCapture(0)
		if not capture:
			print("Failed to capture video streaming ")
			sys.exit(1)
		else:
			print("Successed to capture video streaming")
		return capture


	def cleanList(self, emotionList, unwantedElement):
		try:
			emotionList = [x for x in emotionList if x != unwantedElement]
		except ValueError:
			pass
		return emotionList

	def averageListElements(self,inputList):
		try:
			inputList =  int(sum(inputList)/len(inputList))
		except ZeroDivisionError :
			pass
		return inputList

	def startModel(self):
		capture = self.getCameraStreaming()
		if self.showCam:
			cv2.startWindowThread()
			cv2.namedWindow(self.windowsName, cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty(self.windowsName, cv2.WND_PROP_FULLSCREEN, cv2.WND_PROP_FULLSCREEN)
		emotionList = []
		t_end = time.time() + self.captureDuration

		print("Detecting expression..")
		while time.time() < t_end:
			emotionList.append(self.showScreenAndDectect(capture))
			emotionList = self.cleanList(emotionList, None)
			avgEmotion = self.averageEmotion = self.averageListElements(emotionList)
			self.averageEmotion = 5
		return (self.emotion[avgEmotion], avgEmotion)

obj = Webcam()
t0 = time.time()
print(obj.startModel())
t1 = time.time()
#
# print(t1-t0)
