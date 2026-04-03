from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
import os
from datetime import datetime


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

        self.day = QLabel()
        self.day.setStyleSheet("font-size: 16px; background-color: transparent;")

        self.date = QLabel()
        self.date.setStyleSheet("font-size: 24px; background-color: transparent;")

        top.addWidget(self.day)
        top.addStretch()
        top.addWidget(self.date)

        self.time = QLabel()
        self.time.setStyleSheet("font-size: 29px; background-color: transparent;")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        

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


        self.time.setParent(clock_img)
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.setGeometry(0, 0, 168, 168)

        main.addWidget(clock_img, alignment=Qt.AlignmentFlag.AlignCenter)
        main.addStretch()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)
        self.update_datetime()

    def update_datetime(self):
        from datetime import datetime    

        days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

        self.day.setText(days[datetime.now().weekday()])
        self.date.setText(datetime.now().strftime("%d.%m.%Y"))
        self.time.setText(datetime.now().strftime("%H:%M"))