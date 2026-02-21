from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os


class TimeInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setFixedSize(390, 303)
        self.setStyleSheet("""
            background: rgba(0,0,0,0.25);
            border-radius: 10px;
            color: white;
        """)

        main = QVBoxLayout(self)
        main.setContentsMargins(25, 25, 25, 25)
        main.setSpacing(15)

        today = QLabel("Сьогодні")
        today.setStyleSheet("font-size: 12px; background-color: transparent;")

        top = QHBoxLayout()

        day = QLabel("Понеділок")
        day.setStyleSheet("font-size: 16px; background-color: transparent;")

        date = QLabel("24.03.2025")
        date.setStyleSheet("font-size: 24px; background-color: transparent;")

        top.addWidget(day)
        top.addStretch()
        top.addWidget(date)

        time = QLabel("14:24")
        time.setStyleSheet("font-size: 29px; background-color: transparent;")
        time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        

        clock_img = QLabel(self)
        clock_img.setStyleSheet("background-color: transparent;")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "..", "..", "images", "clock.png")

        img = QPixmap(path)
        img = img.scaled(168, 168)

        clock_img.setPixmap(img)
        clock_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        

        main.addWidget(today)
        main.addLayout(top)
        main.addStretch()

        clock_img.setFixedSize(168, 168)


        time.setParent(clock_img)
        time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        time.setGeometry(0, 0, 168, 168)

        main.addWidget(clock_img, alignment=Qt.AlignmentFlag.AlignCenter)
        main.addStretch()
