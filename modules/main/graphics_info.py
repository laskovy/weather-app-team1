from PyQt6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel
from ..utils import get_temp
from PyQt6.QtCore import Qt

class GraphicsInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(790, 197)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")
        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        # layout.setAlignment(Qt.AlignmentFlag) - вирівнювання елементів (Qt з QtCore)
        self.setLayout(self.main_layout)
        min_visible_temp, list_height = get_temp()
        for height in list_height:
            frame = QFrame()
            frame.setFixedHeight(height)
            frame.setStyleSheet("""background-color: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #FFDF56, stop: 1 #87CEFA
            )""")
            self.main_layout.addWidget(frame, alignment=Qt.AlignmentFlag.AlignBottom)
            
        self.temp_frame = QFrame()
        self.temp_layout = QVBoxLayout()
        self.temp_frame.setLayout(self.temp_layout)
        
        max_temp = min_visible_temp + 35 
        for count in range(8):
            temp = max_temp - count *5 
            text = QLabel(text=f"{temp}°")
            text.setStyleSheet("background-color: transparent")
            self.temp_layout.addWidget(text)
        
        self.main_layout.addWidget(self.temp_frame)