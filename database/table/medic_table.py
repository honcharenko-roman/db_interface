from database.db_util import Singleton, execute_statement
from database.table.category_table import CategoryTable
from database.table.table import Table
from entity.medic import Medic


class MedicTable(Table, metaclass=Singleton):
    table_name: str = 'Medic'
    id_field_name: str = 'id'
    _first_name_field_name: str = 'first_name'
    _last_name_field_name = 'last_name'
    _phone_field_name = 'phone'
    _email_field_name = 'email'
    category_id_field_name: str = 'category_id'

    def __init__(self):
        super().__init__(MedicTable.table_name)
        execute_statement(
            f'''CREATE TABLE if not exists {MedicTable.table_name} (
                        {MedicTable.id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,                        {MedicTable._first_name_field_name} TEXT, 
                        {MedicTable._last_name_field_name} TEXT, 
                        {MedicTable._phone_field_name} TEXT, 
                        {MedicTable._email_field_name} TEXT, 
                        {MedicTable.category_id_field_name} INTEGER
                            REFERENCES {CategoryTable.table_name} ({CategoryTable.id_field_name})
                    )'''
        )

    @staticmethod
    def insert(medic: Medic):
        execute_statement(
            f'''INSERT INTO {MedicTable.table_name} 
                        ({MedicTable._first_name_field_name}, 
                        {MedicTable._last_name_field_name},
                        {MedicTable._phone_field_name},
                        {MedicTable._email_field_name},
                        {MedicTable.category_id_field_name}) 
                        VALUES (?,?,?,?,?)''',
            (medic.first_name, medic.last_name, medic.phone, medic.email, medic.category_id,)
        )
