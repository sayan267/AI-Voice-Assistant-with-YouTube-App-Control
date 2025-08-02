import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setGeometry(100, 100, 300, 200)
        label = QLabel("Hello! GUI is working.", self)
        label.move(50, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec_())
