from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("BitLink End-Point")
        self.setGeometry(100, 100, 1200, 850)  # x, y, width, height
        self.setFixedSize(1200, 850)  # Prevent resizing

        # Create a main frame for the window
        self.main_frame = QFrame(self)
        self.main_frame.setStyleSheet("background-color: gray17;")  # Set background color
        self.main_frame.setFixedSize(1200, 850)

        # Add layout to the frame (PyQt doesn't use pack, uses layouts)
        layout = QVBoxLayout(self.main_frame)
        self.main_frame.setLayout(layout)

# Entry point for the PyQt5 application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
