from PyQt6.QtWidgets import QFrame

class Header(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(790, 36)