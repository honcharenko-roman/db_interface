import os
import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from database.db_manager import DatabaseManager
from entity.category import Category
from entity.comment import Comment
from entity.medic import Medic
from entity.patient import Patient
from ui.TableQComboBox import TableComboBox


def main():
    db_manager = DatabaseManager()

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(80, 80, 280, 80)
    window.move(60, 15)
    helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
    helloMsg.move(60, 15)

    def onChangedTableQComboBox(value: str):
        helloMsg.setText(value)
        helloMsg.adjustSize()

    c = TableComboBox(onChangedTableQComboBox)
    layout = QHBoxLayout()
    layout.addWidget(c)
    layout.addWidget(helloMsg)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())


def to_dataset(database_all):
    data = {}

    for item in database_all:
        for keys in vars(item).keys:
            data[keys.replace('_', '')] = ''
        # for key, value in vars(item).items():
        #     data[key] = value
        # for value in vars(item)
        # print(keys, values)
    # for item in database:
    #     for keys, values in vars(category).items():
    #         for value in values:
    #
    #     data[keys] = value
    # for key, value in vars(category).values():
    #     data[key] = value

    print(data)

    return {'col1': ['1', '2', '3', '4'],
            'col2': ['1', '2', '1', '3'],
            'col3': ['1', '1', '2', '1']}


def insert_data():
    db_manager.category_table.insert(Category('aaa'))
    db_manager.medic_table.insert(Medic('a', 'b', 'c', 'd', 1))
    db_manager.comment_table.insert(Comment(1, 2, '3'))
    db_manager.comment_table.insert(Comment(1, 2, '333'))
    db_manager.patient_table.insert(Patient('e', 'f', 'g', 'i', 1))
    db_manager.favourite_table.insert(1, 2)


if __name__ == '__main__':
    os.remove("/home/roman/dasha_kurs/data.db")
    db_manager = DatabaseManager()
    insert_data()
    # to_dataset(db_manager.comment_table.get_all())
    # result = db_manager.comment_table.get_all()
    # print(result)
    to_dataset(db_manager.comment_table.get_all())
    # main()
