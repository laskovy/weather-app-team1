from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt, QTimer
from modules.main.city import City
from modules.utils.api import get_weather, load_cities, save_cities  
from datetime import datetime, timezone, timedelta


class SidePanel(QFrame):
    def __init__(self, main_window):
        QFrame.__init__(self)
        self.main_window = main_window
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.1);
            border: 0;
        """)

        self.setFixedSize(370, 800)

        self.main_layout = QVBoxLayout()

        self.scroll_element = QScrollArea(self)
        self.scroll_element.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_element)

        self.scroll_element.setFixedSize(370, 800)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.content = QFrame()
        self.content.setLayout(self.vertical_layout)

        self.cards = []

        
        cities = load_cities()

        for city in cities:
            self.add_city(city)
        self.vertical_layout.addStretch()

        self.scroll_element.setWidget(self.content)
        self.setLayout(self.main_layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_times)
        self.timer.start(60000)

    
    def add_city(self, city_name):
        if city_name.lower() in [c.city_name.lower() for c in self.cards]:
            return

        data = get_weather(city_name)
        if not data or data.get("cod") != 200:
            return

        utc_now = datetime.now(timezone.utc)
        city_time = utc_now + timedelta(seconds=data["timezone"])
        time_now = city_time.strftime("%H:%M")

        card = City(
            data["name"],
            str(round(data["main"]["temp"])),
            str(round(data["main"]["temp_min"])),
            str(round(data["main"]["temp_max"])),
            data["weather"][0]["description"].capitalize(),
            time_now,
            data["timezone"],
            data["weather"][0]["icon"]  
    )

        card.setStyleSheet("background-color: transparent;")
        card.on_click = self.main_window.change_city

        self.cards.append(card)
        self.vertical_layout.insertWidget(0, card)

        
        city_names = [c.city_name for c in self.cards]
        save_cities(city_names)
        self.vertical_layout.addStretch()
    def update_times(self):
        for card in self.cards:
            card.update_time()

    def select_card(self, selected_card):
        for card in self.cards:
            if card == selected_card:
                card.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 10px;")
            else:
                card.setStyleSheet("background-color: transparent;")
        self.main_window.set_background(selected_card.icon)