import os
import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from database.db_manager import DatabaseManager
from entity.category import Category
from entity.comment import Comment
from entity.medic import Medic
from entity.patient import Patient
from ui.TableQComboBox import TableComboBox
from ui.table_view import TableView


def main():
    db_manager = DatabaseManager()

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Bendas Daria/Course Project')
    window.resize(800, 600)

    table_view = TableView()

    def onChangedTableQComboBox(value: str):
        table_view.clear()
        dataset = db_manager.get_by_table_name(value).get_dataset()
        table_view.data = dataset
        table_view.setData()

    c = TableComboBox(onChangedTableQComboBox)
    layout = QVBoxLayout()
    c.adjustSize()
    table_view.adjustSize()
    layout.addWidget(c)

    layout.addWidget(table_view)
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())


# def to_dataset(database_all, table):
#     data = {}
#
#     for item in database_all:
#         for key in vars(item).keys():
#             data[key[1:]] = table.get_column_values(key[1:])
#
#     return data


def insert_data():
    db_manager.category_table.insert(Category('Therapy'))
    db_manager.medic_table.insert(
        Medic('Ivan', 'Ivanov', '+380999', 'ii@gmail.com', 1)
    )
    db_manager.comment_table.insert(Comment(1, 1636314, 'Very professional'))
    db_manager.comment_table.insert(Comment(1, 4361531, 'Unprofessional at all!'))
    db_manager.patient_table.insert(
        Patient('Svyat', 'Gnode', '+380888', 'sg@gmail.com', 1)
    )
    db_manager.patient_table.insert(
        Patient('Svyat', 'Gnode', '+380888', 'sg@gmail.com', 1)
    )
    db_manager.favourite_table.insert(1, 1)


if __name__ == '__main__':
    os.remove("/home/roman/dasha_kurs/data.db")
    db_manager = DatabaseManager()
    insert_data()
    print(db_manager.comment_table.get_dataset())
    print(db_manager.get_by_table_name('Medic'))
    # print(to_dataset(db_manager.comment_table.get_all(), db_manager.comment_table))
    # result = db_manager.comment_table.get_all()
    # print(result)
    # print(db_manager.comment_table.get_column_values(db_manager.comment_table.timestamp_field_name))
    main()
