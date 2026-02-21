from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt



class City(QFrame):
    def __init__(self, city_name, temp, min_t, max_t, weather, time):
        QFrame.__init__(self)
        self.city_name = city_name
        self.temp = temp
        self.min_temp = min_t
        self.max_temp = max_t
        self.weather = weather
        self.time = time

        main_layout = QHBoxLayout()


        left_layout = QVBoxLayout()

        city_label = QLabel(self.city_name)
        time_label = QLabel(self.time)
        weather_label = QLabel(self.weather)

        city_label.setStyleSheet("color: white; font-size: 24px; font-family: Arial; background-color: transparent;")
        city_label.setFixedSize(247, 28)
        time_label.setStyleSheet("color: white; font-size: 12px; font-family: Arial; background-color: transparent;")
        time_label.setFixedSize(247, 14)
        weather_label.setStyleSheet("color: white; font-size: 12px; font-family: Arial; background-color: transparent;")
        weather_label.setFixedSize(161, 14)

        left_layout.addWidget(city_label)
        left_layout.addWidget(time_label)
        left_layout.addWidget(weather_label)

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        temp_label = QLabel(f"{self.temp}°C")
        range_label = QLabel(f"Min: {self.min_temp}°C  Max: {self.max_temp}°C")

        temp_label.setStyleSheet("color: white; font-size: 44px; font-family: Arial; background-color: transparent;")
        temp_label.setFixedSize(67, 52)
        range_label.setStyleSheet("color: white; font-size: 12px; font-family: Arial; background-color: transparent;")
        range_label.setFixedSize(98, 14)

        right_layout.addWidget(temp_label)
        right_layout.addWidget(range_label)
        

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)