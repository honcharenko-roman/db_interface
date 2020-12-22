from PyQt5.QtWidgets import QComboBox


class TableComboBox(QComboBox):
    def __init__(self, onChangeMethod):
        super().__init__()
        self.addItem('a')
        self.addItem('b')
        self.activated[str].connect(onChangeMethod)
