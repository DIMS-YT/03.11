from PyQt6.QtWidgets import QApplication, QWidget, QLabel


app = QApplication(...)

window = QWidget()

text = QLabel("Hello Cyber")

line = QVBoxLayout()
line.addWidget(text)
window.setLayout(line)

win.show()

app.exec()