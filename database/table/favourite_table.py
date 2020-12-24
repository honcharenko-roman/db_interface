from database.db_util import Singleton, execute_statement
from database.table.medic_table import MedicTable
from database.table.patient_table import PatientTable
from database.table.table import Table


class FavouriteTable(Table, metaclass=Singleton):
    table_name: str = 'Favourite'
    medic_id_field_name: str = 'medic_id'
    patient_id_field_name: str = 'patient_id'

    def __init__(self):
        super().__init__(FavouriteTable.table_name)
        execute_statement(
            f'''CREATE TABLE if not exists {FavouriteTable.table_name} (
                {FavouriteTable.medic_id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT
                    REFERENCES {MedicTable.table_name} ({MedicTable.id_field_name}),
                {FavouriteTable.patient_id_field_name} INTEGER
                    REFERENCES {PatientTable.table_name} ({PatientTable.id_field_name})
            )'''
        )

    @staticmethod
    def insert(medic_id, patient_id):
        execute_statement(
            f'''INSERT INTO {FavouriteTable.table_name} 
                ({FavouriteTable.medic_id_field_name},
                {FavouriteTable.patient_id_field_name}) 
                VALUES (?,?)''',
            (medic_id, patient_id)
        )
