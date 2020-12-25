import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QHBoxLayout, QCheckBox
from PyQt5.QtWidgets import QWidget

from database.db_manager import DatabaseManager
from entity.category import Category
from entity.comment import Comment
from entity.medic import Medic
from entity.patient import Patient
from ui.combo_box import TableComboBox
from ui.table_view import TableView


def main():
    db_manager = DatabaseManager()

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Bendas Daria/Course Project')
    window.resize(800, 600)

    table_view = TableView()

    add_button = QPushButton('Add', parent=window)
    remove_button = QPushButton('Remove', parent=window)

    def handleRemoveButton(self):
        table = db_manager.get_by_table_name(combo_box.currentText())
        for index_to_remove in table_view.checked_id:
            table.remove_by_id(index_to_remove)

        onChangedTableQComboBox(combo_box.currentText())


    def handleAddButton(self):
        print(table_view.checked_id)

    def onChangedTableQComboBox(value: str):
        table_view.clear()
        dataset = db_manager.get_by_table_name(value).get_dataset()
        table_view.data = dataset
        table_view.setData()

    add_button.clicked.connect(handleAddButton)
    remove_button.clicked.connect(handleRemoveButton)
    combo_box = TableComboBox(onChangedTableQComboBox)

    main_layout = QVBoxLayout()

    top_panel = QHBoxLayout()
    top_panel.addWidget(combo_box)
    top_panel.addWidget(add_button)
    top_panel.addWidget(remove_button)

    table_panel = QHBoxLayout()
    table_panel.addWidget(table_view)
    table_panel.addWidget(add_button)

    main_layout.addLayout(top_panel)
    main_layout.addWidget(table_view)

    window.setLayout(main_layout)
    window.show()

    sys.exit(app.exec_())


def insert_data():
    db_manager.category_table.insert(Category('Dermatologist'))
    db_manager.category_table.insert(Category('Pediatrician'))
    db_manager.category_table.insert(Category('Family Physician'))
    db_manager.category_table.insert(Category('Gynecologist'))
    db_manager.category_table.insert(Category('Surgeon'))
    db_manager.category_table.insert(Category('Psychiatrist'))
    db_manager.category_table.insert(Category('Cardiologist'))

    db_manager.medic_table.insert(Medic('Samantha', 'Bailey', '+44(0)0756 5946224', 'samaey@gmail.com', 1))
    db_manager.medic_table.insert(Medic('Rob', 'Chapman', '+44(0)7727 269126', 'robchaman@gmail.com', 3))
    db_manager.medic_table.insert(Medic('Tara', 'Powell', '+44(0)8246 130379', 'taraell@gmail.com', 2))
    db_manager.medic_table.insert(Medic('Tyler', 'Miller', '+44(0)0177 6810506', 'tyleler@gmail.com', 5))

    db_manager.comment_table.insert(Comment(1, 1636314, 'My doctor didn’t return my call.'))
    db_manager.comment_table.insert(Comment(2, 1636314, 'You can put her in the hallway…if you can find a bed.'))
    db_manager.comment_table.insert(Comment(4, 1636314, 'This is the fifth time in two weeks we’ve sent him in'))
    db_manager.comment_table.insert(Comment(3, 1636314, 'Outstanding! I heard at least half of them this week'))
    db_manager.comment_table.insert(Comment(2, 1636314, 'This long after the hurricanes we have severe overcrowd'))
    db_manager.comment_table.insert(Comment(1, 1636314, 'Thanks for the comments!'))
    db_manager.comment_table.insert(Comment(2, 1636314, 'My favorite is when you are working sicker than patient!'))
    db_manager.comment_table.insert(Comment(4, 1636314, 'Outstanding! I heard at least half of them this week'))
    db_manager.comment_table.insert(Comment(3, 1636314, 'I hope I won’t be down there long.'))
    db_manager.comment_table.insert(Comment(2, 4361531, 'I figured I’d get seen quicker this way.'))
    db_manager.comment_table.insert(Comment(1, 4361531, 'Its been going on about a month.'))
    db_manager.comment_table.insert(Comment(3, 4361531, 'The medicine they gave me yesterday didn’t work.'))
    db_manager.comment_table.insert(Comment(4, 4361531, 'Unprofessional at all!'))

    db_manager.patient_table.insert(Patient('Stefan', 'Hill', '+44(0)0204 2043110', 'keithhill@gmail.com', 1))
    db_manager.patient_table.insert(Patient('Keith', 'Wilson', '+44(0)0423 4505694', 'stefaon@gmail.com', 2))
    db_manager.patient_table.insert(Patient('Kyle', 'Wilson', '+44(0)0423 4505694', 'stefaon@gmail.com', 2))
    db_manager.patient_table.insert(Patient('Kyle', 'Cook', '+44(0)7122 66096', 'kylecok@gmail.com', 2))
    db_manager.patient_table.insert(Patient('David', 'Campbell', '+44(0)8844 31029', 'daviell@gmail.com', 2))
    db_manager.patient_table.insert(Patient('Daniel', 'Wright', '+44(0)4997 204627', 'danieht@gmail.com', 2))
    db_manager.patient_table.insert(Patient('Freya', 'Martin', '+44(0)0320 0751033', 'freyatin@gmail.com', 2))
    db_manager.patient_table.insert(Patient('Summer', 'Johnson', '+44(0)0249 6843714', 'summson@gmail.com', 2))

    db_manager.favourite_table.insert(1, 1)
    db_manager.favourite_table.insert(2, 2)
    db_manager.favourite_table.insert(3, 3)
    db_manager.favourite_table.insert(4, 4)
    db_manager.favourite_table.insert(3, 5)
    db_manager.favourite_table.insert(2, 6)
    db_manager.favourite_table.insert(1, 7)
    db_manager.favourite_table.insert(1, 8)


if __name__ == '__main__':
    os.remove("/home/roman/db_interface/data.db")
    db_manager = DatabaseManager()
    insert_data()
    main()
