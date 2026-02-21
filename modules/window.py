from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt 
from .main import *
from .side_panel import SidePanel
from .title_bar import TitleBar

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
        self.side_panel = SidePanel()
        self.content_layout.addWidget(self.side_panel)
        self.setStyleSheet("""background-color: qlineargradient(
            x1: 0, y1: 1, x2: 1, y2: 0,
            stop: 0 #8A2BE2, stop: 1 #191970
        )""")
        self.main = MainInfo()
        self.content_layout.addWidget(self.main)
        self.content_layout.setContentsMargins(0, 0, 20, 0)
        self.content_layout.setSpacing(20)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # В класі вікна, щоб сховати стандартну панель - self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Qt - головний клас налаштувань (з QtCore)


main_window = Window()
