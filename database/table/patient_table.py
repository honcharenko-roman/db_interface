from database.db_util import Singleton, execute_statement
from database.table.comment_table import CommentTable
from database.table.favourite_table import FavouriteTable


class PatientTable(metaclass=Singleton):
    table_name: str = 'Patient'
    _id_field_name: str = 'id'
    _first_name_field_name: str = 'first_name'
    _last_name_field_name = 'last_name'
    _phone_field_name = 'phone'
    _email_field_name = 'email'
    _medic_id_field_name: str = 'medic_id'

    def __init__(self):
        execute_statement(
            f'''CREATE TABLE if not exists {PatientTable.table_name} (
                {PatientTable._id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {PatientTable._first_name_field_name} TEXT, 
                {PatientTable._last_name_field_name} TEXT, 
                {PatientTable._phone_field_name} TEXT, 
                {PatientTable._email_field_name} TEXT, 
                {PatientTable._medic_id_field_name} INTEGER, 
                FOREIGN KEY ({PatientTable._id_field_name})
                        REFERENCES {CommentTable.table_name} ({CommentTable.medic_id_field_name}) 
                FOREIGN KEY ({PatientTable._id_field_name})
                        REFERENCES {FavouriteTable.table_name} ({FavouriteTable.patient_id_field_name}) 
            )'''
        )

    # @staticmethod
    # def insert(medic: Medic):
    #     execute_statement(
    #         f'''INSERT INTO {MedicTable.table_name} (
    #                 {MedicTable.__fourcc})
    #                 VALUES (?)''',
    #         medic.data()
    #     )

    #
    # @staticmethod
    # def drop_table():
    #     execute_statement(
    #         f'DROP TABLE if exists {MedicTable.table_name}'
    #     )
