from PyQt5.QtWidgets import QComboBox


class TableComboBox(QComboBox):
    def __init__(self, onChangeMethod):
        super().__init__()
        self.addItem('Medic')
        self.addItem('Patient')
        self.addItem('Comment')
        self.addItem('Category')
        self.activated[str].connect(onChangeMethod)
