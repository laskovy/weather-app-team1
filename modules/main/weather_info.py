from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt
import os
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtSvg import QSvgRenderer
from modules.utils.api import get_weather


class WeatherInfo(QFrame):
    def __init__(self, city_name):
        QFrame.__init__(self)

        self.setFixedSize(390, 303)
        self.setStyleSheet("""
            background: rgba(0,0,0,0.25);
            border-radius: 10px;
            color: white;
        """)
        data = get_weather(city_name)

        main = QVBoxLayout(self)
        main.setContentsMargins(25, 25, 25, 25)
        main.setSpacing(15)


        city = data["name"]
        temp = round(data["main"]["temp"])
        temp_min = round(data["main"]["temp_min"])
        temp_max = round(data["main"]["temp_max"])
        status = data["weather"][0]["description"].capitalize()
        icon_code = data["weather"][0]["icon"]


        city_label = QLabel(city)
        city_label.setStyleSheet("font-size: 44px; background: transparent;")
        city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        temp_label = QLabel(f"{temp}°")
        temp_label.setStyleSheet("font-size: 74px; background: transparent;")

        status_label = QLabel(status)
        status_label.setStyleSheet("font-size: 24px; background: transparent;")
        status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        minmax = QLabel(f"Макс: {temp_max}°   Мін: {temp_min}°")
        minmax.setStyleSheet("font-size: 16px; background: transparent;")
        minmax.setAlignment(Qt.AlignmentFlag.AlignCenter)

        

        weather_img = QLabel(self)
        weather_img.setFixedSize(160, 160)
        weather_img.setStyleSheet("background-color: transparent;")

        icon_name = f"{icon_code}.svg"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "..", "..", "icons", "light", icon_name)

        renderer = QSvgRenderer(path)
        pixmap = QPixmap(path)
        pixmap.scaled(220, 220, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        img = QPixmap(path)
        img = img.scaled(140, 140)

        weather_img = QLabel()
        weather_img.setPixmap(pixmap)
        

        

        middle = QHBoxLayout()
        middle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        middle.addSpacing(5)

        middle.addWidget(weather_img, alignment=Qt.AlignmentFlag.AlignBottom)
        middle.addWidget(temp_label, alignment=Qt.AlignmentFlag.AlignBottom)
        
        

        main.addWidget(city_label)
        main.addSpacing(10)

        main.addLayout(middle)   

        main.addWidget(status_label)
        main.addWidget(minmax)

        main.addStretch()