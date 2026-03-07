from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt
from .forecast_item import ForecastItem
from ..utils.api import get_data


class ForecastInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.setFixedSize(790, 157)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")

        self.scroll_element = QScrollArea(self)
        self.scroll_element.setWidgetResizable(True)
        self.scroll_element.setStyleSheet("background-color: transparent;")
        self.main_layout.addWidget(self.scroll_element)
        self.scroll_element.setFixedSize(790, 157)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.scroll_frame = QFrame()
        self.scroll_frame.setStyleSheet("background-color: transparent;")

        self.forecast_layout = QHBoxLayout()
        self.scroll_frame.setLayout(self.forecast_layout)
        
        forecast = get_data("Dnipro")
        
        

        for i in range(12):
            data = forecast["list"][i]
            hour = data["dt_txt"][11:13]
            temp = round(data["main"]["temp"])

            icon_code = data["weather"][0]["icon"]

            if "d" in icon_code:
                icon_name = "day.png"
            else:
                icon_name = "afternoon.png"
        
        
        
            item = ForecastItem(
            time_text = str(hour),
            temp_text = f"{temp}°",
            icon_name = icon_name
            )
            
            self.forecast_layout.addWidget(item)
        self.scroll_element.setWidget(self.scroll_frame)