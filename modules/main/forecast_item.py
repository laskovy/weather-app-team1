import os
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class ForecastItem(QFrame):
    def __init__(self, time_text="14", temp_text="11", icon_name="day.png"):
        QFrame.__init__(self)

        self.setFixedSize(45, 72)
        self.setStyleSheet("background-color: transparent;")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(6)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_label = QLabel(time_text)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("color: white;")
        self.main_layout.addWidget(self.time_label)
        

        self.icon_label = QLabel()
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "..", "..", "images", icon_name)

        self.icon_label.setPixmap(QPixmap(path))
        self.main_layout.addWidget(self.icon_label)

        self.temp_label = QLabel(temp_text)
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet("color: white;")
        self.main_layout.addWidget(self.temp_label)
