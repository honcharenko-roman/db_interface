from database.db_util import Singleton, execute_statement
from database.table.category_table import CategoryTable
from database.table.table import Table
from entity.medic import Medic


class MedicTable(Table, metaclass=Singleton):
    table_name: str = 'Medic'
    id_field_name: str = 'id'
    first_name_field_name: str = 'first_name'
    last_name_field_name = 'last_name'
    phone_field_name = 'phone'
    email_field_name = 'email'
    category_id_field_name: str = 'category_id'

    def __init__(self):
        super().__init__(MedicTable.table_name)
        execute_statement(
            f'''CREATE TABLE if not exists {MedicTable.table_name} (
                        {MedicTable.id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {MedicTable.first_name_field_name} TEXT, 
                        {MedicTable.last_name_field_name} TEXT, 
                        {MedicTable.phone_field_name} TEXT, 
                        {MedicTable.email_field_name} TEXT, 
                        {MedicTable.category_id_field_name} INTEGER
                            REFERENCES {CategoryTable.table_name} ({CategoryTable.id_field_name})
                    )'''
        )

    @staticmethod
    def insert(medic: Medic):
        execute_statement(
            f'''INSERT INTO {MedicTable.table_name} 
                        ({MedicTable.first_name_field_name}, 
                        {MedicTable.last_name_field_name},
                        {MedicTable.phone_field_name},
                        {MedicTable.email_field_name},
                        {MedicTable.category_id_field_name}) 
                        VALUES (?,?,?,?,?)''',
            (medic.first_name, medic.last_name, medic.phone, medic.email, medic.category_id,)
        )

    def get_all(self):
        medics = []
        for medic in super().get_all():
            medics.append(Medic(data_tuple=medic))
        return medics

    def get_by_category(self, category_id):
        return execute_statement(
            f'SELECT * FROM {self.table_name}'
            f'WHERE ({self.category_id_field_name})=?',
            (category_id,)
        ) or []
