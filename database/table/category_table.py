from database.db_util import Singleton, execute_statement
from database.table.medic_table import MedicTable
from entity.comment import Comment


class CategoryTable(metaclass=Singleton):
    table_name: str = 'Category'
    _id_field_name: str = 'id'
    _name_id_field_name: str = 'medic_id'

    def __init__(self):
        execute_statement(
            f'''CREATE TABLE if not exists {CategoryTable.table_name} (
                {CategoryTable._id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {CategoryTable._name_id_field_name} TEXT,
                FOREIGN KEY ({CategoryTable._id_field_name})
                    REFERENCES {MedicTable.table_name} ({MedicTable.category_id_field_name}) 
            )'''
        )

    @staticmethod
    def insert(comment: Comment):
        execute_statement(
            f'''INSERT INTO {CategoryTable.table_name} 
                ({CategoryTable._name_id_field_name}) 
                VALUES (?,)''',
            comment.data()
        )

    @staticmethod
    def drop_table():
        execute_statement(
            f'DROP TABLE if exists {CategoryTable.table_name}'
        )

    @staticmethod
    def get_all():
        return execute_statement(
            f'SELECT * FROM {CategoryTable.table_name}',
        ) or []
