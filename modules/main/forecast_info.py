from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt
from .forecast_item import ForecastItem


class ForecastInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.setFixedSize(790, 157)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")

        self.scroll_element = QScrollArea(self)
        self.scroll_element.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_element)
        self.scroll_element.setFixedSize(790, 157)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.scroll_frame = QFrame()

        self.forecast_layout = QHBoxLayout()
        self.scroll_frame.setLayout(self.forecast_layout)

        start_hour = 14
        temps = [11, 11, 10, 8, 5, 4, 3, 3, 0, 0, 0, 0]

        for i in range(len(temps)):
            hour = (start_hour + i) % 24
            temp = temps[i]
            if hour < 18:
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