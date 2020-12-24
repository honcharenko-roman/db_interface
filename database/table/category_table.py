from database.db_util import Singleton, execute_statement
from entity.category import Category


class CategoryTable(metaclass=Singleton):
    table_name: str = 'Category'
    id_field_name: str = 'id'
    _name_id_field_name: str = 'name'

    def __init__(self):
        execute_statement(
            f'''CREATE TABLE if not exists {CategoryTable.table_name} (
                {CategoryTable.id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {CategoryTable._name_id_field_name} TEXT
            )'''
        )

    @staticmethod
    def insert(category: Category):
        execute_statement(
            f'''INSERT INTO {CategoryTable.table_name} 
                ({CategoryTable._name_id_field_name}) 
                VALUES (?)''',
            (category.name,)
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
