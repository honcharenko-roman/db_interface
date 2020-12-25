from database.db_util import Singleton, execute_statement
from database.table.table import Table
from entity.category import Category


class CategoryTable(Table, metaclass=Singleton):
    table_name: str = 'Category'
    id_field_name: str = 'id'
    name_field_name: str = 'name'

    def __init__(self):
        super().__init__(CategoryTable.table_name)
        execute_statement(
            f'''CREATE TABLE if not exists {CategoryTable.table_name} (
                {CategoryTable.id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {CategoryTable.name_field_name} TEXT
            )'''
        )

    @staticmethod
    def insert(category: Category):
        execute_statement(
            f'''INSERT INTO {CategoryTable.table_name} 
                ({CategoryTable.name_field_name}) 
                VALUES (?)''',
            (category.name,)
        )

    def get_all(self):
        categories = []
        for category in super().get_all():
            categories.append(Category(data_tuple=category))
        return categories
