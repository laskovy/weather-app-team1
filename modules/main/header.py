from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtCore import pyqtSignal



class Header(QFrame):
    add_city_signal = pyqtSignal(str)
    def __init__(self):
        QFrame.__init__(self)
          

        self.setFixedSize(790, 36)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(10, 0, 10, 0)
        self.layout.setSpacing(10)

        
        self.settings_btn = QPushButton("⚙️")
        self.settings_btn.setFixedSize(30, 30)
        self.settings_btn.setStyleSheet("background-color: rgba(255,255,255,0.1); border-radius: 6px; color: white;")

        self.title = QLabel("Налаштування")
        self.title.setStyleSheet("color: white;")

        self.layout.addWidget(self.settings_btn)
        self.layout.addWidget(self.title)

        
        self.layout.addStretch()

        
        self.add_btn = QPushButton("Додати")
        self.add_btn.setFixedHeight(28)
        self.add_btn.setStyleSheet("""
            background-color: rgba(255,255,255,0.1);
            border-radius: 8px;
            color: white;
            padding: 0 10px;
        """)

        
        self.input = QLineEdit()
        self.input.setPlaceholderText("...")
        self.input.setFixedSize(180, 28)  

        self.input.setStyleSheet("""
            background-color: rgba(255,255,255,0.1);
            border-radius: 8px;
            padding-left: 8px;
            color: white;
        """)

        
        self.layout.addWidget(self.add_btn)
        self.layout.addWidget(self.input)

        self.setLayout(self.layout)

        self.add_btn.clicked.connect(self.handle_add_city)
    def handle_add_city(self):
        city_name = self.input.text().strip()
        if city_name:
            self.add_city_signal.emit(city_name)
            self.input.clear()