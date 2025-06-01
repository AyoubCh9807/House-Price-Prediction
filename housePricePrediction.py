from PySide6.QtWidgets import (QApplication, QWidget, QPushButton,
							   QMessageBox, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit)
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import sys

spaceInputs = []
bedroomInputs = []
ageInputs = []
priceInputs = []
new_house = []
predictionInputs = []

def predictHouse():

	spaces = [int(spaceInput.text()) for spaceInput in spaceInputs]
	bedrooms = [int(bedroomInput.text()) for bedroomInput in bedroomInputs]
	ages = [int(ageInput.text()) for ageInput in ageInputs]
	prices = [int(priceInput.text()) for priceInput in priceInputs]
	new_house = [[int(pInput.text()) for pInput in predictionInputs]]
	new_house = np.array(new_house)
	

	data = [[space, bedroom, age] for space, bedroom, age in zip(spaces, bedrooms, ages)]
	data = np.array(data)

	for space, bedroom, age, price in zip(spaces, bedrooms, ages, prices):
		try:
			if space < 0 or bedroom < 0 or age < 0 or price < 0:
				QMessageBox.information(None, "Blindness error", "Only positive integers are valid")
				return 
		except ValueError:
			QMessageBox.information(None, "Dumbness error", "Only numbers are valid bru")
			return
	try:
		if any(int(val) < 0 for val in new_house[0]):
			QMessageBox.information(None, "Input Error", "Only positive integers are valid for the new house prediction")
			return
	except ValueError:
		QMessageBox.information(None, "Input Error", "Prediction inputs must be numbers")
		return


	model = LinearRegression()
	model.fit(data, prices)
	
	new_house_prediction = model.predict(new_house)
	
	plt.plot(data[:, 0], prices, marker='o', label='Actual House Prices', color='blue')
	plt.plot(data[:, 0], model.predict(data), marker='o', label='Regression Line', color='red')
	plt.scatter(new_house[:, 0], new_house_prediction[0], marker='*', color='green', label='Predicted House')
	plt.xlabel("House Details")
	plt.ylabel("House Prices")
	plt.grid(True)
	plt.legend()
	plt.show()


def createInputLayout():
	
	layout = QVBoxLayout()
	container = QVBoxLayout()
	layout1 = QHBoxLayout()
	layout2 = QHBoxLayout()
	layout3 = QHBoxLayout()
	layout4 = QHBoxLayout()
	
	for i in range(5):
		
		keyLabel1 = QLabel(f"Enter House n°{i+1}'s space (sqft) : ")
		keyInput1 = QLineEdit()
		keyLabel2 = QLabel(f"Enter House n°{i+1}'s bedrooms : ")
		keyInput2 = QLineEdit()
		keyLabel3 = QLabel(f"Enter House n°{i+1}'s age (y) : ")
		keyInput3 = QLineEdit()
		keyLabel4 = QLabel(f"Enter House n°{i+1}'s price (per $K) : ")
		keyInput4 = QLineEdit()
		
		layout1.addWidget(keyLabel1)
		layout1.addWidget(keyInput1)
		
		layout2.addWidget(keyLabel2)
		layout2.addWidget(keyInput2)
		
		layout3.addWidget(keyLabel3)
		layout3.addWidget(keyInput3)
		
		layout4.addWidget(keyLabel4)
		layout4.addWidget(keyInput4)
		
		container.addLayout(layout1)
		container.addLayout(layout2)
		container.addLayout(layout3)
		container.addLayout(layout4)
		
		layout.addLayout(container)
		
		spaceInputs.append(keyInput1)
		bedroomInputs.append(keyInput2)
		ageInputs.append(keyInput3)
		priceInputs.append(keyInput4)
		
	return layout

def createPredictionLayout():
	layout = QHBoxLayout()
	layout1 = QHBoxLayout()
	layout2 = QHBoxLayout()
	layout3 = QHBoxLayout()
	
	keyLabel1 = QLabel(f"Enter the prediction's space (sqft) : ")
	keyInput1 = QLineEdit()
	keyLabel2 = QLabel(f"Enter the predictions's bedrooms : ")
	keyInput2 = QLineEdit()
	keyLabel3 = QLabel(f"Enter the prediction's age (y) : ")
	keyInput3 = QLineEdit()
	
	layout1.addWidget(keyLabel1)
	layout1.addWidget(keyInput1)
	
	layout2.addWidget(keyLabel2)
	layout2.addWidget(keyInput2)
	
	layout3.addWidget(keyLabel3)
	layout3.addWidget(keyInput3)
	
	layout.addLayout(layout1)
	layout.addLayout(layout2)
	layout.addLayout(layout3)
	
	predictionInputs.append(keyInput1)
	predictionInputs.append(keyInput2)
	predictionInputs.append(keyInput3)
	
	return layout


def main():
	app = QApplication(sys.argv)
	window = QWidget()

	layout = QVBoxLayout()
	
	inputLayout = createInputLayout()
	predictionLayout = createPredictionLayout()
	submitButton = QPushButton("Predict House Price")
	submitButton.clicked.connect(predictHouse)

	layout.addLayout(inputLayout)
	layout.addLayout(predictionLayout)
	layout.addWidget(submitButton)
	
	window.setLayout(layout)
	
	window.setWindowTitle("House Price Prediction App")
	window.resize(200, 400)
	window.show()
	sys.exit(app.exec())
	
if __name__ == '__main__':
	main()

