from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt 
from .main import *
from .side_panel import SidePanel
from .title_bar import TitleBar

bg_colors = {
    "01d": ("#87CEFA", "#FFDF56"),
    "02d": ("#87CEFA", "#FFDF56"),

    "01n": ("#191970", "#8A2BE2"),
    "02n": ("#191970", "#8A2BE2"),

    "03d": ("#C0C0C0", "#FFD27F"),
    "03n": ("#696969", "#9974BC"),

    "04d": ("#A9A9A9", "#696969"),
    "04n": ("#A9A9A9", "#696969"),

    "09d": ("#808080", "#5DACE2"),
    "09n": ("#808080", "#5DACE2"),
    "10d": ("#808080", "#5DACE2"),
    "10n": ("#808080", "#5DACE2"),

    "11d": ("#4A4A4A", "#5DACE2"),
    "11n": ("#4A4A4A", "#5DACE2"),

    "13d": ("#FFFFFF", "#B0C4DE"),
    "13n": ("#FFFFFF", "#B0C4DE"),
}

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(100, 100, 1200, 850)
        self.setWindowTitle("Project")
        self.central_widget = QFrame()
        self.main_layout = QVBoxLayout() 
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        self.title_bar = TitleBar(self)
        self.content = QFrame()
        self.setFixedSize(1200, 850)
        self.main_layout.addWidget(self.title_bar)
        self.main_layout.addWidget(self.content)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.content_layout = QHBoxLayout()
        self.content.setLayout(self.content_layout)
        self.side_panel = SidePanel(self)
        self.content_layout.addWidget(self.side_panel)

        for card in self.side_panel.cards:  
            card.on_click = self.change_city

        self.main = MainInfo("Dnipro")
        self.content_layout.addWidget(self.main)
        self.content_layout.setContentsMargins(0, 0, 20, 0)
        self.content_layout.setSpacing(20)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.main.header.add_city_signal.connect(self.side_panel.add_city)

        if self.side_panel.cards:
            first = self.side_panel.cards[0]
            self.set_background(first.icon)
    def set_background(self, icon_code):
        colors = bg_colors.get(icon_code)

        if not colors:
            return

        c1, c2 = colors

        self.setStyleSheet(f"""
            background-color: qlineargradient(
                x1: 0, y1: 1, x2: 1, y2: 0,
                stop: 0 {c1}, stop: 1 {c2}
            );
        """)


    def change_city(self, selected_card):  
        self.side_panel.select_card(selected_card)  

        
        self.set_background(selected_card.icon)

        city_name = selected_card.city_name

        self.content_layout.removeWidget(self.main)  
        self.main.deleteLater()  

        self.main = MainInfo(city_name)  
        self.content_layout.addWidget(self.main)

        self.main.header.add_city_signal.connect(self.side_panel.add_city)

        
        # В класі вікна, щоб сховати стандартну панель - self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Qt - головний клас налаштувань (з QtCore)


main_window = Window()