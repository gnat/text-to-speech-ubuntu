#!/bin/python3
import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QSlider, QLabel, QWidget
from PyQt6.QtCore import Qt

class TextToSpeechApp(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Text to Speech")
		self.setGeometry(100, 100, 400, 400)

		# Central widget
		central_widget = QWidget()
		self.setCentralWidget(central_widget)

		# Layout
		layout = QVBoxLayout()
		central_widget.setLayout(layout)

		# Textbox
		self.textbox = QTextEdit(self)
		self.textbox.setPlaceholderText("Enter text to speak...")
		layout.addWidget(self.textbox)

		# Speed Slider Layout
		speed_layout = QHBoxLayout()
		self.speed_slider_label = QLabel("Speed: 280")
		self.speed_slider = QSlider(Qt.Orientation.Horizontal)
		self.speed_slider.setMinimum(80)
		self.speed_slider.setMaximum(450)
		self.speed_slider.setValue(280)
		self.speed_slider.valueChanged.connect(self.update_speed_label)
		speed_layout.addWidget(self.speed_slider_label)
		speed_layout.addWidget(self.speed_slider)
		layout.addLayout(speed_layout)

		# Pitch Slider Layout
		pitch_layout = QHBoxLayout()
		self.pitch_slider_label = QLabel("Pitch: 40")
		self.pitch_slider = QSlider(Qt.Orientation.Horizontal)
		self.pitch_slider.setMinimum(0)
		self.pitch_slider.setMaximum(99)
		self.pitch_slider.setValue(40)
		self.pitch_slider.valueChanged.connect(self.update_pitch_label)
		pitch_layout.addWidget(self.pitch_slider_label)
		pitch_layout.addWidget(self.pitch_slider)
		layout.addLayout(pitch_layout)

		# Button layout
		button_layout = QHBoxLayout()

		# Speak Button
		self.button_speak = QPushButton("💬 Speak", self)
		self.button_speak.clicked.connect(self.speak_text)
		self.button_speak.setFixedHeight(60)
		button_layout.addWidget(self.button_speak)

		# Stop Button
		self.button_stop = QPushButton("🛑 Stop", self)
		self.button_stop.clicked.connect(self.stop_speaking)
		self.button_stop.setFixedHeight(60)
		button_layout.addWidget(self.button_stop)
		layout.addLayout(button_layout)

	def update_speed_label(self):
		self.speed_slider_label.setText(f"Speed: {self.speed_slider.value()}")

	def update_pitch_label(self):
		self.pitch_slider_label.setText(f"Pitch: {self.pitch_slider.value()}")

	def speak_text(self):
		text = self.textbox.toPlainText()
		speed = self.speed_slider.value()
		pitch = self.pitch_slider.value()
		if text:
			self.stop_speaking()
			try:
				# Run espeak asynchronously
				subprocess.Popen(["espeak", f"-s{speed}", "-g0", f"-p{pitch}", "-v", "english-us", text])
			except FileNotFoundError:
				print("espeak command not found. Please make sure espeak is installed and in your PATH.")
			except Exception as e:
				print(f"An error occurred: {e}")

	def stop_speaking(self):
		try:
			subprocess.run("ps -ef | grep 'espeak' | tr -s ' ' | cut -d ' ' -f2 | xargs kill -9", shell=True, check=True)
		except Exception as e:
			print(f"An error occurred while stopping espeak: {e}")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_window = TextToSpeechApp()
	main_window.show()
	sys.exit(app.exec())
