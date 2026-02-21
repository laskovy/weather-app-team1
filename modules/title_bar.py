from PyQt6.QtWidgets import QLabel, QFrame, QHBoxLayout, QToolButton
from PyQt6.QtGui import QIcon

class TitleBar(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(1200, 50)
        self.setStyleSheet("background-color: gray")
        self.setLayout(self.main_layout)

        self.button_frame = QFrame()
        self.button_layout = QHBoxLayout()
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_frame.setLayout(self.button_layout)
        self.main_layout.addWidget(self.button_frame)

        self.title_text = QLabel(text="WeatherApp")
        self.main_layout.addWidget(self.title_text)

        self.close_button = QToolButton()
        self.hide_button = QToolButton()
        self.openfull_button = QToolButton()
        self.close_button.setIcon(QIcon("images/close.svg"))
        self.hide_button.setIcon(QIcon("images/hide.svg"))
        self.openfull_button.setIcon(QIcon("images/full.svg"))
        
        self.button_layout.addWidget(self.close_button)
        self.button_layout.addWidget(self.hide_button)
        self.button_layout.addWidget(self.openfull_button)
        
        window = self.window()
        self.close_button.clicked.connect(window.close)
        self.hide_button.clicked.connect(window.showMinimized)
        self.openfull_button.clicked.connect(window.showMaximized)
