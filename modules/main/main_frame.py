from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout
from .forecast_info import ForecastInfo
from .graphics_info import GraphicsInfo
from .header import Header
from .weather_info import WeatherInfo
from .time_info import TimeInfo

class MainInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(790, 733)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")


        self.header = Header()
        self.main_layout.addWidget(self.header)
        
        self.main_container = QFrame()
        self.main_container.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

        self.main_container.setFixedSize(790, 303)
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.main_container.setLayout(self.horizontal_layout)

        self.weather_info = WeatherInfo()
        self.horizontal_layout.addWidget(self.weather_info)
        self.time_info = TimeInfo()
        self.horizontal_layout.addWidget(self.time_info)

        self.main_layout.addWidget(self.main_container)

        self.forecast_info = ForecastInfo()
        self.main_layout.addWidget(self.forecast_info)

        self.graphics_info = GraphicsInfo()
        self.main_layout.addWidget(self.graphics_info)
        