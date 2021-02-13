from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout
from random import randint

def show_winner():
    question.setText("ЭТО ОН!!!")
    button.setText("УРА!")
    a = randint(1,1000)
    a = str(a)
    winner.setText(a)


app = QApplication([])
window = QWidget()

window.resize(400,250)

question = QLabel("Кто победитель?")
winner = QLabel("???")
button = QPushButton("Жми!!!")

general_line = QVBoxLayout()

general_line.addWidget(question, alignment = Qt.AlignCenter)
general_line.addWidget(winner, alignment = Qt.AlignCenter)
general_line.addWidget(button, alignment = Qt.AlignCenter)

window.setLayout(general_line)

button.clicked.connect(show_winner)

window.show()
app.exec_()