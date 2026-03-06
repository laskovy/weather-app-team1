from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from modules.main.city import City
from .main.city import *
from modules.utils.api import get_weather
from datetime import datetime, timezone, timedelta

class SidePanel(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.1);
            border: 0
        """)
        # В стилях колір rgba - працює з прозорістю (4-ете число від 0 до 1)
        self.setFixedSize(370, 800)
        self.main_layout = QVBoxLayout()
        self.scroll_element = QScrollArea(self)
        self.scroll_element.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_element)
        self.scroll_element.setFixedSize(370, 800)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.vertical_layout = QVBoxLayout()
        self.content = QFrame()
        self.content.setLayout(self.vertical_layout)

        cities = ["Dnipro", "Kyiv", "Bratislava", "Warsaw", "Rome, IT"]
        for city in cities:
            data = get_weather(city)
            if data:
                utc_now = datetime.now(timezone.utc)
                city_time = utc_now + timedelta(seconds=data["timezone"])
                time_now = city_time.strftime("%H:%M")

                
                card = City(
                    data["name"],
                    str(round(data["main"]["temp"])),
                    str(round(data["main"]["temp_min"])),
                    str(round(data["main"]["temp_max"])),
                    data["weather"][0]["description"].capitalize(),
                    time_now
                )
                card.setStyleSheet("background-color: transparent;")

                self.vertical_layout.addWidget(card)
                  
        
        # card1 = City(data["name"], str(round(data["main"]["temp"])), str(round(data["main"]["temp_min"])), str(round(data["main"]["temp_max"])), data["weather"][0]["description"].capitalize(), time_now)
        # self.setStyleSheet("""
        #      background-color: transparent);
            
        #      """)
        # self.vertical_layout.addWidget(card1)
        
        # card2 = City(data["name"], str(round(data["main"]["temp"])), str(round(data["main"]["temp_min"])), str(round(data["main"]["temp_max"])), data["weather"][0]["description"].capitalize(), time_now)
        # self.setStyleSheet("""
        #      background-color: transparent);
        #      """)
        # self.vertical_layout.addWidget(card2)
        
        # card3 = City(data["name"], str(round(data["main"]["temp"])), str(round(data["main"]["temp_min"])), str(round(data["main"]["temp_max"])), data["weather"][0]["description"].capitalize(), time_now)
        # self.setStyleSheet("""
        #      background-color: transparent);
        #      """)
        # self.vertical_layout.addWidget(card3)
        
        # card4 = City(data["name"], str(round(data["main"]["temp"])), str(round(data["main"]["temp_min"])), str(round(data["main"]["temp_max"])), data["weather"][0]["description"].capitalize(), time_now)
        # self.setStyleSheet("""
        #      background-color: transparent);
        #      """)
        # self.vertical_layout.addWidget(card4)
        
        # card5 = City(data["name"], str(round(data["main"]["temp"])), str(round(data["main"]["temp_min"])), str(round(data["main"]["temp_max"])), data["weather"][0]["description"].capitalize(), time_now)
        # self.setStyleSheet("""
        #      background-color: transparent);
        #      """)
        # self.vertical_layout.addWidget(card5)

        self.scroll_element.setWidget(self.content)
        self.setLayout(self.main_layout)
        