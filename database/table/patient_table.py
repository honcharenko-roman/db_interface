from database.db_util import Singleton, execute_statement
from database.table.medic_table import MedicTable
from database.table.table import Table
from entity.patient import Patient


class PatientTable(Table, metaclass=Singleton):
    table_name: str = 'Patient'
    id_field_name: str = 'id'
    _first_name_field_name: str = 'first_name'
    _last_name_field_name = 'last_name'
    _phone_field_name = 'phone'
    _email_field_name = 'email'
    medic_id_field_name: str = 'medic_id'

    def __init__(self):
        super().__init__(PatientTable.table_name)
        execute_statement(
            f'''CREATE TABLE if not exists {PatientTable.table_name} (
                {PatientTable.id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {PatientTable._first_name_field_name} TEXT, 
                {PatientTable._last_name_field_name} TEXT, 
                {PatientTable._phone_field_name} TEXT, 
                {PatientTable._email_field_name} TEXT, 
                {PatientTable.medic_id_field_name} INTEGER 
                    REFERENCES {MedicTable.table_name} ({MedicTable.id_field_name})
            )'''
        )

    @staticmethod
    def insert(patient: Patient):
        execute_statement(
            f'''INSERT INTO {PatientTable.table_name} 
                            ({PatientTable._first_name_field_name}, 
                            {PatientTable._last_name_field_name},
                            {PatientTable._phone_field_name},
                            {PatientTable._email_field_name},
                            {PatientTable.medic_id_field_name}) 
                            VALUES (?,?,?,?,?)''',
            (patient.first_name, patient.last_name, patient.phone, patient.email, patient.medic_id,)
        )

    def get_all(self):
        patients = []
        for patient in super().get_all():
            patients.append(Patient(data_tuple=patient))
        return patients
