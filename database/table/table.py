from database.db_util import execute_statement


class Table:
    table_name: str

    def __init__(self, table_name):
        self.table_name = table_name

    def drop_table(self):
        execute_statement(
            f'DROP TABLE if exists {self.table_name}'
        )
