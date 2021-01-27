from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout, QLabel, QLineEdit


class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, table):
        super(Dialog, self).__init__()
        self.createFormGroupBox(table)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Form Layout - pythonspot.com")

    def createFormGroupBox(self, table):
        self.layout = QFormLayout()
        self.edits = {}
        for field in table.get_fields():
            qline_edit = QLineEdit()
            self.edits[field] = qline_edit
            # if 'id' in field:
            self.layout.addRow(QLabel(field), qline_edit)

        self.formGroupBox = QGroupBox("Form layout")
        # layout.addRow(QLabel("Name:"), QLineEdit())
        # layout.addRow(QLabel("Country:"), QComboBox())
        # layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(self.layout)
