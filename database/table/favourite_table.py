from database.db_util import Singleton, execute_statement
from entity.comment import Comment


class FavouriteTable(metaclass=Singleton):
    table_name: str = 'Favourite'
    medic_id_field_name: str = 'id'
    patient_id_field_name: str = 'medic_id'

    def __init__(self):
        execute_statement(
            f'''CREATE TABLE if not exists {FavouriteTable.table_name} (
                {FavouriteTable.medic_id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {FavouriteTable.patient_id_field_name} INTEGER
            )'''
        )

    @staticmethod
    def insert(comment: Comment):
        execute_statement(
            f'''INSERT INTO {FavouriteTable.table_name} 
                ({FavouriteTable.patient_id_field_name}) 
                VALUES (?,)''',
            comment.data()
        )

    @staticmethod
    def drop_table():
        execute_statement(
            f'DROP TABLE if exists {FavouriteTable.table_name}'
        )

    @staticmethod
    def get_all():
        return execute_statement(
            f'SELECT * FROM {FavouriteTable.table_name}',
        ) or []
