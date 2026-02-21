from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os


class WeatherInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setFixedSize(390, 303)
        self.setStyleSheet("""
            background: rgba(0,0,0,0.25);
            border-radius: 10px;
            color: white;
        """)

        main = QVBoxLayout(self)
        main.setContentsMargins(25, 25, 25, 25)
        main.setSpacing(15)

        city1 = QLabel("Ватикан")
        city1.setStyleSheet("font-size: 44px; background-color: transparent;")
        city1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        temp = QLabel("14°")
        temp.setStyleSheet("font-size: 74px; background-color: transparent;")

        status = QLabel("Дощ")
        status.setStyleSheet("font-size: 24px; background-color: transparent;")
        status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        minmax = QLabel("Макс: 15°   Мін: 1°")
        minmax.setStyleSheet("font-size: 16px; background-color: transparent;")
        minmax.setAlignment(Qt.AlignmentFlag.AlignCenter)

        

        weather_img = QLabel(self)
        weather_img.setFixedSize(160, 160)
        weather_img.setStyleSheet("background-color: transparent;")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "..", "..", "images", "rain.png")

        img = QPixmap(path)
        img = img.scaled(140, 140)

        weather_img.setPixmap(img)

        

        middle = QHBoxLayout()
        middle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        middle.addSpacing(5)

        middle.addWidget(weather_img, alignment=Qt.AlignmentFlag.AlignBottom)
        middle.addWidget(temp, alignment=Qt.AlignmentFlag.AlignBottom)
        
        

        main.addWidget(city1)
        main.addSpacing(10)

        main.addLayout(middle)   

        main.addWidget(status)
        main.addWidget(minmax)

        main.addStretch()
